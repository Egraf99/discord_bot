from datetime import datetime
from random import randint
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='prefix')


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command(pass_context=True, aliases=['идея'])
async def __idea(ctx, *args):
    
    # choice random color of Embed
    col = randint(0, 16777215)

    # save send message
    idea = ''
    for mes in args:
        idea += mes + ' '

    # made Embed
    emb = discord.Embed(title=idea, description='!идея',
                        colour=col, timestamp=datetime.utcnow())
    emb.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)

    # send Embed with author to the other channel
    other_channel = bot.get_channel(id='copy_id')
    await other_channel.send('жду шоколадку и идея от {}'.format(ctx.message.author.name))
    message = await other_channel.send(embed=emb)

    # add reactions
    await message.add_reaction('⬆')
    await message.add_reaction('⬇')

    # delete message
    await ctx.message.delete()

token = os.environ.get('token')
bot.run(token)
