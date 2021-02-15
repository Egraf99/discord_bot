import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.command(pass_context=True)
async def info(ctx, user: discord.User):
    emb = discord.Embed(title='Info about {}'.format(user.name))
    emb.add_field(name='Name', value=user.name)
    await ctx.channel.send(embed=emb)

bot.run('#your_token')
