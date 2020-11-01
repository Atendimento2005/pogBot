import discord
import json
import datetime
import math
import pytz
import random
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
    print('Bot is readyy')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

client.run('NzcyMzE4NDI3MTk1ODk5OTM0.X547lg.s82FDY68zvpsMjcQrYjgpkQ_U0U')