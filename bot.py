import os
from telethon import TelegramClient, events

# Replace hardcoded values with environment variables
API_ID = int(os.getenv('API_ID'))  # Set in Railway environment variables
API_HASH = os.getenv('API_HASH')  # Set in Railway environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Set in Railway environment variables
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  # Set your channel ID in Railway environment variables

# Dictionary of text and links
text_links = {
    '51game': 'https://51gameappinin.com/#/register?invitationCode=83363102977',
    'bswin': 'https://bslotto.com/#/register?invitationCode=86787104955',
    '82bet': 'https://82bet.com/#/register?invitationCode=583873088657',
    'okwin': 'https://www.okwin.la/#/register?invitationCode=715142961253',
    'Deltin': 'http://deltin.bet/register?key=1000277575',
    'Raja luck': 'https://rajaluck.com/#/register?invitationCode=tleWe85176',
    'In99': 'https://in999.club/#/register?invitationCode=13587102403',
    'sonsy': 'https://www.sonsy1.in/#/register?invitationCode=58334104548',
    '1010game': 'https://1014game.in/#/register?invitationCode=372441180074',
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
