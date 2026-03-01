import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.data import permissions

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.command()
    async def banish(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx):
            ctx.reply("You don't have permission to use that command.")
        
        if user:
            roleId = 1477496210414768243

            # Test
            if ctx.guild.id == 1438414082448425111:
                roleId = 1477575309476761672

            role = ctx.guild.get_role(roleId)

            if role in user.roles:
                await user.remove_roles(role)
                await ctx.reply(f"{user.mention} has been unbanished")
            else:
                await user.add_roles(role)
                await ctx.reply(f"{user.mention} has been banished!")
        else:
            ctx.reply("Cannot banish noone!\nCommand usage:?banish @user")

async def setup(bot):
    await bot.add_cog(Staff(bot))
