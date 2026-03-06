import discord

from datetime import datetime
from discord.ext import commands
from utils.discordbot import Bot
from utils.semifunc import SemiFunc
from utils.files import files

class OnMessageDelete(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        doLog = True
        
        # If main server, set doLog to config's log_audits_enabled value
        if message.guild.id == files.get_server_id("main"):
            doLog = files.get_config_entry("log_audits_enabled")
        

        if doLog:
            if message.author.bot == False:
                auditChannelId = files.get_channel_id(message, "audit")
                auditChannel = self.bot.get_channel(auditChannelId)
                
                embed = self.bot.create_embed_notitle(
                    description=f"**Message sent by {message.author.mention} was deleted in {message.channel.mention}**",
                    color=discord.Color.red(),
                    fields=[
                        {
                            "name": "message:",
                            "value": f"```{message.content}```",
                            "inline": False
                        },
                    ]
                )

                embed.timestamp = datetime.utcnow()
                embed.set_author(name=message.author.name, icon_url=message.author.avatar)
                embed.set_footer(text=f"User ID: {message.author.id} • Bot developed by snow2code")
                
                await auditChannel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(OnMessageDelete(bot))
