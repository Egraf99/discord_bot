from datetime import datetime
from random import randint
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix=os.environ['prefix'])


@bot.event
async def on_ready():
    print('Bot gone')


@bot.command(pass_context=True)
async def идея(ctx, *args):
    
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
    print(os.environ['copy_id'])
    print(type(bot.get_channel(id=os.environ['copy_id'])))
    await bot.get_channel(id=os.environ['copy_id']).send('жду шоколадку и идея от {}'.format(ctx.message.author.mention))
    message = await bot.get_channel(id=os.environ['copy_id']).send(embed=emb)
    print(type(message))

    # add reactions
    await message.add_reaction('⬆')
    await message.add_reaction('⬇')

    # delete message
    await ctx.message.delete()
    

bot_token = os.environ['token']
bot.run(bot_token)
