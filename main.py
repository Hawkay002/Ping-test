import asyncio
from telethon import TelegramClient

# Telegram API credentials
api_id = 28203311
api_hash = '9694228796a1f8b181b877fbde5826e2'
phone_number = '+918777845713'  # your number

# Start the client
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)

# Target user
target = '@theprothug'  # username or ID

async def hightech_ping():
    # Simulate a high-tech ping sequence
    tech_messages = [
        "💻 Initializing ping protocol...",
        "🛰️ Connecting to target server...",
        "🔍 Scanning network routes...",
        "⚡ Sending data packets...",
        "📡 Ping in progress...",
        "✅ Target reached! Ping successful!"
    ]
    
    for msg in tech_messages:
        await client.send_message(target, f"`{msg}`")  # code-style formatting
        await asyncio.sleep(0.8)  # short delay for effect

# Run the async function
with client:
    client.loop.run_until_complete(hightech_ping())
