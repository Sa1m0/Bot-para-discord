# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='-', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def no(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def si(ctx, left: int, right: int):
    await ctx.send(left / right)


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def consejo(ctx):
    lista = ["Uso del transporte público y utilización del coche privado solo cuando sea completamente necesario" ,
            "Elegir, a la hora de comprar un carro, un modelo de bajo consumo energético",
            "todo desplazamiento que se pueda realizar en bicicleta o andando es menos contaminante que cualquier coche",
            "Usar espráis que sean respetuosos con el medio ambiente y no generen gases invernadero"]
    await ctx.send(random.choise(lista))

@bot.command()
async def videos(ctx):
    reels = ["https://www.youtube.com/watch?v=GLTCiS6hOT4", "https://www.youtube.com/watch?v=GQdx0OKuEKw"] 
    await ctx.send(random.choise(reels))

@bot.command()
async def mem(ctx):

    imagen = random.choise(os.listdir("IMGS"))

    with open(f'IMGS/{imagen}', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.')

 


bot.run('TOKEN')




"""
comandos = mem, cool, repeat,choose, roll, si, no, add 
"""
