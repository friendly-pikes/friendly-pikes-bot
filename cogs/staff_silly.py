import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.data import permissions
from utils.semifunc import SemiFunc

class StaffSilly(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.command()
    async def explode(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "explode", "give")

    @commands.command()
    async def cutinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "cute", "give")

    @commands.command()
    async def smolinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "smol", "give")
         
    # @commands.command()
    # async def shortinate(self, ctx: CustomContext, user: discord.Member = None):
    #     if not permissions.can_run_staff_cmd(ctx.author):
    #         await ctx.reply("You don't have permission to use that command.")
    #         return

    @commands.command()
    async def tallinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "tall", "give")

    @commands.command()
    async def uncutinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "cute", "remove")

    @commands.command()
    async def unsmolinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "smol", "remove")
        
    # @commands.command()
    # async def unshortinate(self, ctx: CustomContext, user: discord.Member = None):
    #     if not permissions.can_run_staff_cmd(ctx.author):
    #         await ctx.reply("You don't have permission to use that command.")
    #         return

    @commands.command()
    async def unexplode(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "explode", "remove")

    @commands.command()
    async def untallinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        await SemiFunc.pikes_inator(discord.Embed(title="", description=""), ctx, user, "tall", "remove")
        
        
async def setup(bot):
    await bot.add_cog(StaffSilly(bot))
