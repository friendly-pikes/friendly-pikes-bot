import discord
import random

from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class Users(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot


    # @commands.guild_only()
    # @commands.hybrid_command(name="cutedar", description="See how cute someone is!")
    # async def cutedar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "cute")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")

    # @commands.guild_only()
    # @commands.hybrid_command(name="sillydar", description="See how sillydar someone is!")
    # async def sillydar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")


    # # These radar commands are stolen from pride bot
    # # https://github.com/Pridebot-Systems/Pridebot/blob/main/src/commands/fun/
    # @commands.guild_only()
    # @commands.hybrid_command(name="bidar", description="See how bi someone is!")
    # async def bidar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")

    # @commands.guild_only()
    # @commands.hybrid_command(name="gaydar", description="See how gay someone is!")
    # async def gaydar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")

    # @commands.guild_only()
    # @commands.hybrid_command(name="queerdar", description="See how queer someone is!")
    # async def queerdar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")

    # @commands.guild_only()
    # @commands.hybrid_command(name="rizzdar", description="See how much rizz someone has!")
    # async def rizzdar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use radar commands on noone!")

    # @commands.guild_only()
    # @commands.hybrid_command(name="transdar", description="See how trans someone is!")
    # async def transdar(self, ctx: Context, user: discord.Member):
    #     if user:
    #         if user.bot:
    #             await ctx.reply("Not able to use radar commads on bots.")
    #             return
            
    #         if SemiFunc.command_disabled(ctx):
    #             await ctx.reply("That command is currently disabled.")
    #             return
            
    #         SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
    #         embed = await SemiFunc.pikesRadar(self, user, "")
    #         await ctx.reply(embed=embed)
    #     else:
    #         await ctx.reply("Can't use transdar on noone!")

async def setup(bot):
    await bot.add_cog(Users(bot))
