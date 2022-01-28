import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('Hallo'):
    await message.channel.send("Halihalo")

  if msg.startswith('Hoi'):
    await message.channel.send("Hoi was machsch?")

  if msg.startswith('Salü'):
    await message.channel.send("Bonjour, c'est le bot et je peux parler français. que fais-tu dans la vie ?")

  if msg.startswith('Salut'):
    await message.channel.send("Hallo, hier was zum singen --> https://youtu.be/9Pi--KQUzqI")

  if msg.startswith('Hilfe'):
    await message.channel.send("Du brauchts Hilfe? Der Bot ist ganz einfach. Er kann nur Halihalo sagen. \r\n"
    "Wenn du hallo schreibst, schreibt der Bot Halihalo.")

keep_alive()
client.run(os.getenv('TOKEN'))