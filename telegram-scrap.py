import os
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from dotenv import load_dotenv
import re
import json


load_dotenv() 

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print("👌 Successfully joined the channel")
    except Exception as e:
        print("💀 Failed to join the channel:", e)

async def main():
    await client.start()
    
    channel_link = "https://t.me/Afromile"  
    await join_channel(client, channel_link)
    await scrape_messages(client, channel_link, 1)

async def scrape_messages(client, channel, limit=5):
    async for message in client.iter_messages(channel, limit):
        if not message.text:
            continue

        text = message.text.strip()
        parts = text.strip().split("\n\n", 2)

        # ---- Split lines ----
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        # ---- Title (first line) ----
        title = lines[0] if lines else None

        # ---- Description (rest) ----
        description = parts[1] if len(parts) > 1 else None

        # ---- Price (ETB) ----
        price_match = re.search(r'(\d+)\s*ETB', text)
        price = price_match.group(0) if price_match else None

        # ---- Image ----
        image_path = None
        if message.photo:
            image_path = await message.download_media(file="images/")

        # ---- Structured result ----
        event = {
            "title": title,
            "description": description,
            "price": price,
            "image": image_path,
            "date_posted": message.date.isoformat() if message.date else None,
            "views": message.views
        }

        print("📌 EVENT FOUND")
        print(json.dumps(event, indent=2, ensure_ascii=False))
        print("-" * 50)


with client:
    client.loop.run_until_complete(main())
