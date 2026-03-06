import discord

from discord.ext import commands
from utils.data import DiscordBot
from utils.semifunc import SemiFunc

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.logger.info(msg=f"")
        self.bot.logger.info(msg=f"Logged in as {self.bot.user.name}")
        await self.bot.change_presence(status=discord.Status.invisible)


async def setup(bot):
    await bot.add_cog(OnReady(bot))
