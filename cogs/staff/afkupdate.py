import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class afkupdate(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="afkupdate", description="Update your AFK status!")
    async def afkupdate(self, ctx: Context, *, message: str = "Gone Fishin'", return_message: bool = True):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        if SemiFunc.can_afk__isalreadytrue(ctx):
            await SemiFunc.update_afk(ctx, message, return_message)
            await ctx.reply(content=f"I've updated your afk status to `{message}`", ephemeral=True)
        else:
            await ctx.reply("Cannot set your status to AFK, as you didn't use ?afk.")

async def setup(bot):
    await bot.add_cog(afkupdate(bot))
