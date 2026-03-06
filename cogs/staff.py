import discord

from datetime import datetime
from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default
from utils.data import DiscordBot
from utils.semifunc import SemiFunc

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    # @commands.hybrid_command(name="ban", description="Ban a user! (diffrent from banish)")
    # async def ban(self, ctx: CustomContext, user: str, *, reason: str="No reason provided.", keep_msgs: bool):
    @commands.guild_only()
    @commands.command()
    async def ban(self, ctx: CustomContext, user_id: str, *, reason: str="No reason provided."):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        try:
            delete_message_days = 0
            user = ctx.guild.get_member(int(user_id))

            if user:
                # if keep_msgs.lower() == "no" or keep_msgs.lower() == "n":
                #     delete_message_days = 7

                reason = f"{datetime.now().strftime('%d/%m/%Y - %H:%M')} @{ctx.author.name} (Permanent): {reason}"
                # DATE - Time @punisher (Permanent): reason

                # try:
                # except discord.errors.50

                await user.ban(delete_message_days=1, reason=reason)
            else:
                await ctx.reply(f"A user with the id '{user_id}' isn't in {ctx.guild.name}")
        except Exception as e:
            await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")

    @commands.guild_only()
    @commands.hybrid_command(name="banish", description="Banish a user!")
    async def banish(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        if user != None:
            try:
                roleId = SemiFunc.get_role(ctx, "banished")
                role = ctx.guild.get_role(roleId)

                if user:
                    if permissions.can_run_staff_cmd(user):
                        await ctx.reply("Cannot banish a staff member.")
                    else:
                        if user.get_role(roleId):
                            await ctx.reply(f"Cannot banish {user.mention}, as they are already banished.")
                        else:
                            verifiedRole = user.guild.get_role(1477494681959923743)
                            
                            await user.remove_roles(verifiedRole)
                            await user.add_roles(role, reason=f"They've been banished by {ctx.author.global_name}")
                            await ctx.reply(f"{user.mention} has been banished!")
                else:
                    await ctx.reply("The user with that User ID isn't in this server.")
            except Exception as e:
                await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")
        else:
            await ctx.reply("Cannot banish noone!\nCommand usage:?banish @user")

    @commands.guild_only()
    @commands.hybrid_command(name="unbanish", description="Unbanish a user!")
    async def unbanish(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        if user != None:
            try:
                roleId = SemiFunc.get_role(ctx, "banished")
                role = ctx.guild.get_role(roleId)

                if user:
                    if permissions.can_run_staff_cmd(user):
                        await ctx.reply("Cannot banish a staff member.")
                    else:

                        if role in user.roles:
                            await user.remove_roles(role, reason=f"They've been unbanished by {ctx.author.global_name}")
                            await ctx.reply(f"{user.mention} has been unbanished")
                else:
                    await ctx.reply("The user with that User ID isn't in this server.")
            except Exception as e:
                await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")
        else:
            await ctx.reply("Cannot banish noone!\nCommand usage:?banish @user")

    @commands.guild_only()
    @commands.hybrid_command(name="verify", description="Manually verify the user with a command")
    async def verify(self, ctx: CustomContext, user: discord.Member):
        if not permissions.can_run_staff_cmd(ctx.author):
            await ctx.reply("You don't have permission to use that command.")
            return
        
        if user:
            verifiedId = SemiFunc.get_role(ctx, "verified")
            verifiedRole = user.guild.get_role(verifiedId)

            await user.add_roles(verifiedRole)
            await ctx.reply(f"Verified {user.mention}")
        else:
            ctx.reply("Can't verify noone!")


    # @commands.guild_only()
    # @commands.hybrid_command(name="afk", description="Set your status to AFK")
    # async def afk(self, ctx: CustomContext, *, reason: str = "AFK", unafk_msg: bool = False):
    #     if permissions.can_run_staff_cmd(ctx.author):

    #     else:
    #         await ctx.reply("You don't have permission to use that command.")


    @commands.guild_only()
    @commands.hybrid_command(name="reply", description="Send a message to whatever as a reply to a message!")
    async def reply(self, ctx: CustomContext, channel: discord.TextChannel, message_id: str, *, message: str):
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        if ctx.channel.id == SemiFunc.get_channel(ctx, "staff_commands"):
            if not permissions.can_run_staff_cmd(ctx.author):
                await ctx.reply("That's not a command.")
                return
            
            if channel == None:
                await ctx.reply(f"Channel is needed.\nUsage: ?repeat #channel long or short message")
                return
            
            if message == None:
                await ctx.reply(f"Message is needed.\nUsage: ?repeat #channel long or short message OR /repeat")
                return
            
            # We're good, so send message
            try:
                message_id = int(message_id)
                msg_reply = await channel.fetch_message(message_id)
                if msg_reply:
                    await msg_reply.reply(message)
                    await ctx.reply("Sent message successfully!")
                else:
                    await ctx.reply(f"Cannot find a message with the id '{message_id}' in {channel.mention}")
            except Exception as e:
                self.logger.info(msg=f"Got Exception in repeat staff command:\n{e}")
        else:
            if ctx.interaction:
                ctx.reply("Use this command in staff-commands!", ephemeral=True)
            else:
                await ctx.message.delete()
            # await ctx.reply("Wot?")

    @commands.guild_only()
    @commands.hybrid_command(name="repeat", description="Send a message to whatever channel!")
    async def repeat(self, ctx: CustomContext, channel: discord.TextChannel, *, message: str):
        SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction)
        
        if ctx.channel.id == SemiFunc.get_channel(ctx, "staff_commands"):
            if not permissions.can_run_staff_cmd(ctx.author):
                await ctx.reply("That's not a command.")
                return
            
            if channel == None:
                await ctx.reply(f"Channel is needed.\nUsage: ?repeat #channel long or short message")
                return
            
            if message == None:
                await ctx.reply(f"Message is needed.\nUsage: ?repeat #channel long or short message OR /repeat")
                return
            
            # We're good, so send message
            try:
                await channel.send(message)
                await ctx.reply("Sent message successfully!")
            except Exception as e:
                self.logger.info(msg=f"Got Exception in repeat staff command:\n{e}")
        else:
            if ctx.interaction:
                ctx.reply("Use this command in staff-commands!", ephemeral=True)
            else:
                await ctx.message.delete()
            # await ctx.reply("Wot?")

async def setup(bot):
    await bot.add_cog(Staff(bot))
