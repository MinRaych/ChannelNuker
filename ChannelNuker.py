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
        async for element in channel.history(limit=999999999999999999999999999999999999999999999999999999999999999999999):
            print(element.content)
            if element.author == client.user:
                if element.content == "" and len(element.embeds) == 0 and len(element.attachments) == 0:
                    break
                await element.delete()
        sys.exit(0)
    else:
        try:
            user = client.get_user(int(id))
            channel = await user.create_dm()
            async for element in channel.history(limit=999999999999999999999999999999999999999999999999999999999999999999999):
                print(element.content)
                if element.author == client.user:
                    if element.content == "" and len(element.embeds) == 0 and len(element.attachments) == 0:
                        break
                    await element.delete()
            sys.exit(0)
        except:
            sys.exit(0)

client.run(token, bot=False)
