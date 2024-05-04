import os
import discord

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Channel ID to send notifications
CHANNEL_ID = int(os.environ['CHANNEL_ID'])

VOICE_CHANNEL_ID = int(os.environ['VOICE_CHANNEL_ID'])


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")

@bot.event
async def on_voice_state_update(member, before, after):
    # Check if the member joins a specific voice channel
    if not before.channel and after.channel and after.channel.id == VOICE_CHANNEL_ID:
        # Get the text channel by ID
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            # Send a notification message
            await channel.send(f"{member.mention} has joined voice channel: "+ after.channel.name)

# Run Bot with Token
bot.run(os.environ['BOT_TOKEN'])