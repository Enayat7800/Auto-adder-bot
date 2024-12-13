from telethon import TelegramClient, events, sync
import re

# Replace with your actual values!
API_ID = 1234567  # Your API ID
API_HASH = 'your_api_hash'  # Your API HASH
BOT_TOKEN = 'your_bot_token'  # Your Bot Token
CHANNEL_ID = -1001234567890  # Your channel ID

# Dictionary of text and links
text_links = {
    'captain': 'https://www.google.com',
    'captain2': 'https://www.facebook.com',
    'captain3': 'https://www.flipkart.com'
}

# Initialize the client
client = TelegramClient('bot_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_ID))
async def add_links(event):
    message_text = event.message.message
    for text, link in text_links.items():
        if message_text == text:
            new_message_text = f"{text}\n{link}"
            await event.edit(new_message_text, parse_mode=None) # Removed 'html' parse mode
            break

# Start the bot
with client:
    client.run_until_disconnected()
