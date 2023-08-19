import discord
from discord.ext import commands
import requests
import time
import random
from options import *


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.command()
async def randomcat(ctx):
    await ctx.send("Обработка...")
    time.sleep(4)
    await ctx.send(urlcat2)
    
@bot.command()
async def randomdog(ctx):
    await ctx.send("Обработка...")
    req = requests.get(urldog)
    data = req.json()
    time.sleep(1)
    await ctx.message.delete()
    await ctx.send(data['fileSizeBytes'])
    await ctx.send(data['url'])
    
@bot.command()
async def yesorno(ctx):
    await ctx.send("Обработка...")
    req = requests.get(yesno)
    data = req.json()
    await ctx.send('Ответ:')
    await ctx.send(data['answer'])
    await ctx.send(data['image'])

@bot.command()
async def site(ctx):
    await ctx.send("verilest.github.io")
    
@bot.command()
async def question(ctx):
    await ctx.send("Обработка...")
    time.sleep(1)
    await ctx.send("Данный API работает на Английском языке")
    req = requests.get(urlquestion)
    data = req.json()
    await ctx.send('Вопрос:')
    await ctx.send(data[0]['question'])
    time.sleep(2)
    await ctx.send('Ответ:')
    await ctx.send(data[0]['answer'])
    
@bot.command()
async def imbored(ctx):
    await ctx.send("Обработка...")
    time.sleep(1)
    await ctx.send('Данный API работает на Английском языке')
    req = requests.get(urlbored)
    data = req.json()
    await ctx.send('Тип активности:')
    await ctx.send(data['type'])
    await ctx.send('Активность:')
    await ctx.send(data['activity'])
    
@bot.command()
async def randomcount(ctx):
    await ctx.send("Обработка...")
    time.sleep(2)
    await ctx.send(random.randint(0, 1000))
    
@bot.command()
async def randomcity(ctx):
    await ctx.send('Обработка...')
    time.sleep(2)
    await ctx.send(random.choice(city_list))

@bot.command()
async def randomceed(ctx):
    await ctx.send('Обработка...')
    time.sleep(2)
    await ctx.send(random.random())

@bot.command()
async def help(ctx):
    await ctx.send("Вот что умею:")
    await ctx.send("Могу показать картинку кота/кошки командой !randomcat")
    await ctx.send("Могу показать картинку собаки командой !randomdog")
    await ctx.send("Могу ответить на вопрос да или нет? Командой !yesorno")
    await ctx.send("Могу показать случайный город, командой !randomcity")
    await ctx.send("Могу сгенерировать случайное число (от 0 до 10000), командой !randomcount")
    await ctx.send("Могу сгенерировать любое 'семя' (seed), командой !randomseed")
    await ctx.send("Могу придумать чем заняться, командой !imbored (В работе сервиса наблюдаются сбои, если бот не ответил попробуйте еще раз)")
    await ctx.send("Могу придумать вопрос и ответ к нему, командой !question (В работе сервиса наблюдаются сбои, если бот не ответил попробуйте еще раз)")
    await ctx.send("Вот что я умею: !Help")
    await ctx.send("Если бот не ответил после обработки команды, значит произошла ошибка, повторите попытку.")
    

    await ctx.send("--")
    await ctx.send("Бот сделан Mr.Veriller#7995")
    
bot.run(TOKEN)
