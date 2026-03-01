import discord
import random

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.data import permissions

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.command()
    async def cutedar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            percent = random.randint(1, 100)

            # Pixie / Pixel Vortex / Victor is 0% cute!
            if user.id == 1262124659814695005:
                percent = 0

            if percent == 67:
                if random.randomint(1, 2) == 1:
                    percent = percent - 1
                else:
                    percent = percent + 2

            embed = DiscordBot.create_embed(self.bot, "🎀 Cute Radar 🎀", f"{user.mention} is {percent}% cute! 🎀", discord.Color.pink())

            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use cutedar on noone!\nUsage: ?cutedar @user")

async def setup(bot):
    await bot.add_cog(Users(bot))
