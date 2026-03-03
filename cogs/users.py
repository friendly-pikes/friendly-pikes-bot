import discord
import random

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.semifunc import SemiFunc

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot


    @commands.command()
    async def cutedar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "cute")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use cutedar on noone!\nUsage: ?cutedar @user")

    # These radar commands are stolen from pride bot
    # https://github.com/Pridebot-Systems/Pridebot/blob/main/src/commands/fun/
    @commands.command()
    async def bidar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "bi")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use bidar on noone!\nUsage: ?bidar @user")

    @commands.command()
    async def gaydar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "gay")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use gaydar on noone!\nUsage: ?gaydar @user")

    @commands.command()
    async def queerdar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "queer")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use queerdar on noone!\nUsage: ?queerdar @user")

    @commands.command()
    async def rizzdar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "rizz")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use rizzdar on noone!\nUsage: ?rizzdar @user")

    @commands.command()
    async def transdar(self, ctx: CustomContext, user: discord.Member = None):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                embed = await SemiFunc.pikes_radar(user, "trans")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use transdar on noone!\nUsage: ?transdar @user")

async def setup(bot):
    await bot.add_cog(Users(bot))
