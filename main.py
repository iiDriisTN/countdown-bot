from discord.ext import commands
import discord
import os
from datetime import datetime , timedelta
from dotenv import load_dotenv
import asyncio

# bdl .env 9bl

load_dotenv()

ramadhan = datetime(2024, 6, 1, 10, 0, 0) #yyyy , mm/m , dd/d , hh/h , mm/m , ss/s
still = timedelta()
async def check_ramadan(): # async function t7sb kl 1 sec 9adeh mzl.
    global still
    while not bot.is_closed():
        now = datetime.now()
        still = ramadhan - now
        days, hours, minutes, seconds = still.days, still.seconds // 3600, (still.seconds // 60) % 60 , still.seconds % 60
        activity_status = f"end of school is in: {days} days, {hours} hours, {minutes} minutes."
        await bot.change_presence(activity=discord.Game(name=activity_status))
        await asyncio.sleep(1)


TOKEN = os.getenv("DISCORD_TOKEN")

activity = discord.Game(name=f"end of school is in : {still}")
bot = commands.Bot(command_prefix=os.getenv("COMMAND_PREFEX"),intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected!')
    bot.loop.create_task(check_ramadan()) # task bch ybdeh

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)

@bot.command(name='9', help='see how many days still')
async def r(ctx):
    try:
        days, hours, minutes, seconds = still.days, still.seconds // 3600, (still.seconds // 60) % 60 , still.seconds % 60
        await ctx.send(f"mazel is in: {days} days, {hours} hours, {minutes} minutes , {seconds} seconds.")
    except NameError:
        await ctx.send("Error: Still variable not defined.")

bot.run(TOKEN)