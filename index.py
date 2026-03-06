import discord
import os

from dotenv import load_dotenv
from utils.semifunc import SemiFunc
from utils import data
load_dotenv()

token = os.getenv('DISCORD_TOKEN')
config = SemiFunc.get_config()

bot = data.DiscordBot(
    command_prefix=config["prefix"],
    prefix=config["prefix"], command_attrs=dict(hidden=True),
    help_command=data.HelpFormat(),
    allowed_mentions=discord.AllowedMentions(
        everyone=False, roles=False, users=True
    ),
    intents=discord.Intents(
        # kwargs found at https://docs.pycord.dev/en/master/api.html?highlight=discord%20intents#discord.Intents
        guilds=True, members=True, messages=True, reactions=True,
        presences=True, message_content=True,
    )
)

try:
    bot.run(token)
except Exception as e:
    bot.logger.error(f"Error when logging in: {e}")
