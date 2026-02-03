import os
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from dotenv import load_dotenv

load_dotenv() 

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def join_channel(client, channel_link):
    try:
        await client(JoinChannelRequest(channel_link))
        print("✅ Successfully joined the channel")
    except Exception as e:
        print("❌ Failed to join the channel:", e)

async def main():
    await client.start()
    
    channel_link = "https://t.me/ShegerEventsHub"  
    await join_channel(client, channel_link)

with client:
    client.loop.run_until_complete(main())
