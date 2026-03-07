import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class giverole(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="giverole", description="Give a role to a certain user")
    async def giverole(self, ctx: Context, user: discord.Member = None, role: discord.Role = None):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_owner(ctx.author):
            await ctx.reply("That command is owners only.")
            return
        
        if role:
            if user.get_role(role.id):
                await ctx.reply(f"They already have the `{role.name}` role.")
            else:
                await user.add_roles(role)
                await ctx.reply(f"Gave {user.name} the `{role.name}` role!")
        else:
            await ctx.reply("Usage: ?giverole @role")

async def setup(bot):
    await bot.add_cog(giverole(bot))
