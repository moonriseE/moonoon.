import discord
from discord.ext import commands, tasks
from discord.ui import Button, View, Select
from discord import ButtonStyle, app_commands
from discord.utils import get
from datetime import datetime
from dotenv import load_dotenv
from pymongo import MongoClient
from config import load_work_data, save_work_data
import os
import json

# Загрузка переменных окружения
load_dotenv(".env")
token = os.getenv("TOKEN")
mongodb = os.getenv("MONGO")
cluster = MongoClient(mongodb)
usersdb = cluster.WN.members

# Инициализация бота
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.tree.fallback_to_global = False

@bot.tree.command(name="permission", description="for Maksim Postov")
async def perm(ctx: discord.Interaction, channel: discord.TextChannel):
    if ctx.user.id == 1153543540442406994:
        for i in channel.overwrites.keys():
            if i.id != 653925506076639242:
                perm = channel.overwrites_for(i)
                perm.use_application_commands = True
                await channel.set_permissions(target=i, overwrite=perm)


@bot.tree.command(name="testik", description="for Maksim Postov")
async def testik(ctx: discord.Interaction):
    if ctx.user.id == 1153543540442406994:
        with open("members.json", "r") as file:
            data = json.loads(file.read())
        no = []
        hum = [i["Паспорт"] for i in usersdb.find({}, {"Паспорт": 1})]
        print(hum)
        for i in data["members"]:
            if i["id"] in hum:
                continue
            memb = [
                member
                for member in ctx.guild.members
                if i["name"].replace("_", " ").lower() in member.display_name.lower()
            ]
            if memb == []:
                memb = [
                    member
                    for member in ctx.guild.members
                    if i["name"].lower() in member.display_name.lower()
                ]
                if memb != []:
                    print(i["name"])
                    usersdb.insert_one(
                        {
                            "_id": memb[0].id,
                            "Имя": i["name"].replace("_", " "),
                            "Паспорт": i["id"],
                        }
                    )
                else:
                    no.append(i["name"])
            else:
                print(i["name"])
                usersdb.insert_one(
                    {
                        "_id": memb[0].id,
                        "Имя": i["name"].replace("_", " "),
                        "Паспорт": i["id"],
                    }
                )
        print(no)


@bot.tree.command(name="testik1", description="for Maksim Postov")
async def testik1(ctx: discord.Interaction):
    global voice
    voice = get(bot.voice_clients, guild=ctx.guild)
    await voice.disconnect()




@bot.tree.command(
    name="перевод_отдел", description="Перевод пользователя в указанный отдел (роль)."
)
@app_commands.describe(пользователь="Пользователь", департамент="Отдел (роль)", причина="Причина")
async def transfer_dept(
    interaction: discord.Interaction, пользователь: discord.Member, департамент: discord.Role, причина: str
):
    member = пользователь
    department = департамент
    reason = причина
    # Проверка прав
    user_role_ids = [role.id for role in interaction.user.roles]
    allowed_roles = [
        914793194540130314,
        748098965660106822,
        653928670095736832,
        653928672381632532,
    ]
    if not any(rid in allowed_roles for rid in user_role_ids):
        await interaction.response.send_message(
            "У вас нет прав на использование этой команды.", ephemeral=True
        )
        return

    # Назначаем роль пользователю
    await member.add_roles(department)

    # Создаем Embed
    embed = discord.Embed(
        title="Перевод сотрудника",
        description="Данные о переводе",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Пользователь", value=member.mention, inline=False)
    embed.add_field(name="Новый отдел", value=department.mention, inline=False)
    embed.add_field(name="Причина", value=reason, inline=False)
    embed.add_field(name="Перевод выполнил", value=interaction.user.mention, inline=False)
    embed.set_footer(text=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    # Отправляем сообщение
    await interaction.response.send_message(content=f"{member.mention}", embed=embed)

    data = load_work_data()
        
    work_id = max([w["id"] for w in data["work"]], default=0) + 1

    message = await interaction.original_response()

    message_link = f"https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{message.id}"

    work_data = {
        "id": work_id,
        "category": "transfer_dept",
        "message_link": message_link,
        "user": str(interaction.user.id),
    }
    data["work"].append(work_data)
    save_work_data(data)

@bot.tree.command(
    name="вывод_отдел", description="Вывод пользователя из указанного отдела (роль)."
)
@app_commands.describe(пользователь="Пользователь", департамент="Отдел (роль)", причина="Причина")
async def transfer_vivod_dept(interaction: discord.Interaction, пользователь: discord.Member, департамент: discord.Role, причина: str):
    member = пользователь
    department = департамент
    reason = причина
    # Проверка прав
    user_role_ids = [role.id for role in interaction.user.roles]
    allowed_roles = [
        914793194540130314,
        748098965660106822,
        653928670095736832,
        653928672381632532,
    ]
    if not any(rid in allowed_roles for rid in user_role_ids):
        await interaction.response.send_message(
            "У вас нет прав на использование этой команды.", ephemeral=True
        )
        return

    # Назначаем роль пользователю
    await member.remove_roles(department)

    # Создаем Embed
    embed = discord.Embed(
        title="Вывод сотрудника",
        description="Данные о выводе",
        color=discord.Color.blue(),
    )
    embed.add_field(name="Пользователь", value=member.mention, inline=False)
    embed.add_field(name="Отдел", value=department.mention, inline=False)
    embed.add_field(name="Причина", value=reason, inline=False)
    embed.add_field(name="Вывод выполнил", value=interaction.user.mention, inline=False)
    embed.set_footer(text=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    # Отправляем сообщение
    await interaction.response.send_message(content=f"{member.mention}", embed=embed)

    message = await interaction.original_response()

    message_link = f"https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{message.id}"

    data = load_work_data()
        
    work_id = max([w["id"] for w in data["work"]], default=0) + 1
    
    work_data = {
        "id": work_id,
        "category": "transfer_vivod_dept",
        "message_link": message_link,
        "user": str(interaction.user.id),
    }
    data["work"].append(work_data)
    save_work_data(data)


async def unload_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                await bot.unload_extension(f"cogs.{filename[:-3]}")
            except:
                pass

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Загружен {filename[:-3]}")

@bot.tree.command(name="reload_cogs", description="Перезагрузка Когов")
async def reload_cogs(interaction: discord.Interaction):
    if interaction.user.id in [763731794200625172, 653167765347106829]:
        await unload_cogs()
        await load_cogs()
        # for guild in bot.guilds:
        #     bot.tree.clear_commands(guild=discord.Object(id=guild.id))
        #     bot.tree.copy_global_to(guild=discord.Object(id=guild.id))
        #     bot.tree.clear_commands(guild=discord.Object(id=guild.id))
        #     await bot.tree.sync(guild=discord.Object(id=guild.id))
        await bot.tree.sync()
        await interaction.response.send_message("Коги успешно перезагружены!", ephemeral=True)

@bot.event
async def on_ready():
    print("Бот запущен!")
    await load_cogs()
    for guild in bot.guilds:
        with open("channels.json") as file:
            data = json.load(file)
        if str(guild.id) not in data:
            with open("channels.json", "w") as file:
                data[str(guild.id)] = {}
                json.dump(data, file, indent=4)
        # bot.tree.clear_commands(guild=discord.Object(id=guild.id))
        # bot.tree.copy_global_to(guild=discord.Object(id=guild.id))
    await bot.tree.sync()
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="Lofi Hip Hop",
        ),
    )


@bot.event
async def on_resumed():
    # print("on_resumed")
    try:
        await load_cogs()
    except:
        pass
    for guild in bot.guilds:
        with open("channels.json") as file:
            data = json.load(file)
        if str(guild.id) not in data:
            with open("channels.json", "w") as file:
                data[str(guild.id)] = {}
                json.dump(data, file, indent=4)
    await bot.tree.sync()
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="Lofi Hip Hop",
        ),
    )
    print("Бот продолжает работу!")


@bot.event
async def on_guild_join(guild):
    # bot.tree.copy_global_to(guild=discord.Object(id=guild.id))
    await bot.tree.sync(guild=discord.Object(id=guild.id))
    with open("channels.json") as file:
        data = json.load(file)
    with open("channels.json", "w") as file:
        data[str(guild.id)] = {}
        json.dump(data, file, indent=4)
    # await create_privates(guild, "ru")


@bot.event
async def on_guild_leave(guild):
    with open("channels.json") as file:
        data = json.load(file)
    with open("channels.json", "w") as file:
        del data[str(guild.id)]
        json.dump(data, file, indent=4)


bot.run(token)