import discord
import random
from discord.ext import commands, tasks
from random import choice

client = commands.Bot(command_prefix='$')

status = ['kbhelp']
queue = []

@client.event
async def on_ready():
    change_status.start()
    print('The bot is online')

@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"Avatar of {member}")
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@client.command()
@commands.has_guild_permissions(ban_members=True)
async def kick(ctx, member:discord.Member=None, *, reason=None):

    if not member:#if member isnt mentioned
        await ctx.sendd("User isnt mentioned")

    await member.kick(reason=reason)
    await ctx.send(f"{member.name} kicked by {ctx.author}")

@client.command()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member:discord.Member=None, *, reason=None):

    if not member:#if member isnt mentioned
        await ctx.sendd("User isnt mentioned")

    await member.ban(reason=reason)
    await ctx.send(f"{member.name} Baned by {ctx.author}")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))


client.run('Nzg0NjcwNjM1ODg0MDE5NzIz.X8sreg._4LgrlqA7jupVspqKBV1d3CSpAQ')     