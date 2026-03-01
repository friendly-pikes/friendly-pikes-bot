import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.data import permissions

# 1477749083404767364 - Test cute role
# 1477749159997214863 - Test shortie role
# 1477749196366020780 - Test smol role

class StaffSilly(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.command()
    async def cutinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781229599199434

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749083404767364
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from the cutinator!")
            else:
                await user.add_roles(role)
                await ctx.reply(f"{user.mention} has invoked of the wrath of the cutinator!")

    @commands.command()
    async def smolinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781211622539326

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749196366020780
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from the smolinator!")
            else:
                await user.add_roles(role)
                await ctx.reply(f"{user.mention} has invoked of the wrath of the smolinator!")
         
    @commands.command()
    async def shortinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781226910912563

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749196366020780
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from the shortinator!")
            else:
                await user.add_roles(role)
                await ctx.reply(f"{user.mention} has invoked of the wrath of the shortinator!")
         

    @commands.command()
    async def uncutinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781229599199434

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749083404767364
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from the cutinator!")

    @commands.command()
    async def unsmolinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781211622539326

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749196366020780
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from the smolinator!")
        
    @commands.command()
    async def unshortinate(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(user):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        ## Testy Test
        roleId = 1477781226910912563

        if ctx.guild.id == 1438414082448425111:
            roleId = 1477749196366020780
        
        # We need a user to cutinate god damn it!
        # (checking if user was given with command)
        if user != None:
            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been released from theshortinate!")
        
async def setup(bot):
    await bot.add_cog(StaffSilly(bot))
