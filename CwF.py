import discord

class MyClient(discord.Client):
    
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

client = MyClient()
client.run('ODg4OTE2NDQ1Njg0MTg3MTc2.YUZp8w.ut-KQsj5kd-7Ezk_kS4rkUMFfaA')
