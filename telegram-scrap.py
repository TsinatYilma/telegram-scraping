import os, requests
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from extractor import extract_title, extract_description, extract_price
from state import load_last_id, save_last_id
from dotenv import load_dotenv
from lib.upload_image import upload_image
import re
import json


load_dotenv() 

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
api_endpoint = os.getenv("API_END")

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
    await scrape_messages(client, channel_link, 100)

async def scrape_messages(client, channel, limit=5):

    events = []
    last_id = load_last_id(channel)
    max_seen_id = last_id

    async for message in client.iter_messages(channel, limit):
        if not message.text or message.id <= last_id:
            continue

        text = message.text.strip()
        parts = text.strip().split("\n\n", 2)

    
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        #IDD
        messageId = message.id

        # TITLE
        title = extract_title(text)

        # DESCRIPTION
        description = extract_description(text)
        
        #PRICE
        price = extract_price(text)

        # ---- Image ----
        image_path = None
        if message.photo:
            image_path = await message.download_media(file="images/")
            image_url = image_url = upload_image(image_path)

        # FINALE OBJECT
        events.append({
            "messageId": messageId,
            "title": title,
            "description": description,
            "price": price,
            "image": image_url,
            "datePosted": message.date.isoformat() if message.date else None,
        })
        max_seen_id = max(max_seen_id, message.id)

        print("📌 EVENT FOUND")
        
    if events:
        response = requests.post(api_endpoint, json=events)
        save_last_id(channel, max_seen_id)
        print(f"✅ {len(events)} new events from {channel}")
        print(f"the api response {response}")
    else:
        print(f"ℹ️ No new events from {channel}")

    
    for event in events:
        print(f"{event}")
                

with client:
    client.loop.run_until_complete(main())
