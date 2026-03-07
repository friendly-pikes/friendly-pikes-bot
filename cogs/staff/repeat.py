import re
import discord
import asyncio

import utils.files as files
from datetime import datetime, timedelta
from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class repeat(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

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
    await bot.add_cog(repeat(bot))
