import os
import discord
import stdin
import random
from discord.ext import commands

bot = discord.ext.commands.Bot(command_prefix = "!");


@bot.event
async def on_ready():
    print('Bot online.')


@bot.command(case_insensitive = True, aliases = ["remind", "reminder"])
@commands.bot_has_permissions(attach_files = True, embed_links = True)
async def on_message1(ctx, time, *, reminder):
    print(time)
    print(reminder)
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    else:  
        await ctx.send(f"Alright, I will remind you about {reminder} in {time}.")
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    else:
        await asyncio.sleep(seconds)
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
        await ctx.send(f"Hi, you asked me to remind you about {reminder} {counter} ago.")
        await ctx.send(embed=embed)


bot.run('OTA0Njg4MDU5NTQ1Njk0MzE4.YX_KaQ.OOaaV4qer28WQ9qlYwNgcATf0G0')