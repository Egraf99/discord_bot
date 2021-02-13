from random import randint
from config import settings
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command(pass_context=True)
async def идея(ctx, user: discord.User):
    col = randint(0, 16777215)
    emb = discord.Embed(title='Info about {}'.format(user.name), colour=col)
    emb.add_field(name='Name', value=user.name)
    await ctx.channel.send(embed=emb)
    await ctx.message.delete()

bot.run(settings['token'])
