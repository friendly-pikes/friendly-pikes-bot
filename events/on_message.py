import discord
import random
import re

from utils import permissions, default
from discord.ext import commands
from utils.data import DiscordBot

from misc import banished_words_private
from utils.semifunc import SemiFunc

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        
        if not self.bot.is_ready() or msg.author.bot or \
           not permissions.can_handle(msg, "send_messages"):
            return
        
        ctx = await self.bot.get_context(msg, cls=default.CustomContext)
        
        if ctx.valid:
            await self.bot.invoke(ctx)
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

            # TEMP SERVER CHECK
            # if msg.guild.id == 1438414082448425111:
            if permissions.can_run_staff_cmd(msg.author) == False:
                ## You don't work.. decoding error.
                # for replacement in banished["replacments"]:
                #     if content_lower_final.find(replacement):
                #         content_lower_final.replace(replacement, banished[replacement])
                
                for banished_thing in banished["banished_words"]:
                    shouldBanish = True
                    if content_lower_final.find(banished_thing) >= 0:
                        for ignore_banish in banishedIgnore:
                            if content_lower_final.find(ignore_banish) >= 0:
                                shouldBanish = False
                                self.bot.logger.info(msg=f"Don't banish '{content_lower}' sent by {msg.author.name}")
                        
                        # Let's not banish the message if the user mentioned someone, and their user id has "67" in it
                        if len(msg.raw_mentions) > 0:
                            for mention in msg.raw_mentions:
                                if str(mention).find("67"):
                                    shouldBanish = False

                        if shouldBanish:
                            if msg.channel.id == 1419042219842736299 and content_lower_final == "67":
                                self.bot.logger.info(msg="We need them to count ffs!")
                            else:
                                embed = self.bot.create_embed("Banished Words", "Placeholder", discord.Color.red())
                                
                                await SemiFunc.banish_word(self, msg, ctx, msg.content, banished_thing, banished["banished_words"][banished_thing])
                ## Private
                for banished_thing in banished_words_private.private_banished():
                    if content_lower_final.find(banished_thing) >= 0:
                        if content_lower_final in banishedIgnore:
                            self.bot.logger.info(msg=f"Don't banish '{content_lower}' sent by {msg.author.name}")
                        else:
                            embed = self.bot.create_embed("Banished Words", "Placeholder", discord.Color.red())
                            
                            await SemiFunc.banish_word(self, msg, ctx, msg.content, banished_thing, banished["banished_words"][banished_thing])


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

async def setup(bot):
    await bot.add_cog(OnMessage(bot))
