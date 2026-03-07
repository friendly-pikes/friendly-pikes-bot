import discord

from discord.ext import commands
from utils.discordbot import Bot
from utils.files import files
from utils.semifunc import SemiFunc

class OnMemberJoin(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = member.guild.get_channel( SemiFunc.get_channel_id(member, "welcome") )
        banished_ids = files._banished()['banished_ids']
        join_roles = files.get_config_entry("join_roles")

        if member.id in banished_ids:
            role = member.guild.get_role( SemiFunc.get_role_id(member, "banished") )
            channel = member.guild.get_channel( SemiFunc.get_channel_id(member, "audit") )
            
            embed = self.bot.create_embed(
                title="Dammy Files Banisher",
                description=f"User {member.display_name} ({member.name}) was banished. Reason being they are in the Dammy Files.\n\nUser Info:\nUser - {member.name}\nUserID - {member.id}",
                color=discord.Color.pink()
            )

            await member.add_roles(role)
            await channel.send(embed=embed)
            return

        if files.get_config_entry("join_message_enabled"):
            welcome_channel.send(f"Hello {member.mention}! Welcome to the server! :3")


        # Join Roles
        for rolea in join_roles:
            role = member.guild.get_role(join_roles[rolea])

            if role == "member" and member.bot:
                role = member.guild.get_role(join_roles[rolea][1])
                await member.add_roles(role, reason="Join Roles")
            elif role == "member" and member.bot == False:
                role = member.guild.get_role(join_roles[rolea][0])
                await member.add_roles(role, reason="Join Roles")
            else:
                if role:
                    await member.add_roles(role, reason="Join Roles")
                else:
                    self.bot.logger.warn(f"Cannot give {member.name} the role {rolea} as it doesn't exist!")

async def setup(bot):
    await bot.add_cog(OnMemberJoin(bot))
