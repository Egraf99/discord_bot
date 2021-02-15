from datetime import datetime
from random import randint
from config import settings
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command(pass_context=True, aliases=['идея'])
async def __idea(ctx, *args):
    
    # choice random color of Embed
    col = randint(0, 16777215)

    # save send message
    desc = ''
    for mes in args:
        desc += mes + ' '

    # made Embed
    emb = discord.Embed(title='!идея', description=desc,
                        colour=col, timestamp=datetime.utcnow())
    emb.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)

    # send Embed to the other channel
    other_channel = bot.get_channel(id=settings['copy_id'])
    await other_channel.send(embed=emb)

    # delete message
    await ctx.message.delete()

bot.run(settings['token'])
