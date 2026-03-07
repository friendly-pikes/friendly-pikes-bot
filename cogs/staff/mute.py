import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc


def parase_duration(duration: str):
    match = re.match(r'^(\d+)([smhd])$', duration.lower())
    if not match:
        return None
    
    value = int(match.group(1))
    unit = match.group(2)

    multipliers = {
        "s": 1,
        "m": 60,
        "h": 3600,
        "d": 86400
    }

    return value * multipliers[unit]


class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="mute", description="Mute a user!")
    async def mute(self, ctx: Context, user: discord.Member = None, duration: str = "5m", *, reason: str = "No reason provided."):
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
                errors = [
                    
                ]

                if parase_duration(duration) > 2419200:
                    duration = 2419200
                    errors.append("Max duration exected! Max duration for a mute is 28 days.")
                
                if parase_duration(duration) < 0:
                    duration = parase_duration("5m")
                    errors.append("Duration is not a positive integer.")

                    
                duration = timedelta(seconds=parase_duration(duration))
                
                await SemiFunc.moderate_user(self.bot, ctx, user, "mute", [reason])
                await user.timeout(duration, reason=f'{reason} (Timed out by {ctx.author.name})')
                
                await ctx.reply(f"Sucessfully muted {user.mention} for '{reason}'")
                if len(errors) > 0:
                    await ctx.send(f"Errors:")
                    for error in errors:
                        await ctx.send(f"`{error}`")
                # /mute user:@snow2code limit: reason:
        else:
            await ctx.reply("Usage: ?mute @user length (e.g 5m, 1h, 1d) long reason")

async def setup(bot):
    await bot.add_cog(Staff(bot))
