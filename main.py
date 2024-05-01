import json
import random
import datetime
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1223523951184183359)

    wlc = discord.Embed(title=f"Welcome", description="", color=0x00ff00)
    wlc.add_field(f'{member.mention}, I\'m an (somewhat) automated bot created by Yui. Use ".help" to get information from Yui. I\'ll post and track Yui\'s status. Which you can view in #yui-gps .')
    wlc.timestamp = datetime.datetime.now()
    wlc.set_footer(text='\u200b',icon_url="https://m.media-amazon.com/images/M/MV5BODk4N2UzNTAtZDU1ZS00MWJhLTk1ZmQtMzM5MmMxZTFlZWJjXkEyXkFqcGdeQXVyODc5MTI0NjU@._V1_.jpg")

    if (member.id == 1008106406693589123):
        await channel.send(embed=wlc)

@bot.event
async def on_message(message):
    channel = bot.get_channel(1224406730247634978)

    if (message.channel == channel):
        member = bot.get_user(1178112208991957086)
        await member.send(message.content)

    await bot.process_commands(message)

@bot.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    await gps()

@bot.command(aliases = ['upd'])
async def update(ctx):
    with open('/jfs/log.json', 'r') as json_File:
        lf = json.load(json_File)
 
    lid = lf['logs']
    lido = lid[0].values()
    log = list(lido)[0]

    upd = discord.Embed(title="", description="", color=0x00ff00)
    upd.add_field(name=f"Patch Notes", value=log, inline=False)
    upd.timestamp = datetime.datetime.now()
    upd.set_footer(text='\u200b',icon_url="https://m.media-amazon.com/images/M/MV5BODk4N2UzNTAtZDU1ZS00MWJhLTk1ZmQtMzM5MmMxZTFlZWJjXkEyXkFqcGdeQXVyODc5MTI0NjU@._V1_.jpg")

    await ctx.reply(embed=upd)
    await ctx.message.delete()

@bot.command(aliases = ['gw'])
async def guesswhat(ctx):
    gwra = random.randint(0, 12)

    with open('/ra/gwa.json', 'r') as json_File:
        gwf = json.load(json_File)
 
    gwd = gwf['answers']
    gwo = gwd[0].values()  
    log = list(gwo)[gwra]

    gw = discord.Embed(title="", description="", color=0xFFC0CB)
    gw.add_field(name="Guess what...", value=log, inline=False)
    gw.timestamp = datetime.datetime.now()
    gw.set_footer(text='\u200b',icon_url="https://m.media-amazon.com/images/M/MV5BODk4N2UzNTAtZDU1ZS00MWJhLTk1ZmQtMzM5MmMxZTFlZWJjXkEyXkFqcGdeQXVyODc5MTI0NjU@._V1_.jpg")
    
    await ctx.reply(embed=gw)
    await ctx.message.delete()

@bot.command(aliases = ['hm'])
async def h(ctx):
    with open('/cmds/cl.json', 'r') as json_File:
        cf = json.load(json_File)
 
    cld = cf['commands']
    cldo = cld[0].values()
    cl = list(cldo)[0]
    cl2 = list(cldo)[1]
    cl3 = list(cldo)[2]

    cmdl = discord.Embed(title="Yui\'s Command List", description="Command prefix is '.'", color=0x00ff00)
    cmdl.add_field(name=cl, value='Shows a list of commands.', inline=False)
    cmdl.add_field(name=cl2, value='Gives the latest patch notes.', inline=False)
    cmdl.add_field(name=cl3, value='A game of guess what.', inline=False)
    cmdl.timestamp = datetime.datetime.now()
    cmdl.set_footer(text='\u200b',icon_url="https://m.media-amazon.com/images/M/MV5BODk4N2UzNTAtZDU1ZS00MWJhLTk1ZmQtMzM5MmMxZTFlZWJjXkEyXkFqcGdeQXVyODc5MTI0NjU@._V1_.jpg")

    await ctx.reply(embed=cmdl)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def p(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

async def gps():
    channel = bot.get_channel(1223538641641668688)
    member = bot.get_guild(1223523951184183356).get_member(1178112208991957086)
    clr = ''
    activity = ''
    stts = member.status.name

    if (member.activity == None):
        activity = 'None'
    
    else:
        activity = member.activity.name

    if (stts == 'offline'):
        clr = int(0x808080)

    if (stts == 'online'):
        clr = int(0x00ff00)

    if (stts == 'idle'):
        clr = int(0xfbf07b)

    if (stts == 'dnd'):
        clr = int(0xFF0000)

    stat = discord.Embed(title="", description="", color=clr)
    stat.add_field(name="Status", value=f'{member.status.name}', inline=False)
    stat.add_field(name="Activity", value=f'Playing {activity}', inline=False)
    stat.timestamp = datetime.datetime.now()
    stat.set_footer(text='\u200b',icon_url="https://m.media-amazon.com/images/M/MV5BODk4N2UzNTAtZDU1ZS00MWJhLTk1ZmQtMzM5MmMxZTFlZWJjXkEyXkFqcGdeQXVyODc5MTI0NjU@._V1_.jpg")
    
    await channel.send(embed=stat)

bot.run("MTIwNTk2OTYwMjI0MTM2ODE2NA.GBtb22.D97MwEmR3I4PqJJ1H-vhM-oECQAVl5Lk9fVKnU")
