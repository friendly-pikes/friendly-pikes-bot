import discord
import logging
import logging.handlers

from datetime import datetime
from discord.ext import commands
from utils.data import DiscordBot

class OnConnect(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot
    
    @commands.Cog.listener()
    async def on_connect(self):
        await self.bot.change_presence(status=discord.Status.invisible)

        # This copies the global commands over to your guild.
        try:
            synced = await self.bot.tree.sync()
            self.bot.logger.info(msg=f"Synced {len(synced)} commands globally.")
        except Exception as e:
            self.bot.logger.error(msg=f"Error: {e}")
        # self.tree.copy_global_to()
        # await self.tree.sync(self.guilds)

async def setup(bot):
    await bot.add_cog(OnConnect(bot))
