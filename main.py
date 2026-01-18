import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
ROLE_ID = int(os.getenv('ROLE_ID')) # ID должен быть числом

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен через .env!')

@bot.event
async def on_member_join(member):
    role = member.guild.get_role(ROLE_ID)
    if role:
        try:
            await member.add_roles(role)
            print(f'Выдана роль новичка для {member.display_name}')
        except discord.Forbidden:
            print("Ошибка: Проверьте иерархию ролей!")
    else:
        print("Ошибка: ID роли в .env указан неверно.")

bot.run(TOKEN)
