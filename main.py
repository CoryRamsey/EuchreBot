import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=intents)
token = os.environ.get('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def start_game(ctx):

    await ctx.send("Starting a new Euchre game!")


bot.run(token)

