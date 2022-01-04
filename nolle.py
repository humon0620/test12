import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time
import random

bot = commands.Bot(command_prefix='!')

access_token = os.environ{'BOT_TOKEN'}


# 봇이 구동되었을 때 보여지는 코드
@bot.event
async def on_ready():
    print("노오오오에엘~")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(status=discord.Status.online, activity=None)

# 봇이 특정 메세지를 받고 인식하는 코드
@bot.command()
async def 입장(ctx):
    global vc
    await ctx.channel.send('부르셨습니까. 주인님')
    vc=await ctx.message.author.voice.channel.connect()

@bot.command()
async def 도움말(ctx):
    await ctx.channel.send('!입장 (통방 입장)\n!퇴장 (통방 퇴장)\n!공연시작 <링크>\n!룰렛\n!가챠룰렛\n원신출첵링크 https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ko-kr\n허락 받고 타 서버에서 사용해주세요.\n제작자 : 어스#9276 , kani#0842 (문의, 허락)')

@bot.command()
async def 룰렛(ctx):
    await ctx.channel.send('또 도박인가요....?(도박중독신고는 1336)')
    time.sleep(3)
    menu = '1000원','1000원','1000원','1000원','1000원','1000원','1000원','1000원','1000원','1000원', '5000원','5000원','5000원','5000원','5000원','5000원','5000원', '10000만원','10000만원','10000만원','10000만원','10000만원', '50000원','50000원','50000원','100000원(당첨!!)'
    msg = random.choice(menu)
    await ctx.channel.send('결과입니다 주인님:'+msg)

@bot.command()
async def 가챠룰렛(ctx):
    await ctx.channel.send('오늘 가챠를 할지 말지 정해달라구요?')
    time.sleep(2)
    await ctx.channel.send('음.....')
    time.sleep(2)
    menu2 = '한번 해보세요! 오늘 운이 좋으신것같으니!', '오늘은 날이 아닌것같아요..'
    msg2 = random.choice(menu2)
    await ctx.channel.send(msg2)

@bot.command()
async def 퇴장(ctx):
    await ctx.channel.send('저는 이만 가보겠습니다.')
    await vc.disconnect()

@bot.command()
async def 공연시작(ctx, *, url):
    await ctx.channel.send('공연을 시작하겠습니다.')
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']
    vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        
bot.run(access_token)
