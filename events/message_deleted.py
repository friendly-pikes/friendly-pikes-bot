import discord

from discord.ext import commands
from utils.data import DiscordBot
from utils.semifunc import SemiFunc

class MessageDelete(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    # We have bots for this already
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        doLog = True

        # If main server, set doLog to config's log_audits value
        if message.guild.id == SemiFunc.server_ids["main"]:
            doLog = SemiFunc.get_config_entry("log_audits")
        

        if doLog:
            if message.author.bot == False:
                auditChannelId = SemiFunc.get_channel(message, "audit")
                auditChannel = self.bot.get_channel(auditChannelId)
                embed = SemiFunc.audit_embed("message_deleted", [message.author, message.channel, message])

                await auditChannel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MessageDelete(bot))
