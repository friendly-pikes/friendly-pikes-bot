import discord
import random
import os

from utils import permissions, default
from utils.config import Config
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand


banishUserIds = [
    1403877222959419423, # Test
    495293024394543124, # FoxyOwo
    626154564202266636, # Dammy
    1070256519897161749, # Danny
    1262934126844182633 # Rubicon

    ## These are innonent plp
    # 825309596784001024 # FreddyCR
    # 400045916762931203 # Archie
]

class ServerInfo():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    server_ids = [
        #Main
        1414222707570118656,
        # Test
        1438414082448425111
    ]

    role_ids = {
        "seperators": {
            "vanity": 1477780961935491226
        },
        "roles": {
            "cute": 1477781229599199434,
            "shortie": 1477781226910912563,
            "smol": 1477781211622539326,
            "explode": 1477803664407003340,
            "tall": 1478069476284039180
        },

        "seperators_test": {
            "vanity": 1478032301685211298
        },
        "roles_test": {
            "cute": 1477749083404767364,
            "shortie": 1477749159997214863,
            "smol": 1477749196366020780,
            "explode": 1478033086196482241,
            "tall": 1478069476284039180
        }
    }

    ignore_radar_ids = {
        "cute": [
            1262124659814695005,
            1450968328821670040
        ],
        "gay": [
            1000478105128947773
        ]
    }

    forced_radar_ids = [
        1257541858809217035
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
    
    async def on_connect(self):
        # You gotta be hidden!
        await self.change_presence(status=discord.Status.invisible)

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
        
        ctx = await self.get_context(msg, cls=default.CustomContext)
        if ctx.valid:
            await self.invoke(ctx)
        else:
            ## Other stuff first, then ban stuff
            content_lower = msg.content.lower()

            # Cute denier
            if "not cute" in content_lower or "nawt cute" in content_lower:
                if random.randint(1, 100) == 100:
                    msg.reply("Cute denier detected! They are undeniably cute.")


            if permissions.can_run_staff_cmd(msg.author) == False:
                ## PETITION BAN 67!!
                if "67" in msg.content or "6-7" in msg.content \
                    or "six seven" in content_lower:

                    await msg.reply("Banished term detected.")
                    await msg.delete()
                
                ## Ban talking about the dammy files
                elif "dammy files" in content_lower:
                    await msg.reply("Please don't talk about that.")
                    await msg.delete()

        # await self.process_commands(msg)


        

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
