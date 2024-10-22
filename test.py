import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file
token = os.getenv("DISCORD_TOKEN")  # Get token from .env

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="MADWOLFOP , VSCODE"
        )
    )
    print(f"Logged in as {bot.user}")


bot.run(token)
