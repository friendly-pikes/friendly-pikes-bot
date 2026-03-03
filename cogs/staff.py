import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot, ServerInfo

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    @commands.command()
    async def repeat(self, ctx: CustomContext, channelId: int, *, message: str):
        main_or_test = ServerInfo.main_or_test_server(ServerInfo, ctx)
        
        if ctx.channel.id == ServerInfo.channels[main_or_test]["staff_commands"]:

            if channelId == None:
                await ctx.reply(f"Channel is needed.\nUsage: ?repeat channel_id long or short message")
                return
            
            if message == None:
                await ctx.reply(f"Message is needed.\nUsage: ?repeat channel_id long or short message")
                return
            
            # We're good, so send message
            try:
                if ctx.guild.get_channel(channelId):
                    channel = ctx.guild.get_channel(channelId)
                    await channel.send(message)
                    await ctx.reply("Send message successfully!")
                else:
                    good = False
                    for guild in self.bot.guilds:
                        if guild.get_channel(channelId):
                            good = True
                            channel = guild.get_channel(channelId)
                            await channel.send(message)
                            await ctx.reply("Send message successfully!")

                    if good == False:
                        await ctx.reply(f"Cannot find a channel with the id '{channelId}'")
            except Exception as e:
                print(f"Got Exception in repeat staff command:\n{e}")
        else:
            await ctx.message.delete()
            # await ctx.reply("Wot?")


    # @commands.command()
    # async def verify(self, ctx: CustomContext, user: discord.Member = None):
    #     if not permissions.can_run_staff_cmd(ctx.author):
    #         await ctx.reply("You don't have permission to use that command.")
    #         return
        
    #     if user:
    #         verifiedRole = user.guild.get_role(1477494681959923743)

    #         await user.add_roles(verifiedRole)
    #         await ctx.reply(f"Verified {user.mention}")
    #     else:
    #         ctx.reply("Can't verify noone!")

    @commands.command()
    async def banish(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        if user:
            roleId = 1477496210414768243

            # Test
            if ctx.guild.id == 1438414082448425111:
                roleId = 1477575309476761672

            role = ctx.guild.get_role(roleId)

            if permissions.can_run_staff_cmd(user):
                await ctx.reply("Cannot banish a staff member.")
            else:
                if role in user.roles:
                    await user.remove_roles(role, reason=f"They've been unbanished by {ctx.author.global_name}")
                    await ctx.reply(f"{user.mention} has been unbanished")
                else:
                    verifiedRole = user.guild.get_role(1477494681959923743)
                    
                    await user.remove_roles(verifiedRole)
                    await user.add_roles(role, reason=f"They've been banished by {ctx.author.global_name}")
                    await ctx.reply(f"{user.mention} has been banished!")
        else:
            await ctx.reply("Cannot banish noone!\nCommand usage:?banish @user")

    @commands.command()
    async def unbanish(self, ctx: CustomContext, user: discord.Member = None):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return

        if user:
            roleId = 1477496210414768243

            # Test
            if ctx.guild.id == 1438414082448425111:
                roleId = 1477575309476761672

            role = ctx.guild.get_role(roleId)

            if permissions.can_run_staff_cmd(user):
                await ctx.reply("Cannot banish or unbanish a staff member.")
            else:
                if role in user.roles:
                    await user.remove_roles(role, reason=f"They've been unbanished by {ctx.author.global_name}")
                    await ctx.reply(f"{user.mention} has been unbanished")
        else:
            await ctx.reply("Cannot banish noone!\nCommand usage:?unbanish @user")

async def setup(bot):
    await bot.add_cog(Staff(bot))
