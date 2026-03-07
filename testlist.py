import os
class Bot():
    def test():
        ## Load listener cogs
        for file in os.listdir("listeners"):
            # Ignore files that aren't .py files
            if not file.endswith(".py"):
                continue

            name = file[:-3]
            # await self.load_extension(f"listeners.{name}")
            
        ## Load command cogs
        for who in os.listdir("cogs"):
            gud = True
            if who == "__pycache__":
                gud = False


            if gud:
                for file in os.listdir(f"cogs/{who}"):
                    # Ignore files that aren't .py files
                    if not file.endswith(".py"):
                        continue
                    
                    name = file[:-3]
                    print(f"cogs.{who}.{name}")
                    # await self.load_extension(f"cogs.{who}.{name}")

Bot.test()