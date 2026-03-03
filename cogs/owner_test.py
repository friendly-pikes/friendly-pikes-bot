

from discord.ext import commands
from utils.default import CustomContext
from utils import permissions, default, http
from utils.data import DiscordBot

from utils.semifunc import SemiFunc

class OwnerTest(commands.Cog):
    def __init__(self, bot):
        self.bot: DiscordBot = bot

    # @commands.command()
    # @commands.check(permissions.is_owner)
    # async def remotejson(self, ctx: CustomContext):
    #     print(SemiFunc.call_snow2code_api("discord_bot/banished_words"))
    #     # with open('https://raw.githubusercontent.com/friendly-pikes/friendly-pikes-bot/refs/heads/main/misc/banished_words.json') as json_data:
    #     #     d = json.load(json_data)
    #     #     print(d)


async def setup(bot):
    await bot.add_cog(OwnerTest(bot))
