import os
import asyncio
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv() 

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("anon", api_id, api_hash)

async def main():
    await client.start()
    chat = '@kinfe123'
    messages = ["MoltBot, Testing, \nSurprise! Automation loves you 😎 \nEven if you get sick hearing the word AI"]
    repeat_count = 100
    delay = 0.2  
    delete_after = 50

    # collect all deletion tasks
    deletion_tasks = []

    for i in range(repeat_count):
        for msg in messages:
            sent_msg = await client.send_message(chat, msg)
            print(f"Message {i+1} sent ✌️")

            # schedule deletion+++++++++
            task = asyncio.create_task(delete_later(chat, sent_msg, delete_after))
            deletion_tasks.append(task)

            await asyncio.sleep(delay)

    # wait for all deletions to complete
    await asyncio.gather(*deletion_tasks)
    print("All messages sent and deleted!")

async def delete_later(chat, message, delay):
    await asyncio.sleep(delay)
    await client.delete_messages(chat, message, revoke=True)
    print(f"😒 Message deleted")

# run the main function
asyncio.run(main())

