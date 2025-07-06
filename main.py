import discord
from discord.ext import commands, tasks
from typing import Optional
from discord import app_commands
from discord.ui import Select, View
from itertools import cycle
import logging
from dotenv import load_dotenv
import asyncio
import os 
import webserver

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():   
    await bot.change_presence(status=discord.Status.idle, activity=discord.CustomActivity(
        name="🧺 𝜗⁾𓈒 ᭙a𝕥chׁׅ֮ing̲ 𝕠vꫀr 𝕚gnɑׁׅ֮t &  ׄ   ⓗaꫀb𝕚ng"
    ))
    print("Bot is now online.")
    try:
        synced_commands = await bot.tree.sync()
        print("Commands synced.")
    except Exception as e:
        print("An error with syncing application commands has occured: ", e)

@bot.tree.command(name="rec", description="Use this command to recommend stories, such as manhwa, manga, manhua, or novels.")
@app_commands.describe(
    title='title',
    alt_title='title in korean/japanese/chinese',
    genre='genre it belongs to',
    type='manhwa, manga, manhua, or novel',
    plot='plot of the book',
    link='link to the book'
)
@app_commands.choices(type=[
    app_commands.Choice(name='manhwa', value='manhwa'),
    app_commands.Choice(name='manga', value='manga'),
    app_commands.Choice(name='manhua', value='manhua'),
    app_commands.Choice(name='novel', value='novel')
])
async def rec(interaction: discord.Interaction, 
                title: str, alt_title: str, genre: str, type: app_commands.Choice[str], plot: str, link: str):
    manhwa_channel = bot.get_channel(1381387295655202897)
    manga_channel = bot.get_channel(1381387295655202897)
    manhua_channel = bot.get_channel(1381387295655202897)
    novel_channel = bot.get_channel(1381387295655202897)
    if type.value == 'manhwa':
        channel = manhwa_channel
        await interaction.response.send_message(f"recommendation has been sent to {manhwa_channel.mention}", ephemeral=True) 
        await channel.send(
            f"_ _\n"
            f"ꆭ 𓏼**𝓂a__nwha__** re𝕔com__𝕖ndatⅈon__  <:fishhh:1382860704427671593>  ུ\n"
            f"_ _ ◟ཀ  ;  {title} ✿⸝⸝⸝\n"
            f"-# _ _   ̣̣̥ ༷ ಎ _ _ **{alt_title}** ꒰ ˃̶̤́ ꒳ ˂̶̤̀ ꒱\n"
            f"_ _\n"
            f"_ _  ൄ g𝕖__nr𝕖__ ; {genre} 。。\n"
            f"_ _ <:e_egg:1382854144057933888>  ꦿ 𝕡𝓁ot  ;  {plot} *!* 𓏼\n"
            f"_ _\n"
            f"_ _ ❀ [𝓁ⅈ__ꪀk__](<{link}>)  ׄ  //"
        )
    if type.value == 'manga':
        channel = manga_channel
        await interaction.response.send_message(f"recommendation has been sent to {manga_channel.mention}", ephemeral=True)
        await channel.send(
            f"_ _\n"
            f" ꆭ 𓏼**𝓂a__nga__** re𝕔com__𝕖ndatⅈon__  <:d_leafs:1382841507115172042>     ུ\n"
            f"_ _ ◟ཀ  ;  {title} ✿⸝⸝⸝\n"
            f"-# _ _   ̣̣̥ ༷ ಎ _ _ **{alt_title}** ꒰ ˃̶̤́ ꒳ ˂̶̤̀ ꒱\n"
            f"_ _\n"
            f"_ _  ൄ g𝕖__nr𝕖__ ; {genre} 。。\n"
            f"_ _ <:fishhh:1382860704427671593>    ꦿ 𝕡𝓁ot  ;  {plot} *!* 𓏼\n"
            f"_ _\n"
            f"_ _ ❀ [𝓁ⅈ__ꪀk__](<{link}>)  ׄ  //"
        )
    if type.value == 'manhua':
        channel = manhua_channel
        await interaction.response.send_message(f"recommendation has been sent to {manhua_channel.mention}", ephemeral=True)
        await channel.send(
            f"_ _\n"
            f" ꆭ 𓏼**𝓂a__nhua__** re𝕔com__𝕖ndatⅈon__  <:0001_red_animals:1382841512106262709>   ུ\n"
            f"_ _ ◟ཀ  ;  {title} ✿⸝⸝⸝\n"
            f"-# _ _   ̣̣̥ ༷ ಎ _ _ **{alt_title}** ꒰ ˃̶̤́ ꒳ ˂̶̤̀ ꒱\n"
            f"_ _\n"
            f"_ _  ൄ g𝕖__nr𝕖__ ; {genre} 。。\n"
            f"_ _ <:00_18:1390127795883085916>   ꦿ 𝕡𝓁ot  ;  {plot} *!* 𓏼\n"
            f"_ _\n"
            f"_ _ ❀ [𝓁ⅈ__ꪀk__](<{link}>)  ׄ  //"
        )
    if type.value == 'novel':
        channel = novel_channel
        await interaction.response.send_message(f"recommendation has been sent to {novel_channel.mention}", ephemeral=True)
        await channel.send(
            f"_ _\n"
            f" ꆭ 𓏼**𝘯o__vel__** re𝕔com__𝕖ndatⅈon__  <a:000_red_popstraw:1382841515251994666>      ུ\n"
            f"_ _ ◟ཀ  ;  {title} ✿⸝⸝⸝\n"
            f"-# _ _   ̣̣̥ ༷ ಎ _ _ **{alt_title}** ꒰ ˃̶̤́ ꒳ ˂̶̤̀ ꒱\n"
            f"_ _\n"
            f"_ _  ൄ g𝕖__nr𝕖__ ; {genre} 。。\n"
            f"_ _ <:006_splash:1374359958468038707>    ꦿ 𝕡𝓁ot  ;  {plot} *!* 𓏼\n"
            f"_ _\n"
            f"_ _ ❀ [𝓁ⅈ__ꪀk__](<{link}>)  ׄ  //"
        )
    else:
        await interaction.response.send_message("Invalid type selected. Please choose from manhwa, manga, manhua, or novel.", ephemeral=True)
        
webserver.keep_alive()
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
