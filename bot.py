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
token = 'NzcwMzQzMjM1MjE3Nzg0ODYy.X5cMCw.2lSdAtFEIvx4QkvuKp9PZXfvecc'
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





@bot.command()
async def nextconvoy(ctx):
  embed = discord.Embed(title="ALLE GROUPS NEXT CONVOY", color=0xFF0000)
  embed.add_field(name="DATE", value=f"N/A", inline=True)
  embed.add_field(name="SERVER", value=f"N/A", inline=False)
  embed.add_field(name="ORIGIN", value=f"N/A ", inline=False)
  embed.add_field(name="DESTINATION", value=f"N/A", inline=False)
  embed.add_field(name="MEET", value=f"N/A", inline=False)
  embed.add_field(name="DEPART", value=f"N/A", inline=False)
  embed.add_field(name="CARS", value=f"N/A", inline=False)
  embed.add_field(name="TRAILERS", value=f"N/A", inline=False)
  embed.add_field(name="NO TIME ZONE", value=f"N/A", inline=False)
  embed.add_field(name="TMP EVENT SIGN UP ", value=f"N/A", inline=False)
  embed = discord.Embed(description="do `announce1` or `convoy` to add a convoy xD. But pls note that at the current time CONVOYS ARE CANCELLED. You are not seeing the convoy info due to convoys being stopped. :) P.S the next couple of public convoys are `25th-january-prime-convoy` `26th-january-rlc-convoy` `28th-january-truckers-chn-convoy` hope to see ya at them. ", inline=False)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def apply(ctx):
  embed = discord.Embed(title="WELCOME TO ALLE GROUP", color=0xFF0000)
  embed.add_field(name="APPLY HERE",
                  value=f"https://truckersmp.com/vtc/13006", inline=True)
  await ctx.send(embed=embed)
  await ctx.message.delete()


@bot.command()
async def test(ctx, *, message):
    embed = discord.Embed(description=message, color=0xFF0000)
    await ctx.send(embed=embed)


@bot.command()
async def announce(ctx, *, message):
    await ctx.message.delete()
    channel1 = bot.get_channel(794887947865817088)
    embed = discord.Embed(description=message, color=0xFF0000)
    embed.set_footer(
        text=f"sent by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    await channel1.send(embed=embed)


@bot.command()
async def helpannounce(ctx):
    await ctx.message.delete()
    await ctx.send("please do `?announce` to announce something like a driver leaving / joining or a driver becoming staff. *** DO NOT USE THIS TO ANNOUNCE CONVOYS ***")


@bot.command()
async def announce1(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="ALLE GROUP MESSAGE EMBED", color=0xFF0000)
    embed.add_field(name="Messsage", value=message, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def partnerc(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(
        title="ALLE GROUP PARTNER / PUBLIC CONVOY POSTING SYSTEM", color=0xFF0000)
    embed.add_field(name="convoy info", value=message, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def carl(ctx):
   await ctx.message.delete()
   await ctx.send(" Mr bot greeter   :rofl: nutter :smile:")


@bot.command()
async def speedy(ctx):
   await ctx.message.delete()
   await ctx.send(" Im fast as f##k boiiii. *** look at my disco lights ***")
   #await ctx.send ("its my brithday woooooo im another year older")
   await ctx.send("https://cdn.discordapp.com/attachments/794887186990366750/801142872966561812/20210119153518_1.jpg")
   #await ctx.send("https://cdn.discordapp.com/attachments/756549175759470676/801252071923908668/20210120004307_1.jpg")


@bot.command()
async def sully(ctx):
    await ctx.message.delete()
    await ctx.send(" the boss i dont mess with him `error 68` ")


@bot.command()
@commands.has_role('Human Resources')
async def add(ctx, steamid, tmpid, name):
 await ctx.message.delete()
 mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Fv4&4*JT61%8WGj&vwj",
     database="alle_hub"
 )
 mycursor = mydb.cursor()

 sql = "INSERT INTO users (steam_id, tmp_id, name) VALUES (%s, %s, %s)"
 val = (f"{steamid}", f"{tmpid}", f"{name}")
 mycursor.execute(sql, val)

 mydb.commit()
 embed = discord.Embed(title="Welldone u added a driver", color=0xFF0000)
 embed.add_field(name="Name", value=f"{name}", inline=False)
 embed.add_field(name="TMP ID", value=f"{tmpid}", inline=False)
 embed.add_field(name="STEAM ID", value=f"{steamid}", inline=False)
 await ctx.send(embed=embed)
 channel1 = bot.get_channel(794888270923300884)
 embed1 = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator}",
                        icon_url=ctx.author.avatar_url, color=0xFF0000)
 embed1.add_field(
     name=f"This user  just added driver {name} to the api using", value="`?add`", inline=False)
 await channel1.send(embed=embed1)
 mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="Fv4&4*JT61%8WGj&vwj",
     database="alle_hub"
 )
 cursor = mydb.cursor()
 cursor.execute("select count(name) from users;")
 result = cursor.fetchall()
 results = result
 await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{results} drivers"))


@bot.command()
async def dev1(ctx):
  if ctx.message.author.server_permissions.administrator:
   await ctx.message.delete()
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="Fv4&4*JT61%8WGj&vwj",
       database="alle_hub"
   )
   mycursor = mydb.cursor()
   cursor = mydb.cursor()

   mycursor.execute("SELECT name FROM users")
   myresult = mycursor.fetchall()
   cursor.execute("select count(name) from users;")
   result = cursor.fetchall()
   await ctx.send(tabulate(myresult, headers=['users'], tablefmt='psql'))


@bot.command()
async def drivers(ctx):
  await ctx.message.delete()
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Fv4&4*JT61%8WGj&vwj",
      database="alle_hub"
  )
  mycursor = mydb.cursor()
  cursor = mydb.cursor()

  mycursor.execute("SELECT name FROM users")
  myresult = mycursor.fetchall()
  cursor.execute("select count(name) from users;")
  result = cursor.fetchall()
  embed = discord.Embed(title="Drivers List", color=0xFF0000)
  embed.add_field(name="List of drivers", value=myresult, inline=False)
  embed.add_field(name="Total Number Of Drivers", value=result, inline=False)
  #await ctx.send(tabulate(myresult, headers=['users'], tablefmt='psql'))
  await ctx.send(embed=embed)
  results = result

  channel = bot.get_channel(794888270923300884)
  embed1 = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator}",
                         icon_url=ctx.author.avatar_url, color=0xFF0000)
  embed1.add_field(name="This user  just checked the amount of drivers using ",
                   value="`?drivers`", inline=False)
  await channel.send(embed=embed1)


@bot.event
async def on_ready():
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="Fv4&4*JT61%8WGj&vwj",
       database="alle_hub"
   )
   cursor = mydb.cursor()
   cursor.execute("select count(name) from users;")
   result = cursor.fetchall()
   results = result
   print("My body is ready")
   await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Rosskemp on the frontline"))
# change async def (members) change the members bit to what ever u want.


@bot.command()
async def members(ctx):
 r = requests.get("https://api.truckersmp.com/v2/vtc/13006")
 data = r.json()
 members_count = r.json()['response']['members_count']
 await ctx.send(f'The amount of drivers and staff in this vtc is {members_count}')


@bot.command()
async def servers(ctx):
 await ctx.message.delete()
 getserversURL = "https://api.truckersmp.com/v2/servers"
 r = requests.get(getserversURL)
 data = r.json()["response"]
 embed = discord.Embed(title="TMP Server Status",
                       url="https://traffic.krashnz.com/", color=0xFF0000)
 embed.set_thumbnail(url='https://truckersmp.com/assets/img/avatar.png')
 embed.set_footer(
     text="Bot Devloped by  StarAssassin64#9196 and Jamesmay#0001")
 for server in data:
    serverid = server["id"]
    game = server["game"]
    name = server["shortname"]
    players = str(server["players"])
    queue = str(server["queue"])
    maxplayers = str(server["maxplayers"])
    online = (server["online"])
    if online:
      online = " :white_check_mark:"
    else:
      online = " :x:"
    embed.add_field(name=game + ": " + name + online,
                    value=players + '/' + maxplayers, inline=True)
 await ctx.send(embed=embed)
# command ofa


@bot.command()
async def traffic(ctx):
 await ctx.message.delete()
 getserversURL = "https://traffic.krashnz.com/api/v2/public/server/ets2/sim1/top.json"
 r = requests.get(getserversURL)
 data = r.json()["response"]
 embed = discord.Embed(title="TMP Traffic Status (SIM 1)",
                       url="https://traffic.krashnz.com/", color=0xFF0000)
 embed.set_thumbnail(url='https://truckersmp.com/assets/img/avatar.png')
 embed.set_footer(
     text="Bot Devloped by  StarAssassin64#9196 and Jamesmay#0001")
 for top in data["top"]:
    id = top["id"]
    name = top["name"]
    country = top["country"]
    players = str(top["players"])
    severity = top["severity"]
    embed.add_field(name=name,
                    value=severity + '' + ':octagonal_sign: ' + "(" + players + ")", inline=True)
 await ctx.send(embed=embed)


@bot.command()
async def traffic2(ctx):
 await ctx.message.delete()
 getserversURL = "https://traffic.krashnz.com/api/v2/public/server/ets2/sim2/top.json"
 r = requests.get(getserversURL)
 data = r.json()["response"]
 embed = discord.Embed(title="TMP Traffic Status (SIM 2)",
                       url="https://traffic.krashnz.com/", color=0xFF0000)
 embed.set_thumbnail(url='https://truckersmp.com/assets/img/avatar.png')
 embed.set_footer(
     text="Bot Devloped by  StarAssassin64#9196 and " + "" + truckerbd)
 for top in data["top"]:
    id = top["id"]
    name = top["name"]
    country = top["country"]
    players = str(top["players"])
    severity = top["severity"]
    embed.add_field(name=name,
                    value=severity + '' + ':octagonal_sign: ' + "(" + players + ")", inline=True)
 await ctx.send(embed=embed)


@bot.command()
async def traffic3(ctx):
 await ctx.message.delete()
 getserversURL = "https://traffic.krashnz.com/api/v2/public/server/ets2/sim3/top.json"
 r = requests.get(getserversURL)
 data = r.json()["response"]
 embed = discord.Embed(title="TMP Traffic Status (SIM 3)",
                       url="https://traffic.krashnz.com/", color=0xFF0000)
 embed.set_thumbnail(url='https://truckersmp.com/assets/img/avatar.png')
 embed.set_footer(
     text="Bot Devloped by  StarAssassin64#9196 and Jamesmay#0001")
 for top in data["top"]:
    id = top["id"]
    name = top["name"]
    country = top["country"]
    players = str(top["players"])
    severity = top["severity"]
    embed.add_field(name=name,
                    value=severity + '' + ':yellow_circle: : ' + "(" + players + ")", inline=True)
 await ctx.send(embed=embed)


@bot.command()
async def status(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="ALLE SERVICES STATUS", color=0xFF0000)
  embed.add_field(name=" BOT STATUS",
                  value=":green_square:  'BOT IS ONLINE'", inline=True)
  embed.add_field(name=" CONVOY ADDING STATUS",
                  value=":red_square:  CONVOY ADDING IS OFFLINE DUE TO CONVOYS BEING STOPPED", inline=True)
  embed.add_field(name="WEB SERVER STAUS",
                  value=":red_square: WEB SERVER IS UNDER GOING MAINTENANCE", inline=True)
  embed.add_field(name="ALLE DRIVERS HUB STAUS",
                  value=":red_square:  ALLE DRIVERS HUB IS OFFLINE", inline=True)
  embed.add_field(name="DISCORD RICH PRESENCE STAUS",
                  value=":red_square: DISCORD RICH PRESENCE IS OFFLINE", inline=True)
  embed.add_field(name="API STAUS",
                  value=":green_square: API IS ONLINE", inline=True)
  embed.add_field(name="JOB TRACKING STAUS",
                  value=":red_square: JOB TRACKING IS OFFLINE", inline=True)
  embed.add_field(name=" ADD A DRIVER STAUS",
                  value=":green_square: ADD A DRIVER IS ONLINE", inline=True)
  embed.set_footer(text="'ALLE SERVICES POWERED BY ALLE API'")
  await ctx.send(embed=embed)
# use this command to kick users


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
     await member.kick(reason=reason)
     await ctx.send(f'{member.mention} has been kicked for the following reason: {reason}')




#use this to ban members / users


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
     await member.ban(reason=reason)
     await ctx.send(f'{member.mention} has been banned for the following reason: {reason}')

#use this to unban banned members


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
     banned_users = await ctx.guild.bans()
     member_name, member_discriminator = member.split("#")
     for ban_entry in banned_users:
         user = ban_entry.user
         if (user.name, user.discriminator) == (member_name, member_discriminator):
             await ctx.guild.unban(user)
             await ctx.send(f"unbanned {user.mention}")

# ust this to change nicknames of users. In your discord server.


@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def chnick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@bot.command()
async def statusapi(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="ERROR", color=0xFF0000)
    embed.add_field(name="REQUEST ERROR",
                    value="Failed to establish a new connectionConnection refused", inline=True)
    embed.set_footer(text="ALLE SERVICES API REFUSED THE CONNECTION")
    await ctx.send(embed=embed)
    await ctx.send("https://tenor.com/view/lifeissohard-problems-life-homer-homer-simpson-gif-13342474")


@bot.command()
async def check(ctx, nameid):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
      async with cs.get('http://51.195.223.137/users?name={nameid}') as r:
        res = await r.json()
        await ctx.send(res)

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    await ctx.send('do u know this cat if so take it back NOW!!!')
    await ctx.send('https://media.discordapp.net/attachments/794887127086530570/803393677207535647/gnnhhnhg.png?width=485&height=595')



@bot.command()
async def convoy(ctx,  date1,  server2,  origin3,  destination4,  meet5,  depart6,  cars7,  trailers8,  notimezone, tmpeventspage):
    channel1 = bot.get_channel(800961728841908234)
    embed = discord.Embed(title="NEW ALLE GROUP CONVOY", color=0xFF0000)
    embed.add_field(name="date", value=date1, inline=False)
    embed.add_field(name="server", value=server2, inline=False)
    embed.add_field(name="origin", value=origin3, inline=False)
    embed.add_field(name="destination", value=destination4, inline=False)
    embed.add_field(name="meet", value=meet5, inline=False)
    embed.add_field(name="depart", value=depart6, inline=False)
    embed.add_field(name="cars", value=cars7, inline=False)
    embed.add_field(name="trailers", value=trailers8, inline=False)
    embed.add_field(name="no time zone link", value=notimezone, inline=False)
    embed.add_field(name="tmp events page link",
                    value=tmpeventspage, inline=False)
    await channel1.send(embed=embed)
    await ctx.send("convoy added / message sent")
    await ctx.message.delete()


@bot.command()
async def job(ctx):
    embed = discord.Embed(title="JOB COMPLETE", color=0xFF0000)
    embed.add_field(name="From", value="BETA", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def helpconvoy(ctx):
    await ctx.message.delete()
    await ctx.send("`?convoy 19/01/2021 sim-3 test-location test-location test-location 7pm no yes testing testing` the command structure is like this *** date, server, origin, destination, meet, depart, cars, trailers, no time zone link, tmp events page link. *** ` YOU MUST MAKE SURE TO HAVE IT IN THAT ORDER ` *** please have `-` between words e.g no-trailers-please ***")





@bot.command()
async def remove(ctx):
  await ctx.send("what do u want to remove from me i feel sad now :(")
bot.run(token, bot=True)
