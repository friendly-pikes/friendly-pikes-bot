import os
import dotenv
import discord
import utils.files as files

from utils.discordbot import Bot
dotenv.load_dotenv()

token = os.getenv('DISCORD_TOKEN')
config = files._config()

bot = Bot(
    command_prefix=config['prefix'],
    prefix=config['prefix'], command_attrs=dict(hidden=True),
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
