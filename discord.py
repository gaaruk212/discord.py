import asyncio
import discord
from discord.ext import commands
import os


client = discord.Client()

token = "" # 자신의 디스코드 ID

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("") # 자유
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

if message.content.startswith("!채팅청소"):
        if (message.author.id == ): # 자신의 디스코드 ID
            try:
                amount = message.content[6:]
                await message.channel.purge(limit=int(amount))
                await message.channel.send(f"**{amount}**개의 메시지를 지웠습니다.")
            except ValueError:
                await message.channel.send("청소하실 메시지의 **수**를 입력해 주세요.")
        else:
            await message.channel.send("권한이 없습니다.")
            
if (message.content.startswith("!채팅")):
        if (message.author.id == ): # 자신의 디스코드 ID
            try:
                colour = message.content.split(" ")[1].split("\n")[0]
                content = message.content.split("\n")[1:]
                content = "\n".join(content)
                embed = discord.Embed(color=int("0x"+colour, 0), description=content)
                await message.channel.send(embed=embed)
                await message.delete()
            except:
                embed = discord.Embed(color=0xe81111, title="명령어 사용법", description="!채팅 (원하는 헥스 색상 코드)\n(공지를 원하는 내용)")
                await message.channel.send(embed=embed)
                
client.run(token)
