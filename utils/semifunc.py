import json
import discord
import random
import asyncio
import utils.files as files
from utils.custom.context import Context
from datetime import datetime

def main_or_test(ctx: Context):
    config = files._config()
    if ctx.guild.id == config['server_ids']['main']:
        return "main"
    
    return "test"


class SemiFunc():
    def __init__(*args, **kargs):
        super().__init__(*args, **kargs)

    def create_embed(title: str = "", description: str = "", color: discord.Color = discord.Color.dark_embed()):
        return discord.Embed(
            title=title,
            description=description,
            color=color
        )

    def get_server_id(what):
        config = files._config()
        
        if config['server_ids'][what]:
            return config['server_ids'][what]
        
        return None
    
    def get_channel_id(ctx: Context, channelname: str):
        channelids = files.get_channel_ids(ctx)
        if channelids[channelname]:
            return channelids[channelname]
        return None
    
    def get_role_id(ctx: Context, rolename: str):
        roles = files.get_role_ids(ctx)

        if roles[rolename]:
            return roles[rolename]
        
        return None

    def is_owner(user: discord.Member):
        config = files._config()
        if user.id in config['owners']:
            return True
        return False

    def is_staff(user: discord.Member):
        role = SemiFunc.get_role_id(user, "staff")

        if user.get_role(role):
            return True
        
        return False
        # staff = SemiFunc.get_role_id(user, "staff")
        
        # if user.get_role(staff):
        #     return True
        
        # return False
    
    def can_afk__isalreadytrue(ctx: Context):
        afk = files.get_filepath("afk", "json")

        with open(afk, 'r', encoding='utf8') as file:
            data = json.load(file)

            afkSince_createdat = ctx.message.created_at.strftime("%d/%m/%Y %H:%M")
            canAfk = False
            for entry in data['users']:
                if entry['user_id'] == ctx.author.id:
                    canAfk = True
                    
            return canAfk
        
    def can_afk__isalready(ctx: Context):
        afk = files.get_filepath("afk", "json")

        with open(afk, 'r', encoding='utf8') as file:
            data = json.load(file)

            afkSince_createdat = ctx.message.created_at.strftime("%d/%m/%Y %H:%M")
            canAfk = True
            for entry in data['users']:
                if entry['user_id'] == ctx.author.id:
                    canAfk = False
                    
            return canAfk

    async def update_afk(ctx: Context, message: str, return_message):
        afk = files.get_filepath("afk", "json")

        with open(afk, "r", encoding="utf8") as file:
            data = json.load(file)

        afk_since = ctx.message.created_at.strftime("%d/%m/%Y %H:%M")

        for entry in data['users']:
            if entry['user_id'] == ctx.author.id:
                entry['msg'] = message
                break
                    
        with open(afk, "w", encoding="utf8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    async def add_afk(ctx: Context, message: str, return_message):
        afk = files.get_filepath("afk", "json")
        
        # for entry in afk:
            # if entry['user_id'] == ctx.author.id
            
        # await ctx.reply
        with open(afk, 'r+', encoding='utf8') as file:
            data = json.load(file)

            afkSince_createdat = ctx.message.created_at.strftime("%d/%m/%Y %H:%M")
            can_afk = SemiFunc.can_afk__isalready(ctx)
            
            data['users'].append({
                "name": ctx.author.display_name,
                "user_id": ctx.author.id,
                "return_message": return_message,
                "msg": message,
                "since": f"{afkSince_createdat}"
            })
                
            file.seek(0)

            json.dump(data, file, indent=4, ensure_ascii=False)

    async def moderate_user(bot, ctx: Context, user: discord.Member, moderation_type: str, args: []):
        moderation_embed = bot.create_embed()
        isGud = False

        
        if moderation_type == "kick":
            isGud = True
            moderation_embed.title = f"Staff at {files.get_server_name()}"
            moderation_embed.description = f"You've been kicked from {files.get_server_name()} by {ctx.author.name} ({ctx.author.display_name})"
            moderation_embed.description = moderation_embed.description + f"\n\nReason: {args[0]}\nPunisher: {ctx.author.name}\n\n\nServer Invite: https://discord.gg/X8QqpeYgGF"
        elif moderation_type == "ban":
            isGud = True
            moderation_embed.title = f"Staff at {files.get_server_name()}"
            moderation_embed.description = f"You've been banned from {files.get_server_name()} permanently by {ctx.author.name} ({ctx.author.display_name})"
            moderation_embed.description = moderation_embed.description + f"\n\nReason: {args[0]}\nPunisher: {ctx.author.name}\n\n\nServer Invite: https://discord.gg/X8QqpeYgGF"
        elif moderation_type == "mute":
            isGud = True
            moderation_embed.title = f"Staff at {files.get_server_name()}"
            moderation_embed.description = f"You've been muted in {files.get_server_name()} by {ctx.author.name} ({ctx.author.display_name})"
            moderation_embed.description = moderation_embed.description + f"\n\nReason: {args[0]}\nPunisher: {ctx.author.name}"
        elif moderation_type == "unmute":
            isGud = True
            moderation_embed.title = f"Staff at {files.get_server_name()}"
            moderation_embed.description = f"You've been unmuted in {files.get_server_name()} by {ctx.author.name} ({ctx.author.display_name})"
            moderation_embed.description = moderation_embed.description + f"\n\nReason: {args[0]}\nPunisher: {ctx.author.name}"
        elif moderation_type == "message_banished":
            audit = ctx.guild.get_channel(SemiFunc.get_channel_id(ctx, "audit"))

            # isGud = True
            moderation_embed.title = f"**Message sent by {ctx.author.mention} in {ctx.channel.mention} was banished**"
            moderation_embed.description = f"\n\nMessage: {ctx.content}\n"
            moderation_embed.description = f"Detected banished word: {args[1]}\n"
            moderation_embed.description = f"Message ID: {ctx.id}"
            moderation_embed.color = discord.Color.red()

            await ctx.reply(f"{args[0]}")
            await audit.send(embed=moderation_embed)

            return

        if isGud:
            await user.send(embed=moderation_embed)

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

    def get_inator_text(inator_type: str):
        inator_type = inator_type.lower()
        inator_text = f"{inator_type}inator"

        return inator_text

    async def pikesInator(bot, ctx: Context, user: discord.Member, inator_type:str, do_what: str):
        role_ids = files.get_role_ids(ctx)
        vanity_role_sep = SemiFunc.get_role_id(ctx, "vanity")
        role = SemiFunc.get_role_id(ctx, inator_type)
        inator_text = SemiFunc.get_inator_text(inator_type)

        embed = discord.Embed()

        if user.bot:
            await ctx.reply(f"I don't think {user.mention} has invoked or has been released from the {inator_text}")
        else:
            # Ignores
            if ctx.command:
                cmd = ctx.command.name.removeprefix("un")

                ignores = files.get_command_ignores()
                
                if ignores[cmd]:
                    if user.id in ignores[cmd]:
                        await ctx.reply(f"{user.mention} is not worthy of the {inator_text}.")
                        return
            else:
                print(f"interaction {ctx.interaction.command.name}")

            if do_what == "remove":
                if inator_type == "explode":
                    await user.remove_roles(ctx.guild.get_role(role), reason=f"They unexploded")
                    await ctx.reply(f"{user.mention} has unexploded.. how.")
                else:
                    await user.remove_roles(ctx.guild.get_role(role), reason=f"They've been released from the {inator_text}")
                    await ctx.reply(f"{user.mention} has been released from the {inator_text}!")
            else:
                if user.get_role(role) == None:
                    if inator_type == "explode":
                        await user.add_roles(ctx.guild.get_role(role), reason=f"They exploded")
                        await ctx.reply("https://tenor.com/view/cat-explosion-sad-explode-gif-15295996165959499721")
                    else:
                        await user.add_roles(ctx.guild.get_role(role), reason=f"They invoked the {inator_text}")
                        await ctx.reply(f"{user.mention} has invoked of the wrath of the {inator_text}!")
                else:
                    await ctx.send(f"{user.mention} has already invoked of the wrath of the {inator_text}. They can't invoke the {inator_text} again.")
                
            await asyncio.sleep(1)

            ## If user doesn't have any vanity roles, remove the seperator
            if user.get_role(role_ids["cute"]) == None and user.get_role(role_ids["smol"]) == None and user.get_role(role_ids["explode"]) == None and user.get_role(role_ids["tall"]) == None:
                # safe guard cuz I'm just now adding vanity seperator to the code
                if user.get_role(vanity_role_sep):
                    await user.remove_roles(ctx.guild.get_role(vanity_role_sep), reason="No longer needs the seperator")
            else:
                await user.add_roles(ctx.guild.get_role(vanity_role_sep), reason="They need the seperator")

    async def pikesRadar(bot, user: discord.Member, radar: str):
        forced_ignore = files._radar_ignore_force()
        percent = random.randint(1, 100)
        embed = SemiFunc.create_embed(color=discord.Color.pink())

        emoji = "🎀"
        if radar == "gay":
            emoji = "🏳️‍🌈"


        # Ban 67.
        if percent == 67:
            if random.randint(1, 2) == 1:
                # Use 66
                percent = percent - 1
            else:
                # Use 69
                percent = percent + 2

        # If in ignore radars, set the percent to 0
        if user.id in forced_ignore['ignore'][radar]:
            percent = 0

        # If in forced radars, set the percent to 101
        if user.id in forced_ignore['forced'][radar]:
            percent = 101


        embed.title = f"{emoji} {radar.capitalize()} Radar {emoji}"
        
        if radar == "rizz":
            embed.description = f"{user.mention} has {percent}% {radar}! {emoji}"
        else:
            embed.description = f"{user.mention} is {percent}% {radar}! {emoji}"

        embed.color = discord.Color.pink()
        
        if radar == "cute":
            if percent >= 50 and percent < 80:
                embed.description = f"{embed.description}\n{user.name} is totally cute!"
            elif percent >= 80:
                embed.description = f"{embed.description}\n{user.name} is **A D O R A B L E**!"
        elif radar == "silly":
            if percent >= 50 and percent < 80:
                embed.description = f"{embed.description}\n{user.name} is totally silly!"
            elif percent >= 80:
                embed.description = f"{embed.description}\n{user.name} is **T O O  S I L L Y**!"
        elif radar == "gay" and percent >= 50:
            embed.description = f"{embed.description}\n{user.name} is totally gay!"
        
        embed.set_footer(text="Bot developed by snow2code")

        return embed
    
    def command_disabled(ctx: Context):
        disabled = files._config()['disabled_commands']

        if ctx.interaction == None:
            if ctx.command.name in disabled:
                return True
        else:
            if ctx.interaction.command.name in disabled:
                return True

        return False
    
    def log_command_use(bot, author: discord.User, message_content, interaction: discord.Interaction):
        if files.get_config_entry("output_on_command_used_enabled"):
            if interaction == None:
                bot.logger.info(msg=f"{author}: {message_content}")
            else:
                content = f"/{interaction.command.name}"
                
                for option in interaction.data["options"]:
                    content = f"{content} {option['value']}"
                bot.logger.info(msg=f"{interaction.user.name}: {content}")
