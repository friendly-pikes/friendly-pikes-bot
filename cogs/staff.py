import discord

import utils.files as files
from datetime import datetime
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="ban", description="Ban a user! (Diffrent from banish)")
    async def ban(self, ctx: Context, user: discord.Member = None):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        if user:
            if SemiFunc.is_staff(ctx.author):
                await ctx.reply(f"Cannot ban a staff member")
            else:
                reason = f"{datetime.now().strftime('%d/%m/%Y - %H:%M')} @{ctx.author.name} (Permanent): {reason}"
                await user.ban(delete_message_days=1, reason=reason)
        else:
            await ctx.reply("Usage: ?ban @user long reason (This'll remove their messages from the last day)")

    @commands.guild_only()
    @commands.hybrid_command(name="kick", description="Kick a user!")
    async def kick(self, ctx: Context, user: discord.Member = None):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        if user:
            if SemiFunc.is_staff(ctx.author):
                await ctx.reply(f"Cannot ban a staff member")
            else:
                reason = f"{datetime.now().strftime('%d/%m/%Y - %H:%M')} @{ctx.author.name}: {reason}"
                # await user.ban(delete_message_days=1, reason=reason)
        else:
            await ctx.reply("Usage: ?ban @user long reason (This'll remove their messages from the last day)")

    @commands.guild_only()
    @commands.hybrid_command(name="banish", description="Banish a user!")
    async def banish(self, ctx: Context, user: discord.Member = None):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        if user == None:
            await ctx.reply("Banish usage: ?banish @user OR use the app / slash command")
        else:
            if SemiFunc.is_staff(user):
                await ctx.reply("Cannot banish a staff member.")
            else:
                banishId, verifiedId = SemiFunc.get_role_id(ctx, "banished"), SemiFunc.get_role_id(ctx, "verified")
                banished, verified = ctx.guild.get_role(banishId), ctx.guild.get_role(verifiedId)

                if user.get_role(banishId):
                    await ctx.reply(f"Cannot banish {user.mention}, they are already banished.\nUnbanish them with `unbanish`")
                else:
                    await user.remove_roles(verified, reason=f"They've been banished by {ctx.author.name}")
                    await user.add_roles(banished, reason=f"They've been banished by {ctx.author.name}")
                    await ctx.reply(f"{user.mention} has been banished!")

    @commands.guild_only()
    @commands.hybrid_command(name="unbanish", description="Unbanish a user!")
    async def unbanish(self, ctx: Context, user: discord.Member = None):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        if user == None:
            await ctx.reply("Banish usage: ?banish @user OR use the app / slash command")
        else:
            if SemiFunc.is_staff(user):
                await ctx.reply("Cannot banish a staff member.")
            else:
                banishId, verifiedId = SemiFunc.get_role_id(ctx, "banished"), SemiFunc.get_role_id(ctx, "verified")
                banished, verified = ctx.guild.get_role(banishId), ctx.guild.get_role(verifiedId)

                if user.get_role(banishId):
                    await user.remove_roles(banished, reason=f"They've been unbanished by {ctx.author.name}")
                    await ctx.reply(f"{user.mention} has been unbanished!")
                else:
                    await ctx.reply(f"Cannot unbanish {user.mention}, they aren't banished.")

    @commands.guild_only()
    @commands.hybrid_command(name="afk", description="Set your AFK status!")
    async def afk(self, ctx: Context, *, message: str = "Gone Fishin'", return_message: bool = False):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        if ctx.author.id == files.get_owner_id():
            await SemiFunc.add_afk(ctx, message)

    @commands.guild_only()
    @commands.hybrid_command(name="reply", description="Send a message to whatever as a reply to a message!")
    async def reply(self, ctx: Context, channel: discord.TextChannel, message_id: str, *, message: str):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        if ctx.channel.id == SemiFunc.get_channel_id(ctx, "staff_commands"):
            message_id = int(message_id)
            msg_reply = await channel.fetch_message(message_id)
            if msg_reply:
                await msg_reply.reply(message)
                await ctx.reply("Sent message successfully!")
            else:
                await ctx.reply(f"Cannot find a message with the id '{message_id}' in {channel.mention}")

    @commands.guild_only()
    @commands.hybrid_command(name="repeat", description="Send a message to whatever channel!")
    async def repeat(self, ctx: Context, channel: discord.TextChannel, message: str):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return

        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        if ctx.channel.id == SemiFunc.get_channel_id(ctx, "staff_commands"):
            await ctx.send(message)
            await ctx.reply("Sent message successfully!")

async def setup(bot):
    await bot.add_cog(Staff(bot))
