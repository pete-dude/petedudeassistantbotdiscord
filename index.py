import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!help'):
            await message.channel.send('Welcome to Dude FX! Say -new in #request to request something. {0.author.mention}'.format(message))

client = MyClient()
client.run('NzA1NDgzOTQ4NjQ1NDE3MDUx.XrMOBg.TReTHjEpPrPeaJrNVBo65S2uKCk')