from discord.ext import commands 
from discord.ext.commands import has_permissions
import os 
import discord 
import discord.ui
#import interactions 

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def hello(ctx):
  await ctx.send("I can respond")

@bot.command()
async def button(ctx):
  view = discord.ui.View()
  button = discord.ui.Button(label="test")
  view.add_item(button)
  await ctx.send(view=view)


@bot.command()
async def ben10(ctx):
  view = discord.ui.View()
  button = discord.ui.Button(label="it's hero time", style=discord.ButtonStyle.url, url="https://www.youtube.com/watch?v=_iIUGEOreiw&ab_channel=Ben10Petya")
  view.add_item(button)
  await ctx.send(view=view)


@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  channel = bot.get_channel(981973830325116998)
  pingmention = member.mention
  await ctx.send("Kicked " + pingmention)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to do this")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  channel = bot.get_channel(981973830325116998)
  pingmention = member.mention
  await ctx.send("Banned " + pingmention)

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to do this")


@bot.command()
async def avatar(ctx, member: discord.Member = None):
  if member == None: 
    member = ctx.author

  embed = discord.Embed(title = member).set_image(url = member.avatar.url)
  await ctx.send(embed = embed)


#async def on_message(message):
  #if message.author == bot.user:
    #return
  
  #if message.content == "its hero time" or "Its hero time" or "It's hero time" or "it's hero time" or "hero time" or "ben 10":
    #await message.channel.send("https://tenor.com/view/ben10-four-arms-transformation-omnitrix-gif-16594499")

password = os.environ['password']
bot.run(password)