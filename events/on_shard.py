import discord

from discord.ext import commands
from utils.data import DiscordBot

class OnShard(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.Cog.listener()
    async def on_shard_connect(self, shard_id):
        await self.bot.change_presence(status=discord.Status.invisible)

    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        await self.bot.change_presence(status=discord.Status.invisible)

async def setup(bot):
    await bot.add_cog(OnShard(bot))
