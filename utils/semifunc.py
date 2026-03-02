import asyncio
import discord

# from utils.data import DiscordBot
from utils.default import CustomContext
from utils.data import ServerInfo

server_ids = ServerInfo.server_ids
role_ids = ServerInfo.role_ids

def get_inator_text(inator_type: str):
    inator_type = inator_type.lower()
    inator_text = f"{inator_type}inator"

    return inator_text

class SemiFunc():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def pikes_inator(bot, ctx: CustomContext, user: discord.Member, inator_type:str, do_what: str):
        vanity_role_sep = 0
        role = 0
        idsPre = ""
        inator_text = get_inator_text(inator_type)

        # Test server, set idsPre so we get the test roles instead of main
        if ctx.guild.id == 1438414082448425111:
            idsPre = "_test"

        if ctx.guild.get_role(role_ids[f"roles{idsPre}"][inator_type]):
            vanity_role_sep = role_ids[f"seperators{idsPre}"]["vanity"]
            role = role_ids[f"roles{idsPre}"][inator_type]



        if user.bot:
            await ctx.reply(f"I don't think {user.mention} has invoked or has been released from the {inator_text}")
        else:
        
            if do_what == "remove":
                try:
                    if inator_text == "explode":
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They unexploded")
                        await ctx.send(f"{user.mention} has unexploded.. how.")
                    else:
                        await user.remove_roles(ctx.guild.get_role(role), reason=f"They've been released from the {inator_text}")
                        await ctx.send(f"{user.mention} has been released from the {inator_text}!")
                except Exception as e:
                    print(f"An error as occured with pikes_inator!\n{e}")
            else:
                try:
                    if user.get_role(role) == None:
                        if inator_text == "explode":
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They exploded")
                            await ctx.send("https://tenor.com/view/cat-explosion-sad-explode-gif-15295996165959499721")
                        else:
                            await user.add_roles(ctx.guild.get_role(role), reason=f"They invoked the {inator_text}")
                            await ctx.send(f"{user.mention} has invoked of the wrath of the {inator_text}!")
                    else:
                        await ctx.send(f"{user.mention} has already invoked of the wrath of the {inator_text}. They can't invoke the {inator_text} again.")
                except Exception as e:
                    print(f"An error as occured with pikes_inator!\n{e}")
                
            await asyncio.sleep(1)
            
            role_ids_b = role_ids[f"roles{idsPre}"]

            ## If user doesn't have any vanity roles, remove the seperator
            if user.get_role(role_ids_b["cute"]) == None and user.get_role(role_ids_b["smol"]) == None and user.get_role(role_ids_b["explode"]) == None:
                # safe guard cuz I'm just now adding vanity seperator to the code
                if user.get_role(vanity_role_sep):
                    await user.remove_roles(ctx.guild.get_role(vanity_role_sep), reason="No longer needs the seperator")
            else:
                await user.add_roles(ctx.guild.get_role(vanity_role_sep), reason="They need the seperator")