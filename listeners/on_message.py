import os
import re
import json
import random
import discord

from datetime import datetime
from discord.ext import commands
from misc import banished_words_private
from utils.discordbot import Bot
from utils.files import files
from utils.semifunc import SemiFunc

class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        afk = files.get_filepath("afk", "json")
        banished = files._banished()['banished_words']
        banished_ignore = files._banished()['banishedWordsBypasses']
        msg_content_lower = msg.content.lower()


        # Boost message
        if msg.type == discord.MessageType.premium_guild_subscription:
            print(msg)
            boosts_channel = msg.guild.get_channel( SemiFunc.get_channel_id(msg, "boosts") )
            total_boosts = re.sub(r'0-9:!', '', boosts_channel.topic)
            # total_boosts = str(total_boosts).replace("", )

            total_boosts = boosts_channel.topic.replace("Boost messages Total boosts ", "")
            print(total_boosts)
            boosts = msg.guild.premium_subscription_count

            if total_boosts == boosts:
                total_boosts = total_boosts + 1
            # boosts_channel.edit(topic=f"Thanks for the boost! Current boosts: 16 Total boosts: 16{boosts})")
            await boosts_channel.send(f"Thanks for boosting our server {msg.mention}!\nWe now have {boosts}.. or {total_boosts}, we didn't test this yet.")

            return


        if msg.author.bot:
            return
        
        # AFK Message
        if not msg.content.startswith("?"):

            if os.path.exists(afk):
                with open(afk, "r", encoding="utf8") as file:
                    data = json.load(file)

                users = data['users']

                if data['users']:
                    for i, entry in enumerate(users):
                        if entry['user_id'] == msg.author.id:
                            users.pop(i)

                            with open(afk, "w", encoding="utf8") as file:
                                json.dump(data, file, indent=4, ensure_ascii=False)

                            await msg.author.edit(nick=entry['name'], reason="They are baack")
                            await msg.channel.send(content=f"Welcome back {msg.author.mention}, I removed your AFK status.", delete_after=5)

        
        if len(msg.mentions) > 0:
            for mention in msg.mentions:
                with open(afk, 'r+', encoding='utf8') as file:
                    data = json.load(file)
                    users = data['users']
                    for entry in users:
                        if str(mention.id) == str(entry['user_id']):
                            afk_time = datetime.strptime(entry['since'], "%d/%m/%Y %H:%M")
                            now_time = datetime.now()
                            afk_dur = now_time - afk_time

                            seconds = int(afk_dur.total_seconds())

                            hours, minutes, secondsB = seconds // 3600, (seconds % 3600) // 60, seconds & 60

                            hours_text = "hour"
                            minutes_text = "minute"
                            if minutes > 1 or minutes == 0:
                                minutes_text = "minutes"
                            if hours > 1 or hours == 0:
                                hours_text = "hours"
                                
                            await msg.reply(f"`{entry['name']}` is AFK: {entry['msg']}\nBeen AFK for {hours} {hours_text} {minutes} {minutes_text}")
            
        # OwO reaction
        if msg.content.lower() == "owo" or msg.content.lower().find("fox_owo") >= 0:
            # Do not owo react in audits
            if msg.channel.id != SemiFunc.get_channel_id(msg, "audit"):
                owoId = files.get_emoji_ids(msg)['owo']
                owo = await msg.guild.fetch_emoji(owoId)
                await msg.add_reaction(owo)
                    
            
        # Cute Denier
        if msg_content_lower.find("not cute") >= 0 or msg_content_lower.find("nawt cute") >= 0:
            if random.randint(1, 100) > 70:
                await msg.reply("Cute denier detected! They are undeniably cute.")


        # Lastly: Banish
        canBanish = True
            
        # 1 - If a user is menitioned, and their userid has "67" in it, ignore
        if len(msg.mentions) > 0:
            for mention in msg.mentions:
                if str(mention.id).find("67") >= 0:
                    canBanish = False

        # 2 - If in counting and the message has 67 in it, ignore
        if msg.channel.id == 1419042219842736299 and msg_content_lower == "67":
            self.bot.logger.info(msg="We need them to count ffs!")
            canBanish = False

        if canBanish and SemiFunc.is_staff(msg.author) == False:
            content_lower_final = re.sub(r'[(#@-_\\/^,.)]', '', msg_content_lower).replace(" ", "")
            
            for banished_thing in banished:
                shouldBanish = True

                # 3 - If banished_thing in banished_ignore, do not banish
                for ignore in banished_ignore:
                    if content_lower_final.find(ignore) >= 0:
                        shouldBanish = False
                        # self.bot.logger.info(msg=f"Don't banish '{msg_content_lower}' sent by {msg.author.name}")
                    
                if shouldBanish:
                    if msg_content_lower.find(banished_thing) >= 0:
                        await SemiFunc.moderate_user(self.bot, msg, msg.author, "message_banished", [banished[banished_thing], banished_thing])
                        await msg.delete()
                
            # Last now - Private banish word list
            for banished_thing in banished_words_private.private_banished():
                if msg_content_lower.find(banished_thing) >= 0:
                    await SemiFunc.moderate_user(self.bot, msg, msg.author, "message_banished", [banished[banished_thing], banished_thing])
                    await msg.delete()

        # Banish Snowy Paws
        if msg.author.id == 888072934114074624 or msg.author.id == 1257541858809217035 or msg.author.id == 1094359688541372457 or msg.author.id == 1403877222959419423:
            pawMsg = "You've been banished from using snowy's paws."
            if msg.author.id == 888072934114074624:
                pawMsg = "You've been banished from using your paws."

            # First snowy, and only snowy for now
            if msg_content_lower.find("<:snowypawbs:1468047084664918278>") >= 0:
                await msg.reply(pawMsg)
                await msg.delete()
            if len(msg.stickers):
                for sticker in msg.stickers:
                    if sticker.name == "Snowy Pawbs" or sticker.name == "Snowy Pawbs Real":
                        await msg.reply(pawMsg)
                        await msg.delete()


async def setup(bot):
    await bot.add_cog(OnMessage(bot))
