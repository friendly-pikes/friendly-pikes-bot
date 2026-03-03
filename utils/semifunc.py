import asyncio
import discord
import random
import json

# from utils.data import DiscordBot
from utils.default import CustomContext
from utils.serverinfo import ServerInfo

channel_ids = ServerInfo.channels
server_ids = ServerInfo.server_ids
role_ids = ServerInfo.role_ids
ignore_ids = ServerInfo.ignore_radar_ids
forced_ids = ServerInfo.forced_radar_ids

def get_inator_text(inator_type: str):
    inator_type = inator_type.lower()
    inator_text = f"{inator_type}inator"

    return inator_text

class SemiFunc():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_banished():
        exec_dir = __file__.replace(r"\utils\semifunc.py", "")
        banished_json = None
        with open(f"{exec_dir}\\misc\\banished.json") as banished_raw:
            banished_json = json.loads(banished_raw.read())

        return banished_json
    
    async def banish_word(bot, embed, msg: discord.Message, ctx, content, banished_word, banish_message):
        try:
            print(f"banish '{content}' sent by {ctx.author.name}")

            test_or_main = ServerInfo.main_or_test_server(ServerInfo, ctx)
            auditChannel = msg.guild.get_channel(ServerInfo.channels[test_or_main]["audit"])
            
            description = f"**Message sent by {ctx.author.mention} in {ctx.channel.mention} was banished**"
            description = f"{description}\n\nMessage: {msg.content}"
            description = f"{description}\nDetected banished word: {banished_word}"
            description = f"{description}\nMessage ID: {msg.id}"

            await msg.reply(banish_message)
            await msg.delete()

            # Send a message to banish to let staff know that message was banished
            if auditChannel:
                embed.description = description

                await auditChannel.send(embed=embed)
            else:
                print(f"Cannot find audit channel!\n{description}")

            #                 if auditChannel:
            #                     des = f"**Message sent by {ctx.author.mention} in {ctx.channel.mention} was banished**"
            #                     des = f"{des}\n\nMessage: {msg.content}"
            #                     des = f"{des}\nDetected banished word: {banished_thing}"
            #                     des = f"{des}\nMessage ID: {msg.id}"

            #                     embed = self.create_embed("Banished Words", des, discord.Color.red())

            #                     await auditChannel.send(embed=embed)
            #                 else:
            #                     print(f"Cannot find audit channel!\n\n{des}")
        except Exception as e:
            await msg.channel.send("An error occurred, let <@888072934114074624> know!")
            print(f"An error occurred\n{e}")

    async def pikes_radar(bot, user: discord.Member, radar: str):
        percent = random.randint(1, 100)
        embed = bot.create_embed(bot, "", "", discord.Color.pink())

        if percent == 67:
            if random.randint(1, 2) == 1:
                percent = percent - 1
            else:
                percent = percent + 2

        if radar == "cute":
            if user.id in ignore_ids["cute"]:
                percent = 0
        elif radar == "gay":
            if user.id in ignore_ids["gay"]:
                percent = 0
                
            if user.id in forced_ids:
                percent = 101

            if user.id == 888072934114074624:
                percent = 0

        emoji = "🎀"

        if radar == "gay":
            emoji = "🏳️‍🌈"
        # elif radar == "bi":
        #     emoji = "❤️💜💙"

        embed.title = f"{emoji} {radar.capitalize()} Radar {emoji}"
        embed.description = f"{user.mention} is {percent}% {radar}! {emoji}"
        embed.color = discord.Color.pink()
        
        if radar == "cute" and percent >= 80:
            embed.description = f"{embed.description}\n{user.global_name} is totally cute!"
        elif radar == "gay" and percent >= 50:
            embed.description = f"{embed.description}\n{user.global_name} is totally gay!"


        return embed

    async def pikes_inator(bot, ctx: CustomContext, user: discord.Member, inator_type:str, do_what: str):
        vanity_role_sep = 0
        role = 0
        idsPre = ServerInfo.main_or_test_server(ctx)
        inator_text = get_inator_text(inator_type)

        if ctx.guild.get_role(role_ids[f"roles"][idsPre][inator_type]):
            vanity_role_sep = role_ids[f"seperators"][idsPre]["vanity"]
            role = role_ids[f"roles"][idsPre][inator_type]

        if user.bot:
            await ctx.reply(f"I don't think {user.mention} has invoked or has been released from the {inator_text}")
        else:
        
            if do_what == "remove":
                try:
                    if inator_type == "explode":
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They unexploded")
                        await ctx.reply(f"{user.mention} has unexploded.. how.")
                    else:
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They've been released from the {inator_text}")
                        await ctx.reply(f"{user.mention} has been released from the {inator_text}!")
                except Exception as e:
                    print(f"An error as occured with pikes_inator!\n{e}")
            else:
                try:
                    if user.get_role(role) == None:
                        if inator_type == "explode":
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They exploded")
                            await ctx.reply("https://tenor.com/view/cat-explosion-sad-explode-gif-15295996165959499721")
                        else:
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They invoked the {inator_text}")
                            await ctx.reply(f"{user.mention} has invoked of the wrath of the {inator_text}!")
                    else:
                        await ctx.send(f"{user.mention} has already invoked of the wrath of the {inator_text}. They can't invoke the {inator_text} again.")
                except Exception as e:
                    print(f"An error as occured with pikes_inator!\n{e}")
                
            await asyncio.sleep(1)

            role_ids_b = role_ids[f"roles{idsPre}"]

            ## If user doesn't have any vanity roles, remove the seperator
            if user.get_role(role_ids_b["cute"]) == None and user.get_role(role_ids_b["smol"]) == None and user.get_role(role_ids_b["explode"]) == None and user.get_role(role_ids_b["tall"]) == None:
                # safe guard cuz I'm just now adding vanity seperator to the code
                if user.get_role(vanity_role_sep):
                    await user.remove_roles(ctx.guild.get_role(vanity_role_sep), reason="No longer needs the seperator")
            else:
                await user.add_roles(ctx.guild.get_role(vanity_role_sep), reason="They need the seperator")