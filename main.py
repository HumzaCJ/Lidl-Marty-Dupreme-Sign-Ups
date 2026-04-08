import csv
import time
import asyncio
import aiohttp
import tls_client

apiKey = "put your capsolver key here before running (although obselete now)"

async def get_turnstile_token(session):
    async with session.post("https://api.capsolver.com/createTask", json={
        "clientKey": apiKey,
        "task": {
            "type": "AntiTurnstileTaskProxyLess",
            "websiteURL": "https://www.lidlsupermarketdupreme.co.uk/product/dupreme-jacket",
            "websiteKey": "0x4AAAAAACAulWi76TKOWFt8",
        }
    }) as resp:
        data = await resp.json()
        task_id = data["taskId"]
    
    while True:
        async with session.post("https://api.capsolver.com/getTaskResult", json={
            "clientKey": apiKey,
            "taskId": task_id
        }) as resp:
            result = await resp.json()
            if result["status"] == "ready":
                return result["solution"]["token"]
        await asyncio.sleep(1)

def parse_proxy(proxy_str):
    ip, port, user, pwd = proxy_str.strip().split(":")
    return f"http://{user}:{pwd}@{ip}:{port}"

async def submit_entry(aio_session, row, proxy, index):
    try:
        token = await get_turnstile_token(aio_session)
        
        json_data = {
            "name": row["name"],
            "email": row["email"],
            "phone": "",
            "address1": "",
            "address2": "",
            "town": "",
            "county": "",
            "postcode": row["postcode"],
            "consent": True,
            "cfToken": token,
            "startedAt": int(time.time() * 1000) - 5000,
            "hp": "",
        }
        
        tls_session = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)
        response = tls_session.post("https://www.lidlsupermarketdupreme.co.uk/api/entries", json=json_data, proxy=proxy)
        print(f"[{index}] {row['email']} - {response.status_code}")
    except Exception as e:
        print(f"[{index}] {row['email']} - FAILED: {e}")

async def main():
    with open("resi.txt") as f:
        proxies = [line.strip() for line in f if line.strip()]
    
    with open("data.csv") as f:
        rows = list(csv.DictReader(f))
    
    async with aiohttp.ClientSession() as aio_session:
        tasks = [
            submit_entry(aio_session, row, parse_proxy(proxies[i % len(proxies)]), i + 1)
            for i, row in enumerate(rows)
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
