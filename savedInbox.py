import os
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def main():
    await client.start()
    await client.send_message('me', "Man this is amazing. i will not judge hackers from now on,/n cuz this feels amazing")
    print("✅ Message sent to Saved Messages")

with client:
    client.loop.run_until_complete(main())
