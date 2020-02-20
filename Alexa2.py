import discord
import config
from discord.ext.commands import Bot
import random
import alexa_web


_alexa_prefix_ = ['alexa ', '!', '.']

client = Bot(command_prefix=_alexa_prefix_)


@client.command(name='rozmaryn', brief='Rymuje rozmarynuje', pass_context=True)
async def rozmaryn(context):
    rhymes = ['gitaryn', 'penisiaryn', 'kupsztalyn', 'abituryn', 'akwamaryn', 'alizaryn', 'aneuryn', 'olegezaryn',
              'fosfobakteryn', 'mandaryn', 'zjebaryn', 'ultramaryn', 'huberyn', 'hitleryn', 'uberyn', 'pikoloryn']
    await client.say(context.message.author.mention + " " + random.choice(rhymes))


@client.command(name='yt', brief="Zwraca link do filmiku na yt",
                description="Wysyła link do filmu na youtube po wybranym zapytaniu, przykładowo: alexa yt crab rave",
                pass_context=True, aliases=['youtube', 'play'])
async def yt(context):
    query = context.message.content.split()
    if query[0] == 'alexa':
        query.pop(0)
    query.pop(0)

    await client.send_typing(context.message.channel)
    vid = alexa_web.get_yt(query)
    await client.say(context.message.author.mention + " " + vid)


@client.command(name='img', brief="Zwraca obrazek z google graphics",
                description="Zwraca obrazek z google graphics po zapytaniu",
                pass_context=True, aliases=['pokaz', 'show', 'i'])
async def img(context):
    query = context.message.content.split()
    if query[0] == 'alexa':
        query.pop(0)
    query.pop(0)

    await client.send_typing(context.message.channel)
    image = alexa_web.get_img_google(query)
    await client.say(context.message.author.mention + " " + image)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config._alexa_key_)
