import sys
import discord
# - Download discord.py https://pypi.org/project/discord.py/ #

token = "" # <-- Token
id = "" # <-- Channel's id or User's id
client = discord.Client()

@client.event
async def on_connect():
    channel = client.get_channel(int(id))
    if channel is not None:
        async for element in channel.history():
            try:
                await element.delete()
            except:
                continue
        sys.exit()
    else:
        try:
            user = client.get_user(int(id))
            channel = await user.create_dm()
            async for element in channel.history():
                try:
                    await element.delete()
                except:
                    continue
            sys.exit()
        except:
            return


client.run(token, bot=False)
