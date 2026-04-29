import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot sudah online!")

import asyncio 

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel

        # kalau bot sudah connect, disconnect dulu
        if ctx.voice_client:
            await ctx.voice_client.disconnect()

        await ctx.send("Masuk ke voice...")

        await asyncio.sleep(2)  # delay biar stabil

        await channel.connect(reconnect=True)

        await ctx.send("Bot berhasil masuk voice!")
    else:
        await ctx.send("Kamu harus masuk voice dulu")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Keluar dari voice channel")

import os
bot.run(os.getenv("TOKEN"))