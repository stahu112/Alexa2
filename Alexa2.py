import discord
import datetime
import config
from discord.ext.commands import Bot
import random
import subprocess
import alexa_web

_alexa_prefix_ = ['alexa ', '!', '.']

client = Bot(command_prefix=_alexa_prefix_)


@client.command(name='rozmaryn', brief='Rymuje rozmarynuje', pass_context=True)
async def rozmaryn(context):
    rhymes = ['gitaryn', 'penisiaryn', 'kupsztalyn', 'abituryn', 'akwamaryn', 'alizaryn', 'aneuryn', 'olegezaryn',
              'fosfobakteryn', 'mandaryn', 'zjebaryn', 'ultramaryn', 'huberyn', 'hitleryn', 'uberyn', 'pikoloryn']
    await client.say(context.message.author.mention + " " + random.choice(rhymes))


@client.command(name='pac', brief='Paca kogos', description='pac pac pac', pass_context=True, aliases=['slap', 'pacnij',
                                                                                                       'pacaj',
                                                                                                       'jebnij'])
async def pac(context):
    query = context.message.content.split()
    if query[0] == 'alexa':
        query.pop(0)
    query.pop(0)

    out = ''
    for s in query:
        out += ' ' + s

    await client.send_typing(context.message.channel)
    await client.say('https://cdn.discordapp.com/attachments/678312935189119010/680166939221688363/pac.gif')
    await client.say(context.message.author.mention + " paca " + out)


@client.command(name='kluska', pass_context=True, aliases=['kektopus'])
async def kluska(context):
    query = context.message.content.split()
    if query[0] == 'alexa':
        query.pop(0)
    query.pop(0)

    out = ''
    for s in query:
        out += ' ' + s

    await client.send_typing(context.message.channel)
    await client.say('https://cdn.discordapp.com/attachments/496353603460661268/684354040443961349/ESLZ669XUAMizb8.png')


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


@client.command(name='waifu', brief="Zwraca waifu", pass_context=True)
async def waifu(context):
    await client.send_typing(context.message.channel)
    ret_url = alexa_web.get_waifu()
    await client.say(ret_url[1] + "\n" + ret_url[0])


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


@client.command(name='katnape', aliases=['nape', 'pogrzeb', 'odpoczynek'])
async def nape():
    await client.say('https://www.youtube.com/watch?v=tMVNd08R3jA')


@client.command(name='jasne', pass_context=True)
async def jasne(context):
    await client.send_typing(context.message.channel)
    await client.say("Odpalaj")
    await client.send_typing(context.message.channel)
    await client.say("Lecimy")


@client.command(name='t', pass_context=True)
async def t(context):
    query = context.message.content.split()
    if query[0] == 'alexa':
        query.pop(0)
    query.pop(0)

    cmd = query
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]

    await context.send(output)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config._alexa_key_)
