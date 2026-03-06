import discord
import random

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default
from utils.data import DiscordBot

from utils.semifunc import SemiFunc

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="cutedar", description="See how cute someone is!")
    async def cutedar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "cute")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use cutedar on noone!\nUsage: ?cutedar @user")

    @commands.guild_only()
    @commands.hybrid_command(name="sillydar", description="See how silly someone is!")
    async def sillydar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "silly")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use sillydar on noone!\nUsage: ?sillydar @user")

    # These radar commands are stolen from pride bot
    # https://github.com/Pridebot-Systems/Pridebot/blob/main/src/commands/fun/
    @commands.guild_only()
    @commands.hybrid_command(name="bidar", description="See how bi someone is!")
    async def bidar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "bi")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use bidar on noone!\nUsage: ?bidar @user")

    @commands.guild_only()
    @commands.hybrid_command(name="gaydar", description="See how gay someone is!")
    async def gaydar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "gay")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use gaydar on noone!\nUsage: ?gaydar @user")

    @commands.guild_only()
    @commands.hybrid_command(name="queerdar", description="See how queer someone is!")
    async def queerdar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                try:
                    embed = await SemiFunc.pikes_radar(self, user, "queer")
                    await ctx.reply(embed=embed)
                except Exception as e:
                    await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")
        else:
            await ctx.reply("Can't use queerdar on noone!\nUsage: ?queerdar @user")

    @commands.guild_only()
    @commands.hybrid_command(name="rizzdar", description="See how rizz someone has!")
    async def rizzdar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "rizz")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use rizzdar on noone!\nUsage: ?rizzdar @user")

    @commands.guild_only()
    @commands.hybrid_command(name="transdar", description="See how trans someone is!")
    async def transdar(self, ctx: CustomContext, user: discord.Member):
        if user:
            if user.bot:
                await ctx.reply("Not able to use radar commads on bots.")
            else:
                SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
                embed = await SemiFunc.pikes_radar(self, user, "trans")
                await ctx.reply(embed=embed)
        else:
            await ctx.reply("Can't use transdar on noone!\nUsage: ?transdar @user")

async def setup(bot):
    await bot.add_cog(Users(bot))
