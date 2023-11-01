from typing import Optional
import discord
from discord.ui import Button, View
from discord.ext import commands
import os
import asyncio

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.sync_commands()
    await client.tree.sync()
    print("Success: Bot is conencted to Discord")
    await buttonmenu_command_example()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
             await client.load_extension(f"cogs.{filename[:-3]}")

async def buttonmenu_command_example():
    dummy_interaction = discord.Integration()
    dummy_interaction.user = client.suer

async def async_mock(*args, **kwargs):
    pass

async def dummy_send_message(content, view):
    print(f"/verify")

class ReportModal(discord.ui.Modal, title="กรอกข้อมูลรับไวริส"):
    user_steam = discord.ui.TextInput(label="ลิ้งค์ STEAM", placeholder="eg. https://steamcommunity.com/id/@name/", required=True, max_length=100, style=discord.TextStyle.short)
    user_nameic = discord.ui.TextInput(label="ชื่อ-นามสกุล IC", placeholder="eg. ชื่อ นามสกุล", required=True, max_length=100, style=discord.TextStyle.short)
    user_oc = discord.ui.TextInput(label="อายุ oc", placeholder="eg. อายุ", required=True, max_length=100, style=discord.TextStyle.short)
    user_social = discord.ui.TextInput(label="ลิ้งค์เฟส IC หรือ OC", placeholder="eg. www.facebool.com/@name", required=True, max_length=100, style=discord.TextStyle.short)
    user_whoareyou = discord.ui.TextInput(label="รู้จักเซิร์ฟเวอร์นี้จากไหน", placeholder="eg. บอกเราได้เลยไว้มีกิจกรรมมาให้เล่นค้าบ", required=True,min_length=10, max_length=100, style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"<a:73b:1155924549699911761>: **__ห้ามส่งซ้ำ__** \n <:71a:1155924277959344168>: คุณ{interaction.user.mention}ได้กรอกข้อมูลเรียบร้อยแล้ว \n <:71a:1155924277959344168>: รอทาง <@&1151758322396037130> ตรวจสอบและให้ยศ <a:22bblue:1157225184743395328><@&1152842229644275753>", ephemeral=True)
        channel = discord.utils.get(interaction.guild.channels, name="NAME_ID_ROOM")
        await channel.send(f"**ส่งโดย:** {interaction.user.mention} \n **ชื่อ IC:** {self.user_nameic} \n **อายุ OC:** {self.user_oc} \n **รู้จักเซิร์ฟนี้จาก:** {self.user_whoareyou} \n **Facebook:** {self.user_social} \n **STEAM LINK:** {self.user_steam}")

class TestMenoButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="กดปุ่มกรอกฟอร์มเพื่อรับ WHITELIST", style=discord.ButtonStyle.red, emoji="📘")
    async def test(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(ReportModal())

@client.command()
async def verify(ctx):
    await ctx.send(content="https://cdn.discordapp.com/attachments/1152852129300631612/1155927245051932832/Ads_LOGO_OceanTown.png?ex=65492a23&is=6536b523&hm=a24a83dc0b481c8c75d11ead98cce61dfc412d7fd190fdf4768e4c5dc99f7523&", view=TestMenoButton())

async def main():
    async with client:
        await load()
        await client.start("YOUR_TOKEN_BOT")

asyncio.run(main())
