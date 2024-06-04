import requests
import json
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, case_insensitive=True)

run = 'TOKEN'
channel_id = # channel id
# API
# https://api.discord.gx.games/v1/direct-fulfillment

async def handle_response(user_message, ctx):
    msg = user_message.lower()

    if msg == '.get':
        headers = {
            'authority': 'api.discord.gx.games',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://www.opera.com',
            'referer': 'https://www.opera.com/',
            'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
        }

        json_data = {
            'partnerUserId': 'd55845c6ce4778a1dfc73120c66b44321e82066b47a5cd4fb30cba8e021ca184',
        }

        response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data)

        data = json.loads(response.content)

        if (data['token'] is not None):
            token = data['token']
            template = 'https://discord.com/billing/partner-promotions/1180231712274387115/' + token
            await ctx.channel.send(f'Intro link: {template} ')
            print("Success!")
    elif msg == '.how':
        await ctx.channel.send('Send ```.get``` to get free intro. And send ```.info``` to know more about me.')
    
    elif msg == '.info':
        await ctx.channel.send('This bot was created by Vince, thanks to Opera GX. And this bot gives you a free intro if and only if you never had intro for the last 12 months. Sadly, this needs a valid credit card. Also, don\'t forget to cancel it.')

@bot.command()
async def get(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("This command can only be used in a server.")
        return
    
    username = str(ctx.message.author)
    user_message = str(ctx.message.content)
    channel = str(ctx.message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    await handle_response(ctx.message.content, ctx)

@bot.command()
async def how(ctx):
    
    username = str(ctx.message.author)
    user_message = str(ctx.message.content)
    channel = str(ctx.message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    await handle_response(ctx.message.content, ctx)

@bot.command()
async def info(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send("This command can only be used in a server.")
        return
    
    username = str(ctx.message.author)
    user_message = str(ctx.message.content)
    channel = str(ctx.message.channel)

    print(f"{username} said: '{user_message}' ({channel})")

    await handle_response(ctx.message.content, ctx)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == 1187404132814950450:
        if message.content.startswith(('.get', '.how', '.info')):
            print(message.content)
            await bot.process_commands(message)

bot.run(run)