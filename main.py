import discord
import os
import logging
import aiohttp
import time
import pymongo

import logging
import aiohttp
import time
import pymongo
import keep_alive
from disdiscordcord.ext import commands
from cogs.Antinuke import anti
from cogs.mod import Mod
from discord.ui import Button, Select, View



token = os.getenv('Tucan')


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(
  command_prefix=commands.when_mentioned_or("+"), 
  intents=intents,
  help_command=None
)
client.add_cog(anti(client))
client.add_cog(Mod(client))





@client.event
async def on_ready():
  print(f"Successfully Connected to {client.user}")


@client.event
async def on_connect():

  await client.change_presence(status=discord.Status.dnd, activity = discord.Game(f'>Help '))

@client.listen("on_guild_join")
async def foo(guild):
  for channel in guild.text_channels:
    invite = await channel.create_invite(max_age=0, max_uses=0)
  embed = discord.Embed(title="reverb joined a server!", color=discord.Colour.green())
  embed.add_field(name="*name*", value="`%s`" % (guild.name), inline=False)
  embed.add_field(name="*owner*", value="`%s`" % (guild.owner), inline=False)
  embed.add_field(name="*members*", value="`%s`" % (len(guild.members)), inline=False)
  embed.add_field(name="*invite*", value="[Invite](%s)" % (invite), inline=False)
  me = client.get_channel(932552983214977104)
  await me.send(embed=embed)




@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanalll(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send('Unbanning {} members'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user)


@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    
    await message.delete()
    embed = discord.Embed(title='R44ᴿᶜ', color=0x2f3136, description=f'**```yaml\nPING = {ping} ms ```**')
    embed.set_thumbnail(url='https://images.ctfassets.net/23aumh6u8s0i/2pxitsliEwXLe6LhXYrcBB/e17a6246514c9e1724fe2129857310fb/thief-2')
    await ctx.send(embed=embed)




keep_alive.keep_alive()
client.run(token)p_alive
from disdiscordcord.ext import commands
from cogs.Antinuke import anti
from cogs.mod import Mod
from discord.ui import Button, Select, View



token = os.getenv('Tucan')


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(
  command_prefix=commands.when_mentioned_or("+"), 
  intents=intents,
  help_command=None
)
client.add_cog(anti(client))
client.add_cog(Mod(client))





@client.event
async def on_ready():
  print(f"Successfully Connected to {client.user}")


@client.event
async def on_connect():

  await client.change_presence(status=discord.Status.dnd, activity = discord.Game(f'>Help '))

@client.listen("on_guild_join")
async def foo(guild):
  for channel in guild.text_channels:
    invite = await channel.create_invite(max_age=0, max_uses=0)
  embed = discord.Embed(title="reverb joined a server!", color=discord.Colour.green())
  embed.add_field(name="*name*", value="`%s`" % (guild.name), inline=False)
  embed.add_field(name="*owner*", value="`%s`" % (guild.owner), inline=False)
  embed.add_field(name="*members*", value="`%s`" % (len(guild.members)), inline=False)
  embed.add_field(name="*invite*", value="[Invite](%s)" % (invite), inline=False)
  me = client.get_channel(932552983214977104)
  await me.send(embed=embed)




@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanalll(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send('Unbanning {} members'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user)


@client.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    
    await message.delete()
    embed = discord.Embed(title='R44ᴿᶜ', color=0x2f3136, description=f'**```yaml\nPING = {ping} ms ```**')
    embed.set_thumbnail(url='https://images.ctfassets.net/23aumh6u8s0i/2pxitsliEwXLe6LhXYrcBB/e17a6246514c9e1724fe2129857310fb/thief-2')
    await ctx.send(embed=embed)




keep_alive.keep_alive()
client.run(token)