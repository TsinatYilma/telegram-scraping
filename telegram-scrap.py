from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest


async def scrape():
    await client.start()
    channel = await client.get_entity(channel_username)

    offset_id = 0
    limit = 100  # messages per request
    all_messages = []

    while True:
        history = await client(GetHistoryRequest(
            peer=channel,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))

        if not history.messages:
            break

        for message in history.messages:
            all_messages.append(message)

        offset_id = history.messages[-1].id

    print(f"Scraped {len(all_messages)} messages")

with client:
    client.loop.run_until_complete(scrape())
