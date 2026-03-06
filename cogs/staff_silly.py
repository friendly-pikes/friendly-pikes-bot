import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default
from utils.data import DiscordBot

from utils.data import permissions
from utils.semifunc import SemiFunc

class StaffSilly(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="explode", description="Explode someone!")
    async def explode(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "explode", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="cutinate", description="Sent someone to the cuteinator!")
    async def cutinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "cute", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="smolinate", description="Sent someone to the smolinator!")
    async def smolinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikes_inator(self, ctx, user, "smol", "give")
         
    # @commands.guild_only()
    # @commands.hybrid_command()
    # async def shortinate(self, ctx: CustomContext, user: discord.Member):
    #     if not permissions.can_run_staff_cmd(ctx.author):
    #         SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
    #         await ctx.reply("You don't have permission to use that command.")
    #         return
        
    #     SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

    @commands.guild_only()
    @commands.hybrid_command(name="tallinate", description="Sent someone to the tallinator!")
    async def tallinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "tall", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="uncutinate", description="Take someone away from the cuteinator!")
    async def uncutinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "cute", "remove")

    @commands.guild_only()
    @commands.hybrid_command(name="unsmolinate", description="Take someone away from the smolinator!")
    async def unsmolinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "smol", "remove")
        
    # @commands.guild_only()
    # @commands.hybrid_command()
    # async def unshortinate(self, ctx: CustomContext, user: discord.Member):
    #     if not permissions.can_run_staff_cmd(ctx.author):
    #         SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
    #         await ctx.reply("You don't have permission to use that command.")
    #         return
        
    #     SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

    @commands.guild_only()
    @commands.hybrid_command(name="unexplode", description="Unexplode someone!")
    async def unexplode(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "explode", "remove")

    @commands.guild_only()
    @commands.hybrid_command(name="untallinate", description="Take someone away from the tallinator!")
    async def untallinate(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            SemiFunc.log_command_use(self.bot, ctx.author, f"tried to use {ctx.message.content}")
            await ctx.reply("You don't have permission to use that command.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        await SemiFunc.pikes_inator(self, ctx, user, "tall", "remove")
        
        
async def setup(bot):
    await bot.add_cog(StaffSilly(bot))
