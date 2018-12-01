import discord, pyperclip

TOKEN = ''
wordlist = ''

words = open(wordlist).readlines()
client = discord.Client()

@client.event
async def on_message(message):
    if message.author.id == '432610292342587392':
        if "Type the longest word containing:" in message.content:
            phrase = message.content[65:68].lower()
            for i in words:
                if phrase in i:
                    pyperclip.copy(i.strip('\n'))
                    print(i.strip('\n'))
                    break

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)