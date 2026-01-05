import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# WEB SERVER (UYKU ENGELLEME)
app = Flask('')

@app.route('/')
def home():
    return "Bot aktif."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.event
async def on_ready():
    print(f'{bot.user} aktif.')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

keep_alive()
bot.run(os.getenv("TOKEN"))

