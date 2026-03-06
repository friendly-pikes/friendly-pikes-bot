import discord
import os
import datetime
import logging
import logging.handlers

from utils import permissions, default
from utils.default import CustomContext
from discord import app_commands
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand

from misc import banished_words_private
from utils.semifunc import SemiFunc

class DiscordBot(AutoShardedBot):
    def __init__(self, prefix: list[str] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.tree = app_commands.CommandTree(self)
        # self.tree.sync(self.guilds)
        self.prefix = prefix
        logger = logging.getLogger('discord')
        logger.setLevel(logging.INFO)

        handler = logging.handlers.RotatingFileHandler(
            filename=f"./logs/{datetime.datetime.now().strftime('%d-%m-%Y %H-%M')}.log",
            encoding='utf-8',
            maxBytes=32 * 1024 * 1024,  # 32 MiB
            backupCount=5,  # Rotate through 5 files
        )
        
        dt_fmt = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        self.logger = logger


    async def setup_hook(self):
        ## Load events
        for file in os.listdir("events"):
            if not file.endswith(".py"):
                continue  # Skip non-python files

            name = file[:-3]
            await self.load_extension(f"events.{name}")

        ## Load command cogs
        for file in os.listdir("cogs"):
            if not file.endswith(".py"):
                continue  # Skip non-python files

            name = file[:-3]
            await self.load_extension(f"cogs.{name}")

    def create_embed(self, title, description, color):
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        embed.set_footer(text="Bot developed by snow2code")

        if title == "Banished Words":
            embed.timestamp = datetime.datetime.utcnow()

        return embed
    
    def create_embed_empty(self):
        embed = discord.Embed()

        embed.set_footer(text="Bot developed by snow2code")

        return embed

    async def on_member_join(self, member):
        test_or_main = SemiFunc.main_or_test_server(member)

        roleId = SemiFunc.get_role(member, "banished")
        channelId = SemiFunc.get_channel(member, "audit")
        banishUserIds = SemiFunc.get_banished()["banished_ids"]

        if member.id in banishUserIds:
            role = member.guild.get_role(roleId)
            channel = member.guild.get_channel(channelId)
            
            embed = self.create_embed(
                "Dammy Files Banisher",
                f"User {member.display_name} ({member.name}) was banished. Reason being they are in the Dammy Files.\n\nUser Info:\nUser - {member.name}\nUserID - {member.id}",
                discord.Color.pink()
            )

            await member.add_roles(role)
            await channel.send(embed=embed)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=default.CustomContext)
        await self.invoke(ctx)


class HelpFormat(DefaultHelpCommand):
    def get_destination(self, no_pm: bool = False):
        if no_pm:
            return self.context.channel
        else:
            return self.context.author

    async def send_error_message(self, error: str) -> None:
        """ Sends an error message to the destination. """
        destination = self.get_destination(no_pm=True)
        await destination.send(error)

    async def send_command_help(self, command) -> None:
        """ Sends the help for a single command. """
        self.add_command_formatting(command)
        self.paginator.close_page()
        await self.send_pages(no_pm=True)

    async def send_pages(self, no_pm: bool = False) -> None:
        """ Sends the help pages to the destination. """
        try:
            if permissions.can_handle(self.context, "add_reactions"):
                await self.context.message.add_reaction(chr(0x2709))
        except discord.Forbidden:
            pass

        try:
            destination = self.get_destination(no_pm=no_pm)
            for page in self.paginator.pages:
                await destination.send(page)
        except discord.Forbidden:
            destination = self.get_destination(no_pm=True)
            await destination.send("Couldn't send help to you due to blocked DMs...")
