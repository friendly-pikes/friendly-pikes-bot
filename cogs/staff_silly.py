import discord

from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class StaffSilly(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="explode", description="Send someone to the explodinator!")
    async def explode(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return

        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "explode", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="cutinate", description="Send someone to the cutinator!")
    async def cutinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "cute", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="smolinate", description="Send someone to the smolinator!")
    async def smolinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "smol", "give")

    @commands.guild_only()
    @commands.hybrid_command(name="tallinate", description="Send someone to the tallinator!")
    async def tallinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "tall", "give")
        
    @commands.guild_only()
    @commands.hybrid_command(name="sillinate", description="Send someone to the sillinator!")
    async def sillinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "silly", "give")
        
    @commands.guild_only()
    @commands.hybrid_command(name="unexplode", description="Take someone away from the explodinator!")
    async def unexplode(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "explode", "remove")

    @commands.guild_only()
    @commands.hybrid_command(name="uncutinate", description="Take someone away from the cutinator!")
    async def uncutinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "cute", "remove")

    @commands.guild_only()
    @commands.hybrid_command(name="unsmolinate", description="Take someone away from the smolinator!")
    async def unsmolinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "smol", "remove")

    @commands.guild_only()
    @commands.hybrid_command(name="unsillinate", description="Take someone away from the sillinator!")
    async def unsillinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "silly", "remove")
        
    @commands.guild_only()
    @commands.hybrid_command(name="untallinate", description="Take someone away from the tallinator!")
    async def untallinate(self, ctx: Context, user: discord.Member):
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.is_staff(ctx.author):
            await ctx.reply("That command is staff only.")
            return
        
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)

        await SemiFunc.pikesInator(self, ctx, user, "tall", "remove")

async def setup(bot):
    await bot.add_cog(StaffSilly(bot))
