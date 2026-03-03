import discord
import random
import os
import re
import datetime

from utils import permissions, default
from utils.default import CustomContext
from utils.config import Config
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand

banishUserIds = [
    1403877222959419423, # Test
    495293024394543124, # FoxyOwo
    626154564202266636, # Dammy
    1070256519897161749, # Danny
    1448150720712015912 # Milo

    ## These are innonent plp
    # 825309596784001024 # FreddyCR
    # 400045916762931203 # Archie
    # 1262934126844182633 # Rubicon
    # 264581569094615040, # Mathew
]

class ServerInfo():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def main_or_test_server(self, ctx: CustomContext):
        if ctx.guild.id == self.server_ids["test"]:
            return "test"
        return "main"
    
    server_ids = {
        "main": 1414222707570118656,
        "test": 1438414082448425111
    }
    
    channels = {
        "main": {
            "staff_commands": 1477520001165430938,
            "audit": 1477498994082185350,
        },
        "test": {
            "staff_commands": 1478352488301072477,
            "audit": 1478387549662875689
        }
    }

    role_ids = {
        "seperators": {
            "main": {
                "vanity": 1477780961935491226
            },
            "test": {
                "vanity": 1478032301685211298
            }
        },
        "roles": {
            "main": {
                "cute": 1477781229599199434,
                "shortie": 1477781226910912563,
                "smol": 1477781211622539326,
                "explode": 1477803664407003340,
                "tall": 1478069476284039180
            },
            "test": {
                "cute": 1477749083404767364,
                "shortie": 1477749159997214863,
                "smol": 1477749196366020780,
                "explode": 1478033086196482241,
                "tall": 1478069476284039180
            }
        },
    }

    ignore_radar_ids = {
        "cute": [
            1262124659814695005, # Victor / Pixie / Pivor or whatever
            1450968328821670040 # TKO
        ],
        "gay": [
            1000478105128947773, # 𝐳𝐦𝐢ę𝐤ł𝐲 𝐛𝐢𝐬𝐳𝐤𝐨𝐩
            1449593053492023467 # Kooddoger
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

    banishedWords = {
        "blayze": "We don't talk about him anymore.",

        # 67 banish
        "6or7": 'Do not say that "meme" number.',
        "sixhundredandseven": 'Do not say that "meme" number.',
        "sixtyseven": 'Do not say that "meme" number.',
        "67": 'Do not say that "meme" number.',

        "goon": "Please don't use that term.",

        "fetish": "Do not talk about anything of the sorts.",

        # Furry Wonderland banish
        
        "sneppy": "Please don't talk about Dammy / Sneppy.",
        "sneppyowo": "Please don't talk about Dammy / Sneppy.",
        "dammy": "Please don't talk about Dammy.",
        "dammyfiles": "Please don't talk about that.",
        "damianbednarski79": "Please don't talk about Dammy.",
        
        "foxyowo": "Please don't talk about FoxyOWO.",
        "danny": "Please don't talk abbout Danny.",

        ## [REDACTED] remove, as it's personal info


        "fw": "Please don't talk about Furry Wonderland.",
        "furrywonderland": "Please don't talk about Furry Wonderland.",
                # ## Ban talking about the dammy files
                # elif "dammy files" in content_lower:
                #     await msg.reply("Please don't talk about that.")
                #     await msg.delete()
    }

    # Allow these to be said
    banishedWordsBypasses = [
        ## Gifs and stuff
        "cdndiscordapp", # cdn.discord.app
        "tenorcom", # tenor.com
        "fwop"
    ]

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
            content_lower_final = re.sub(r'[-_\\/^,.]', '', content_lower).replace(" ", "")
            
            # Cute denier
            if "not cute" in content_lower or "nawt cute" in content_lower:
                if random.randint(1, 100) > 80:
                    await msg.reply("Cute denier detected! They are undeniably cute.")


            if permissions.can_run_staff_cmd(msg.author) == False:
                for banished_thing in self.banishedWords:
                    # print(banished_thing)
                    # print(content_lower.find(banished_thing))

                    if content_lower_final.find(banished_thing) >= 0:
                        if content_lower_final in self.banishedWordsBypasses:
                            print(f"Don't banish '{content_lower}' sent by {ctx.author.name}")
                        else:
                            try:
                                print(f"banish '{content_lower}' sent by {ctx.author.name}")
                                message = self.banishedWords[banished_thing]

                                await msg.reply(message)
                                await msg.delete()

                                # Send a message to banish to let staff know that message was banished
                                test_or_main = ServerInfo.main_or_test_server(ServerInfo, ctx)
                                auditChannel = msg.guild.get_channel(ServerInfo.channels[test_or_main]["audit"])

                                if auditChannel:
                                    des = f"**Message sent by {ctx.author.mention} in {ctx.channel.mention} was banished**"
                                    des = f"{des}\n\nMessage: {msg.content}"
                                    des = f"{des}\nDetected banished word: {banished_thing}"
                                    des = f"{des}\nMessage ID: {msg.id}"

                                    embed = self.create_embed("Banished Words", des, discord.Color.red())

                                    await auditChannel.send(embed=embed)
                                else:
                                    print(f"Cannot find audit channel!\n\n{des}")
                            except Exception as e:
                                await msg.channel.send("An error occurred, let <@888072934114074624> know!")
                                print(f"An error occurred\n{e}")
            
            # Banish users from things
            if msg.author.id == 888072934114074624 or msg.author.id == 1257541858809217035 or msg.author.id == 1094359688541372457 or msg.author.id == 1403877222959419423:
                # First snowy. and only snowy for now
                if content_lower.find("<:snowypawbs:1468047084664918278>") == 0:
                    await msg.reply("You've been banished from using your paws.")
                    await msg.delete()
                if msg.stickers:
                    if msg.stickers[0]:
                            
                        if msg.stickers[0].name == "Snowy Pawbs" or msg.stickers[0].name == "Snowy Pawbs Real":
                            messageB = "You've been banished from using your paws."

                            if msg.author.id == 1257541858809217035 or msg.author.id == 1094359688541372457:
                                messageB = "You've been banished from using snowy's paws."

                            await msg.reply(messageB)
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
            
            embed = self.create_embed(
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
