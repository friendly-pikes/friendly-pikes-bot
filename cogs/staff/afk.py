import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="afk", description="Set your AFK status!")
    async def afk(self, ctx: Context, *, message: str = "Gone Fishin'", return_message: bool = True):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        can_afk = SemiFunc.can_afk__isalready(ctx)

        if can_afk:
            await SemiFunc.add_afk(ctx, message, return_message)
            await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}", reason="They went AFK")
            await ctx.reply(content=f"I've updated your status to AFK with the message `{message}`", ephemeral=True)
        else:
            await ctx.reply(f'Cannot change your status to AFK, you are already "AFK"')

async def setup(bot):
    await bot.add_cog(afk(bot))
