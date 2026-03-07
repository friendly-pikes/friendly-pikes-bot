import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class unmute(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="unmute", description="Unmute a user!")
    async def unmute(self, ctx: Context, user: discord.Member = None, *, reason: str = "No reason provided."):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        if user:
            if SemiFunc.is_staff(user):
                await ctx.reply(f"Cannot mute a staff member")
            else:
                duration = timedelta(seconds=0)
                await SemiFunc.moderate_user(self.bot, ctx, user, "unmute", [reason])
                await user.timeout(duration, reason=f'{reason} (Timed out by {ctx.author.name})')
                await ctx.reply(f"Sucessfully unmuted {user.mention} for '{reason}'")
                # /mute user:@snow2code limit: reason:
        else:
            await ctx.reply("Usage: ?unmute @user long reason")

async def setup(bot):
    await bot.add_cog(unmute(bot))
