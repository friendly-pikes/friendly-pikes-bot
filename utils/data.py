import discord
import os

from utils import permissions, default
from utils.config import Config
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand


banishUserIds = [
    1403877222959419423, # Test
    # 825309596784001024 # FreddyCR  (just in case..)
    495293024394543124, # FoxyOwo
    626154564202266636, # Dammy
    1070256519897161749, # Danny
    1262934126844182633, # Rubicon
    400045916762931203 # Archie
]


class DiscordBot(AutoShardedBot):
    def __init__(self, config: Config, prefix: list[str] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.config = config

    def create_embed(self, title, description, color):
        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        embed.set_footer(text="Bot developed by snow2code")

        return embed
    
    """When the bot connects"""
    async def on_connect(self):
        # You gotta be hidden!
        await self.change_presence(status=discord.Status.invisible)

    """When the bot is ready"""
    async def on_ready(self):
        print(f"\nLogged in as {self.user.name}")
        await self.change_presence(status=discord.Status.invisible)

    async def setup_hook(self):
        for file in os.listdir("cogs"):
            if not file.endswith(".py"):
                continue  # Skip non-python files

            name = file[:-3]
            await self.load_extension(f"cogs.{name}")

    async def on_message(self, msg: discord.Message):
        if not self.is_ready() or msg.author.bot or \
           not permissions.can_handle(msg, "send_messages"):
            return

        await self.process_commands(msg)

    async def on_member_join(self, member):
        roleId = 1477496210414768243
        channelId = 1418951533688655989

        # Test
        if member.guild.id == 1438414082448425111:
            roleId = 1477575309476761672
            channelId = 1473069052128661545

        if member.id in banishUserIds:
            role = member.guild.get_role(roleId)
            channel = member.guild.get_channel(channelId)
            
            embed = DiscordBot.create_embed(
                self,
                "Dammy Files Banisher",
                f"User {member.global_name} was banished. Reason being they are in the Dammy Files.\n\nUser Info:\nUser - {member.global_name}\nUserID - {member.id}",
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
