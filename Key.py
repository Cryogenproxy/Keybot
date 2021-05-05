import discord
import os 
import discord.ext import commands
import asyncio

TOKEN = os.environ['TOKEN']
client = discord.Client()
client = commands.Bot(comma_prefix = '$')

@client.event
async def on_ready():
    print('bot is online')

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name="Help: ")
    embed.add_field(name="help", value="Help Command", inline=False)

    await client.send_message(author, embed=embed)
    await client.say("Message sent to your DM's :thumbsup:")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong Bitch you been hacked!')

@client.event

async def on_message(message):
    if message.content == 'skynet':
        await message.channel.send('Execute Y/N?')

@asyncio.coroutine
async def delete_messages(messages):
    if message.content == 'Y':
        await message.delete_messages()

client.run(TOKEN)
