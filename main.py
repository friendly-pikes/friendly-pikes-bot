import discord
import os
from discord.ext import commands
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)

banishUserIds = [
    1403877222959419423, # Test
    # 825309596784001024 # FreddyCR  (just in case..)
    495293024394543124, # FoxyOwo
    626154564202266636, # Dammy
    1070256519897161749, # Danny
    1262934126844182633, # Rubicon
    400045916762931203 # Archie
]

def createEmbed(title, description, color):
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    embed.set_footer(text=f"Bot developed by snow2code")

@bot.event
async def on_ready():
    print(f"\nBot is ready! Signed in as {bot.user} ")

@bot.event
async def on_member_join(member):
    if member.id in banishUserIds:
        channelId = 0
        roleId = 0
        guildId = 1438414082448425111
        print(f"Banish {member.global_name} ({member.id})!")
        

        # Test server
        if member.guild.id == 1438414082448425111:
            channelId = 1441948227158151248
            roleId = 1477575309476761672
        else:
            guildId = member.guild.id
            roleId = 1477496210414768243
            
        print(roleId)
        await bot.add_roles(member, roleId)

        ## Opitional - Send a embed message to General about the banish of them
        # await member.guild.get_channel(channelId).send(
        #     embed = createEmbed("Title (Change me!)", f"Whatever message for banish FW Files mentioned user.\n\n{member.global_name} ({member.id}) was banished", discord.Color.blurple())
        # )

bot.run(os.getenv("TOKEN"))