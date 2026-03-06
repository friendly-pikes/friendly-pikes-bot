import discord

from discord.ext import commands
from utils.data import DiscordBot
from utils.semifunc import SemiFunc

class MessageEdited(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    # We have bots for this already
    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        doLog = True

        # If main server, set doLog to config's log_audits value
        if before.guild.id == SemiFunc.server_ids["main"]:
            doLog = SemiFunc.get_config_entry("log_audits")
        

        if doLog:
            if before.author.bot == False:
                auditChannelId = SemiFunc.get_channel(after, "audit")
                auditChannel = self.bot.get_channel(auditChannelId)
                embed = SemiFunc.audit_embed("message_edited", [before.author, before.channel, before, after])

                await auditChannel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(MessageEdited(bot))
