import asyncio
import discord
import random
import datetime
import logging

from utils.files.json import get_json_file
from utils.default import CustomContext
from utils.serverinfo import ServerInfo


def get_inator_text(inator_type: str):
    inator_type = inator_type.lower()
    inator_text = f"{inator_type}inator"

    return inator_text

def color(content, is_time: bool=False):
    clr = "\033[02m"
    if content == "debug":
        clr = "\x1b[40;1m"
    elif content == "info":
        clr = "\x1b[34;1m"
    elif content == "warning":
        clr = "\x1b[33;1m"
    elif content == "error":
        clr = "\x1b[31m"
    elif content == "critical":
        clr = "\x1b[41m"
        
    if is_time:
        clr = "\x1b[30;1m"
        
    return f"{clr}{content}"
    
class SemiFunc():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    server_ids = ServerInfo.server_ids


    # def info(level: str):
    #     now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #     if not level.lower() in ["info", "warn", "error"]:
    #         level = "info"

    #     for i in range(1, 99):
    #         if i < 10:
    #             print(f"\033[0{i}m{level}   {i}")
    #         else:
    #             print(f"\033[{i}m{level}    {i}")

    #     print(f"{color(now, True)} {color(level.upper())}\x1b[0     ")
    #         # 2026-03-05 06:11:08 INFO     discord.gateway Shard ID 0 has connected to Gateway (Session ID: 474aa28818a4f1f10ab66089ecda1dd9).


    def mention_snowy():
        return "<@888072934114074624>"

    def main_or_test_server(ctx: CustomContext):
        return ServerInfo.main_or_test_server(ServerInfo, ctx)
    
    def get_channel(ctx: CustomContext, channel_name: str):
        main_or_test = SemiFunc.main_or_test_server(ctx)
        config = SemiFunc.get_config_entry("channel_ids")[main_or_test][channel_name]

        return config
    
    def get_role(ctx: CustomContext, role_name: str):
        main_or_test = SemiFunc.main_or_test_server(ctx)
        config = SemiFunc.get_config_entry("role_ids")[main_or_test][role_name]

        return config
    
    def get_roles(ctx: CustomContext):
        main_or_test = SemiFunc.main_or_test_server(ctx)
        config = SemiFunc.get_config_entry("role_ids")[main_or_test]

        return config
    
    def log_command_use(bot, author: discord.User, message_content, interaction: discord.Interaction):
        if SemiFunc.get_config_entry("ouput_on_command_used"):
            if interaction == None:
                bot.logger.info(msg=f"{author}: {message_content}")
            else:
                content = f"/{interaction.command.name}"
                
                for option in interaction.data["options"]:
                    content = f"{content} {option['value']}"
                bot.logger.info(msg=f"{interaction.user.name}: {content}")

    ## JSON files
    def get_banished():
        return get_json_file("banished")
    
    def get_radar_forced_ignore():
        return get_json_file("radar_forced_ignore")

    def get_config():
        return get_json_file("config")

    def get_config_entry(entry: str):
        json = SemiFunc.get_config()

        return json[entry]
    

    def audit_embed(audit_type: str, args: []):
        embed = discord.Embed()
        
        if len(args):
            ## For messages, we add the user's pfp and name as smth, i dunno
            if "message_" in audit_type:
                user: discord.User = args[0]
                channel_id: int = args[1].id
                color = discord.Color.dark_embed()

                message: discord.Message = args[2]

                if audit_type == "message_deleted":

                    embed.description = f"**Message sent by <@{user.id}> was deleted in <#{channel_id}>**"
                    
                    if len(message.attachments) > 0:
                        content = ""

                        for attachment in message.attachments:
                            content = content + f"{attachment.url}\n"

                        if message.content == "" or message.content == None:
                            embed.add_field(name="Content:", value=f"```Attachments:\n{content}```", inline=False)
                        else:
                            embed.add_field(name="Content:", value=f"```{message.content}\n\nAttachments:\n{content}```", inline=False)
                    else:
                        embed.add_field(name="Content:", value=f"```{message.content}```", inline=False)
                    
                    color = discord.Color.red()
                if audit_type == "message_edited":
                    before: discord.Message = args[2]
                    after: discord.Message = args[3]

                    embed.description = f"**Message sent by <@{user.id}> was edited in <#{channel_id}>**"
                    embed.add_field(name="before:", value=f"```{before.content}```", inline=False)
                    embed.add_field(name="after:", value=f"```{after.content}```", inline=False)
                    color = discord.Color.blue()

                embed.color = color

                embed.set_author(name=user.name, icon_url=user.avatar)
                embed.set_footer(text=f"User ID: {message.author.id} • Bot developed by snow2code")
                embed.timestamp = datetime.datetime.utcnow()

        return embed
    
    async def banish_word(bot, msg: discord.Message, ctx, content, banished_word, banish_message):
        embed = discord.Embed()
        try:
            bot.logger.info(msg=f"banish '{content}' sent by {ctx.author.name}")

            auditChannel = msg.guild.get_channel(SemiFunc.get_channel(ctx, "audit"))
            
            description = f"**Message sent by {ctx.author.mention} in {ctx.channel.mention} was banished**"
            description = f"{description}\n\nMessage: {msg.content}"
            description = f"{description}\nDetected banished word: {banished_word}"
            description = f"{description}\nMessage ID: {msg.id}"

            await msg.reply(banish_message)
            await msg.delete()

            # Send a message to banish to let staff know that message was banished
            if auditChannel:
                embed.description = description

                await auditChannel.send(embed=embed)
            else:
                bot.logger.warn(f"Cannot find audit channel!\n{description}")

        except Exception as e:
            # msg.channel.send
            await msg.reply(f"A error occured while banishing this message\n{SemiFunc.mention_snowy()}\n```{e}```")

    async def pikes_radar(bot, user: discord.Member, radar: str):
        radar_forced_ignore = SemiFunc.get_radar_forced_ignore()
        percent = random.randint(1, 100)
        embed = discord.Embed()
        embed.color = discord.Color.pink()
        embed.set_footer(text="Bot developed by snow2code")

        if percent == 67:
            if random.randint(1, 2) == 1:
                percent = percent - 1
            else:
                percent = percent + 2

        if user.id in radar_forced_ignore["ignore"][radar]:
            percent = 0
        
        if user.id in radar_forced_ignore["forced"][radar]:
            percent = 101

        emoji = "🎀"

        if radar == "gay":
            emoji = "🏳️‍🌈"
        # elif radar == "bi":
        #     emoji = "❤️💜💙"

        embed.title = f"{emoji} {radar.capitalize()} Radar {emoji}"
        embed.description = f"{user.mention} is {percent}% {radar}! {emoji}"
        embed.color = discord.Color.pink()
        
        if radar == "cute" and percent >= 80:
            embed.description = f"{embed.description}\n{user.global_name} is totally cute!"
        elif radar == "gay" and percent >= 50:
            embed.description = f"{embed.description}\n{user.global_name} is totally gay!"


        return embed

    async def pikes_inator(bot, ctx: CustomContext, user: discord.Member, inator_type:str, do_what: str):
        role_ids = SemiFunc.get_roles(ctx)
        vanity_role_sep = SemiFunc.get_role(ctx, "vanity")
        role = SemiFunc.get_role(ctx, inator_type)
        inator_text = get_inator_text(inator_type)

        embed = discord.Embed()

        if user.bot:
            await ctx.reply(f"I don't think {user.mention} has invoked or has been released from the {inator_text}")
        else:
        
            if do_what == "remove":
                try:
                    if inator_type == "explode":
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They unexploded")
                        await ctx.reply(f"{user.mention} has unexploded.. how.")
                    else:
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They've been released from the {inator_text}")
                        await ctx.reply(f"{user.mention} has been released from the {inator_text}!")
                except Exception as e:
                    await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")
            else:
                try:
                    if user.get_role(role) == None:
                        if inator_type == "explode":
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They exploded")
                            await ctx.reply("https://tenor.com/view/cat-explosion-sad-explode-gif-15295996165959499721")
                        else:
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They invoked the {inator_text}")
                            await ctx.reply(f"{user.mention} has invoked of the wrath of the {inator_text}!")
                    else:
                        await ctx.send(f"{user.mention} has already invoked of the wrath of the {inator_text}. They can't invoke the {inator_text} again.")
                except Exception as e:
                    bot.logger.info(msg=f"Error with pikes_inator\n{e}")
                    await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")
                
            await asyncio.sleep(1)


            ## If user doesn't have any vanity roles, remove the seperator
            if user.get_role(role_ids["cute"]) == None and user.get_role(role_ids["smol"]) == None and user.get_role(role_ids["explode"]) == None and user.get_role(role_ids["tall"]) == None:
                # safe guard cuz I'm just now adding vanity seperator to the code
                if user.get_role(vanity_role_sep):
                    await user.remove_roles(ctx.guild.get_role(vanity_role_sep), reason="No longer needs the seperator")
            else:
                await user.add_roles(ctx.guild.get_role(vanity_role_sep), reason="They need the seperator")