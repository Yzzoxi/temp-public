import discord
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
from pip._vendor import requests
import datetime
import json
import mysql.connector
import asyncio
from tabulate import tabulate
import aiohttp
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
token = 'you thought'
bot = commands.Bot(command_prefix='?', case_insensitive=True)
# no longer needed game = discord.Game('Alle groups server')

truckerbd = 'Jamesmay#0001'
@bot.command()
async def info(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="ALLE GROUP", color=0xFF0000)
  embed.add_field(name="CEO", value="Sully#3056 ", inline=False)
  embed.add_field(
      name="COO", value="CarlJL2006#8589,Speedy#2286", inline=False)
  embed.add_field(name="CCO", value="jamesmay#8635,LC#2328", inline=False)
  embed.add_field(name="DIRECTOR OF AGRICULTURE",
                  value="NoahTheFox#4148", inline=False)
  embed.add_field(name="TRANSPORT MANGER", value="lewis#4672", inline=False)
  embed.add_field(name="EVENT MANAGER", value="TRUCKERBEAN#0001", inline=False)
  embed.add_field(name="DIRECTOR OF DEVELOPEMENT",
                  value="_Guuuty#8864", inline=False)
  embed.add_field(name="DIRECTOR OF HUMAN RESOURCES",
                  value="Desmond Doss#9332", inline=False)
  embed.add_field(name="DEX", value="Yzzoxi#3590", inline=False)
  embed.add_field(
      name="DEV TEAM", value="Adriano Trezub#3845, StarAssassin64#9196", inline=False)
  embed.add_field(name="HUMAN RESOURCES",
                  value="Saà¹‡à¹‡à¹‡ni#8080", inline=False)
  embed.add_field(name="EVENT / MEDIA TEAM",
                  value="currently hiring", inline=False)
  await ctx.send(embed=embed)
  await ctx.message.delete()





bot.run(token, bot=True)
