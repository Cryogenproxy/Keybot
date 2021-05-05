import discord
from discord.ext import commands

client = commands.Bots(command_prefix = '$')

@client.event
async def on_ready():
    print('bot is online')

client.run(TOKEN)