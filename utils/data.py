import discord
import random
import os
import re
import datetime

from utils import permissions, default
from utils.default import CustomContext
from utils.config import Config
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand

from misc import banished_words_private
from utils.semifunc import SemiFunc
from utils.serverinfo import ServerInfo

class DiscordBot(AutoShardedBot):
    def __init__(self, config: Config, prefix: list[str] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.config = config
        self.create_embed = self.create_embed


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
            content_lower_final = re.sub(r'[(#@-_\\/^,.)]', '', content_lower).replace(" ", "")
            
            banished = SemiFunc.get_banished()
            banishedIgnore = banished["banishedWordsBypasses"]

            # Cute denier
            if "not cute" in content_lower or "nawt cute" in content_lower:
                if random.randint(1, 100) > 80:
                    await msg.reply("Cute denier detected! They are undeniably cute.")

            # TEMP
            if msg.guild.id == 1438414082448425111:
                if permissions.can_run_staff_cmd(msg.author) == False:
                    ## You don't work.. decoding error.
                    # for replacement in banished["replacments"]:
                    #     if content_lower_final.find(replacement):
                    #         content_lower_final.replace(replacement, banished[replacement])

                    for banished_thing in banished["banished_words"]:
                        if content_lower_final.find(banished_thing) >= 0:
                            print(content_lower_final)
                            if content_lower_final in banishedIgnore:
                                print(f"Don't banish '{content_lower}' sent by {msg.author.name}")
                            else:
                                if msg.channel.id == 1419042219842736299 and content_lower_final == "67":
                                    print("We need them to count ffs!")
                                else:
                                    embed = self.create_embed("Banished Words", "Placeholder", discord.Color.red())
                                    
                                    await SemiFunc.banish_word(embed, msg, ctx, msg.content, banished_thing, banished["banished_words"][banished_thing])
                    ## Private
                    for banished_thing in banished_words_private.private_banished():
                        if content_lower_final.find(banished_thing) >= 0:
                            if content_lower_final in banishedIgnore:
                                print(f"Don't banish '{content_lower}' sent by {msg.author.name}")
                            else:
                                embed = self.create_embed("Banished Words", "Placeholder", discord.Color.red())
                                
                                await SemiFunc.banish_word(embed, msg, ctx, msg.content, banished_thing, banished["banished_words"][banished_thing])

                # Banish users from things
                if msg.author.id == 888072934114074624 or msg.author.id == 1257541858809217035 or msg.author.id == 1094359688541372457 or msg.author.id == 1403877222959419423:
                    pawMsg = "You've been banished from using snowy's paws."
                    if msg.author.id == 888072934114074624:
                        pawMsg = "You've been banished from using your paws."


                    # First snowy. and only snowy for now
                    if content_lower.find("<:snowypawbs:1468047084664918278>") == 0:
                        await msg.reply(pawMsg)
                        await msg.delete()
                    if msg.stickers:
                        if msg.stickers[0]:
                                
                            if msg.stickers[0].name == "Snowy Pawbs" or msg.stickers[0].name == "Snowy Pawbs Real":
                                await msg.reply(pawMsg)
                                await msg.delete()

    async def on_member_join(self, member):
        test_or_main = ServerInfo.main_or_test_server(ServerInfo, member)

        roleId = 1477496210414768243
        channelId = ServerInfo.channels[test_or_main]["audit"]
        banishUserIds = SemiFunc.get_banished()["banished_ids"]

        # Test Server
        if member.guild.id == 1438414082448425111:
            roleId = 1477575309476761672
            channelId = 1473069052128661545

        if member.id in banishUserIds:
            role = member.guild.get_role(roleId)
            channel = member.guild.get_channel(channelId)
            
            embed = self.create_embed(
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
