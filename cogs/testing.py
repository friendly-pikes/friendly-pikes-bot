
import discord

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions
from utils.data import DiscordBot

from utils.semifunc import SemiFunc

class OwnerTest(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    ## Hybrid Commands
    # @commands.hybrid_command()
    # @commands.check(permissions.is_owner)
    # async def test(self, ctx: CustomContext, a: str, b: str, c: str, d: str, e: str):
    #     interaction: discord.Interaction = ctx.interaction
        
    #     SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, interaction)

    # @commands.hybrid_command()
    # @commands.check(permissions.is_owner)
    # async def auditembed(self, ctx: CustomContext):
    #     await ctx.send(embed=SemiFunc.audit_embed("message_deleted", [ctx.author, ctx.channel, ctx.message]))

    # @commands.hybrid_command()
    # @commands.check(permissions.is_owner)
    # async def copyembed(self, ctx: CustomContext, source_message_id: int, target_channel_id: int):
    #     try:
    #         good = False


    #         print(f"Copying embed from message {source_message_id} to channel {target_channel_id}...")

            
    #         source_message = await ctx.fetch_message(source_message_id) # Fetch the source message
    #         target_channel = self.bot.get_channel(target_channel_id) # Fetch the target channel

    #         for guild in self.bot.guilds:
    #             if guild.get_channel(source_message_id):
    #                 source_message = await ctx.fetch_message(source_message_id)

    #         # Check if the source message has an embed
    #         if source_message.embeds:
    #             embed = source_message.embeds[0] # Get the first embed from the source message

    #             # Send the embed to the target channel
    #             # await target_channel.send(embed=embed)
    #             await ctx.message.delete()
    #             print(f"description: {embed.description}\n\nfields: {embed.fields}")

    #             print("Embed copied successfully.")
    #         else:
    #             print("Source message does not have an embed!")
    #             await ctx.send("Source message does not have an embed.")
    #     except discord.NotFound:
    #         print("Source message or target channel not found.")
    #         await ctx.send("Source message or target channel not found.")
    #     except Exception as e:
    #         await ctx.reply(f"A error occured while executing the command!\n{SemiFunc.mention_snowy()}\n```{e}```")


async def setup(bot):
    await bot.add_cog(OwnerTest(bot))
