# Lidl "Marty Dupreme" Sign Up Script
This is an extremely simple and lightweight Python tool for automating entries to the popular Lidl "Marty Dupreme" Jacket which was available only via a ballot, which was built as an exploration into raw HTTP-based web automation beyond traditional browser tools and automation.


## Background
Lidl have dropped mystery boxes and special items for over 2 years now and each time I've been succesful with this almost every time due to automation and adequate antibot evasion techniques. The success of this script is shown in the images within this directory to support the quality of the script and emphasise the fact that entries using this method did NOT get filtered despite the sites best attempts. This script utilises:
- **TLS Client Spoofing** - Mimicking browser fingerprints to bypass basic bot detection
- **API Reverse Engineering** - Understanding how web applications communicate under the hood 
- **Request Parameter Analysis** - Crafting authentic-looking requests that mirror real browser behaviour

## How It Works
This script requests Lidl's submission API with a valid payload, generated using randomised information and selected information from the user's CSV. This is then submitted through a TLS-spoofed session which emulates Chrome to minimise flagging. This is further secured through residential proxy intergration which is a typical flagging method most antibots and software use.

## Requirements
```
asyncio
aiohttp
tls_client
```

## Future Additions
There's not many thing i'd add going forward as this is a "one and done" script, but if it does come back and the code remained the same, the additions I'd suggest would be:
```
- Threading requests to save time (will require good enough processing power depeding on the number of threads you're running / data you're submitting)
- Dynamic delays to further prevent any flagging, such as ``sleep(randint(3,10))``
```

## Disclaimer
This project is open-sourced purely for **educational purposes** to understand web automation techniques. Automated account creation violates Lidl's Terms of Service. Use responsibly and at your own risk.

