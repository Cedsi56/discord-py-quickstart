from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# If TOKEN is not set, then the .env isn't set up properly and thus we need to exit
if TOKEN == "":
    print("Please set the Discord bot token in the .env file")
    exit()


# The prefix can be of any length, but is usually one "special" character that people wouldn't type on accident
COMMAND_PREFIX = '?'

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
bot.remove_command('help')


@bot.event
async def on_ready():
    # Everything here will be loaded when the bot starts up
    print("The bot is up!")


@bot.command(name='bird')
async def bird(ctx):
    # Everything here will be loaded whenever the bot sees someone type ?bird
    message = "They are very cool!"
    await ctx.send(message)

# Start up the bot (you may want to handle this in a dedicated function if you're doing specific things)
bot.run(TOKEN)
