import os
from telethon import TelegramClient, events

# Replace hardcoded values with environment variables
API_ID = int(os.getenv('API_ID'))  # Set in Railway environment variables
API_HASH = os.getenv('API_HASH')  # Set in Railway environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Set in Railway environment variables
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Set your channel ID in Railway environment variables

# Dictionary of text and links
text_links = {
    'captain': 'https://www.google.com',
    'captain2': 'https://www.facebook.com',
    'captain3': 'https://www.flipkart.com'
}

# Initialize the client
client = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(chats=CHANNEL_ID))
async def add_links(event):
    message_text = event.message.message
    for text, link in text_links.items():
        if message_text == text:
            new_message_text = f"{text}\n{link}"
            await event.edit(new_message_text, parse_mode=None)  # Removed 'html' parse mode
            break

# Start the bot
with client:
    client.run_until_disconnected()
