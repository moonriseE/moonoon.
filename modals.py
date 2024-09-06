import discord
import traceback
import json
from datetime import datetime


class Accept_Redaction(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Принять в редакцию", *args, **kwargs)
        self.name = discord.ui.TextInput(
            label="Имя Фамилия | Паспорт",
        )
        self.reason = discord.ui.TextInput(
            label="Причина принятия / увольнения:"
        )
        self.date = discord.ui.TextInput(
            label="Дата:"
        )

        self.add_item(self.name)
        self.add_item(self.reason)
        self.add_item(self.date)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "accept-redaction" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["accept-redaction"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на принятие в редакцию №{message_count}", color=0xDC143C
            )
            embed.add_field(
                name="Тема:", value="Принять в редакцию", inline=False
            )
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.reason.label,
                value=self.reason.value,
                inline=False,
            )
            embed.add_field(
                name=self.date.label,
                value=self.date.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Promote_1_to_2(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Повыситься с 1 на 2 ранг", *args, **kwargs)
        self.name = discord.ui.TextInput(
            label="Имя Фамилия",
        )
        self.regulations = discord.ui.TextInput(
            label="Сдача Устава:",
            placeholder='(Сообщение сотрудника HRD") imgur.com / yapx.ru',
        )
        self.end_rp_mission = discord.ui.TextInput(
            label="Завершенное RP-задании:",
            placeholder="(Скриншоты отыгровок) imgur.com / yapx.ru",
        )
        self.stay = discord.ui.TextInput(
            label="Отстояли определенное время за ресепшеном:",
            placeholder="imgur.com / yapx.ru",
        )

        self.add_item(self.name)
        self.add_item(self.regulations)
        self.add_item(self.end_rp_mission)
        self.add_item(self.stay)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "internship" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["internship"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(
                name="Тема:", value="Повыситься с 1 на 2 ранг", inline=False
            )
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.regulations.label,
                value=self.regulations.value,
                inline=False,
            )
            embed.add_field(
                name=self.end_rp_mission.label,
                value=self.end_rp_mission.value,
                inline=False,
            )
            embed.add_field(
                name=self.stay.label,
                value=self.stay.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Promote_2_to_3(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Повыситься с 2 на 3 ранг", *args, **kwargs)
        self.name = discord.ui.TextInput(
            label="Имя Фамилия / Дата заполнения отчета:",
        )
        self.ppo = discord.ui.TextInput(
            label="Сдача ППО-ПРО:",
            placeholder="(Сообщение сотрудника HRD) imgur.com / yapx.ru",
        )
        self.end_rp_mission = discord.ui.TextInput(
            label="Завершенное RP-задание:",
            placeholder="(Скриншоты отыгровок) imgur.com / yapx.ru",
        )
        self.stay = discord.ui.TextInput(
            label="Отстояли определенное время за ресепшеном:",
            placeholder="imgur.com / yapx.ru",
        )
        self.distribution = discord.ui.TextInput(
            label="Раздача листовок:",
            placeholder="imgur.com / yapx.ru",
        )

        self.add_item(self.name)
        self.add_item(self.ppo)
        self.add_item(self.end_rp_mission)
        self.add_item(self.stay)
        self.add_item(self.distribution)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "internship" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["internship"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(
                name="Тема:", value="Повыситься с 2 на 3 ранг", inline=False
            )
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.ppo.label,
                value=self.ppo.value,
                inline=False,
            )
            embed.add_field(
                name=self.end_rp_mission.label,
                value=self.end_rp_mission.value,
                inline=False,
            )
            embed.add_field(
                name=self.stay.label,
                value=self.stay.value,
                inline=False,
            )
            embed.add_field(
                name=self.distribution.label,
                value=self.distribution.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Human_Resources_Department(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Human Resources Department", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия / Ваша должность:")
        self.ppo = discord.ui.TextInput(
            label="Принятие Устава и ППО-ПРО:",
            placeholder='(Сообщение в канале "отчёты-по-экзаменам") https://imgur.com/',
        )
        self.people = discord.ui.TextInput(
            label="Принятие людей по заявкам:",
            placeholder="https://imgur.com/",
        )
        self.set_people = discord.ui.TextInput(
            label="Присутствие на открытом наборе и МП/ГМП",
            placeholder="https://imgur.com/",
        )
        self.otchet = discord.ui.TextInput(
            label="Дата заполнения отчета/последнего повышения:",
            placeholder="https://imgur.com/",
        )

        self.add_item(self.name)
        self.add_item(self.ppo)
        self.add_item(self.people)
        self.add_item(self.set_people)
        self.add_item(self.otchet)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "hrd" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["hrd"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(
                name="Тема:", value="Human Resources Department", inline=False
            )
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.ppo.label,
                value=self.ppo.value,
                inline=False,
            )
            embed.add_field(
                name=self.people.label,
                value=self.people.value,
                inline=False,
            )
            embed.add_field(
                name=self.set_people.label,
                value=self.set_people.value,
                inline=False,
            )
            embed.add_field(
                name=self.otchet.label,
                value=self.otchet.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class News_Room(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="News Room", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия / Ваша должность:")
        self.date = discord.ui.TextInput(
            label="Дата заполнения отчета/последнего повышения:"
        )
        self.work1 = discord.ui.TextInput(
            label="Доказательства проделанной работы №1\nСтатьи:",
            placeholder="https://imgur.com/",
        )
        self.work2 = discord.ui.TextInput(
            label="Доказательства проделанной работы №2\nМП/ГМП:",
            placeholder="https://imgur.com/",
        )
        self.work3 = discord.ui.TextInput(
            label="Доказательства проделанной работы №3:",
            placeholder="https://imgur.com/",
        )

        self.add_item(self.name)
        self.add_item(self.date)
        self.add_item(self.work1)
        self.add_item(self.work2)
        self.add_item(self.work3)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "nr" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["nr"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="News Room", inline=False)
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.date.label,
                value=self.date.value,
                inline=False,
            )
            embed.add_field(
                name=self.work1.label,
                value=self.work1.value,
                inline=False,
            )
            embed.add_field(
                name=self.work2.label,
                value=self.work2.value,
                inline=False,
            )
            embed.add_field(
                name=self.work3.label,
                value=self.work3.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Event_Department(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Event Department", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия:")
        self.job = discord.ui.TextInput(label="Ваша текущая должность:")
        self.date = discord.ui.TextInput(label="Дата последнего повышения:")
        self.work = discord.ui.TextInput(
            label="Все скриншоты о проделанной работе:",
            placeholder="https://imgur.com/",
        )

        self.add_item(self.name)
        self.add_item(self.job)
        self.add_item(self.date)
        self.add_item(self.work)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "ed" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["ed"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="Event Department", inline=False)
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.job.label,
                value=self.job.value,
                inline=False,
            )
            embed.add_field(
                name=self.date.label,
                value=self.date.value,
                inline=False,
            )
            embed.add_field(
                name=self.work.label,
                value=self.work.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Public_Relations(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Public Relations", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия / Ваша текущая должность:")
        self.date = discord.ui.TextInput(label="Дата последнего повышения:")
        self.efir = discord.ui.TextInput(label="Эфиры:")
        self.contract = discord.ui.TextInput(label="Контракты:")
        self.screenshots = discord.ui.TextInput(
            label="Все скриншоты о проделанной работе:",
            placeholder="https://imgur.com/",
        )

        self.add_item(self.name)
        self.add_item(self.date)
        self.add_item(self.efir)
        self.add_item(self.contract)
        self.add_item(self.screenshots)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "pr" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["pr"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="Public Relations", inline=False)
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.date.label,
                value=self.date.value,
                inline=False,
            )
            embed.add_field(
                name=self.efir.label,
                value=self.efir.value,
                inline=False,
            )
            embed.add_field(
                name=self.contract.label,
                value=self.contract.value,
                inline=False,
            )
            embed.add_field(
                name=self.screenshots.label,
                value=self.screenshots.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Media(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Media", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия:")
        self.job = discord.ui.TextInput(label="Ваша текущая должность:")
        self.screenshots = discord.ui.TextInput(
            label="Все скриншоты о проделанной работе:",
            placeholder="https://imgur.com/",
        )
        self.date_otchet = discord.ui.TextInput(label="Дата заполнения отчета:")
        self.date_last = discord.ui.TextInput(label="Дата последнего повышения:")

        self.add_item(self.name)
        self.add_item(self.job)
        self.add_item(self.screenshots)
        self.add_item(self.date_otchet)
        self.add_item(self.date_last)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "media" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["media"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на повышение №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="Media", inline=False)
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.job.label,
                value=self.job.value,
                inline=False,
            )
            embed.add_field(
                name=self.screenshots.label,
                value=self.screenshots.value,
                inline=False,
            )
            embed.add_field(
                name=self.date_otchet.label,
                value=self.date_otchet.value,
                inline=False,
            )
            embed.add_field(
                name=self.date_last.label,
                value=self.date_last.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Recertification(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Переаттестация сотрудника", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия / Ваша должность:")
        self.ppo = discord.ui.TextInput(
            label="Доказательства о пересдачи Устава / ППО-ПРО",
            placeholder="https://imgur.com/",
        )
        self.smi = discord.ui.TextInput(
            label='Доказательства о пересдаче "Закон о СМИ"',
            placeholder="https://imgur.com/",
        )
        self.ppe = discord.ui.TextInput(
            label='Доказательства о пересдаче экзамена "ППЭ"',
            placeholder="https://imgur.com/",
        )
        self.date_otchet = discord.ui.TextInput(
            label="Дата заполнения отчета/последнего повышения:"
        )

        self.add_item(self.name)
        self.add_item(self.ppo)
        self.add_item(self.smi)
        self.add_item(self.ppe)
        self.add_item(self.date_otchet)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "recertification" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["recertification"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на переаттестацию №{message_count}", color=0xDC143C
            )
            embed.add_field(
                name="Тема:", value="Переаттестация сотрудника", inline=False
            )
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.ppo.label,
                value=self.ppo.value,
                inline=False,
            )
            embed.add_field(
                name=self.smi.label,
                value=self.smi.value,
                inline=False,
            )
            embed.add_field(
                name=self.ppe.label,
                value=self.ppe.value,
                inline=False,
            )
            embed.add_field(
                name=self.date_otchet.label,
                value=self.date_otchet.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Change_Name(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Смена Имени и Фамилии", *args, **kwargs)
        self.before = discord.ui.TextInput(label="Было:")
        self.after = discord.ui.TextInput(label="Стало:")

        self.add_item(self.before)
        self.add_item(self.after)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "change-name" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["change-name"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на смену имени №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="Смена Имени и Фамилии", inline=False)
            embed.add_field(
                name=self.before.label,
                value=self.before.value,
                inline=False,
            )
            embed.add_field(
                name=self.after.label,
                value=self.after.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Accept_Quit(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(title="Уволиться", *args, **kwargs)
        self.name = discord.ui.TextInput(label="Имя Фамилия | Номер паспорта:")
        self.job = discord.ui.TextInput(label="Ваша должность и отдел:")
        self.quit = discord.ui.TextInput(label="Причина увольнения:")
        self.shtraf = discord.ui.TextInput(
            label="Доказательство оплаты штрафа/неустойки:",
            placeholder="При наличии активных штрафов",
        )
        self.date = discord.ui.TextInput(label="Дата заполнения:")

        self.add_item(self.name)
        self.add_item(self.job)
        self.add_item(self.quit)
        self.add_item(self.shtraf)
        self.add_item(self.date)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            with open("names.json") as file:
                data = json.load(file)
            if str(interaction.guild.id) in data:
                if "quit" in data[str(interaction.guild.id)]:
                    channel = interaction.guild.get_channel(
                        data[str(interaction.guild.id)]["quit"]
                    )
                else:
                    return await interaction.response.send_message(
                        content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                        ephemeral=True,
                        delete_after=60,
                    )
            else:
                return await interaction.response.send_message(
                    content="Ваша заявка не была отправлена, так как Владельцы Сервера не настроили канал для приёма заявок!",
                    ephemeral=True,
                    delete_after=60,
                )
            message_count = 1
            async for _ in channel.history(limit=None):
                message_count += 1
            embed = discord.Embed(
                title=f"Заявление на увольнение №{message_count}", color=0xDC143C
            )
            embed.add_field(name="Тема:", value="Уволиться", inline=False)
            embed.add_field(
                name=self.name.label,
                value=self.name.value,
                inline=False,
            )
            embed.add_field(
                name=self.job.label,
                value=self.job.value,
                inline=False,
            )
            embed.add_field(
                name=self.quit.label,
                value=self.quit.value,
                inline=False,
            )
            embed.add_field(
                name=self.shtraf.label,
                value=self.shtraf.value,
                inline=False,
            )
            embed.add_field(
                name=self.date.label,
                value=self.date.value,
                inline=False,
            )
            await channel.send(embed=embed)
            await interaction.response.send_message(
                content="Ваша заявка была успешно отправлена!",
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content="Произошла ошибка при отправке заявки.",
                ephemeral=True,
                delete_after=60,
            )
            traceback.print_exception(type(e), e, e.__traceback__)


class Limit(discord.ui.Modal):
    def __init__(self, title, label, placeholder, lang, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.lang = lang
        self.limit = discord.ui.TextInput(
            label=label, placeholder=placeholder, max_length=2
        )
        self.add_item(self.limit)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            number = int(self.limit.value)
            channel = interaction.guild.get_channel(
                private_channels[str(interaction.user.id)]
            )
            await channel.edit(user_limit=number)
            await interaction.response.send_message(
                content=self.get_message("limit_set").format(self.limit.value),
                ephemeral=True,
                delete_after=60,
            )
        except ValueError:
            await interaction.response.send_message(
                content=self.get_message("invalid_format"),
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content=self.get_message("error"), ephemeral=True, delete_after=60
            )
            traceback.print_exception(type(e), e, e.__traceback__)

    def get_message(self, key):
        messages = {
            "ru": {
                "limit_set": "Лимит пользователей установлен на {}!",
                "invalid_format": "Неверный формат лимита!",
                "error": "Произошла ошибка при установке лимита.",
            },
            "en": {
                "limit_set": "User limit set to {}!",
                "invalid_format": "Invalid limit format!",
                "error": "An error occurred while setting the limit.",
            },
        }
        return messages[self.lang].get(key)


class Bitrate(discord.ui.Modal):
    def __init__(self, title, label, placeholder, lang, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.lang = lang
        self.bitrate = discord.ui.TextInput(
            label=label, placeholder=placeholder, min_length=1, max_length=5
        )
        self.add_item(self.bitrate)

    async def on_submit(self, interaction: discord.Interaction):
        try:
            number = int(self.bitrate.value) * 1000
            if 8000 <= number <= 96000:
                channel = interaction.guild.get_channel(
                    private_channels[str(interaction.user.id)]
                )
                await channel.edit(bitrate=number)
                await interaction.response.send_message(
                    content=self.get_message("bitrate_set").format(self.bitrate.value),
                    ephemeral=True,
                    delete_after=60,
                )
            else:
                await interaction.response.send_message(
                    content=self.get_message("bitrate_range"),
                    ephemeral=True,
                    delete_after=60,
                )
        except ValueError:
            await interaction.response.send_message(
                content=self.get_message("invalid_format"),
                ephemeral=True,
                delete_after=60,
            )
        except Exception as e:
            await interaction.response.send_message(
                content=self.get_message("error"), ephemeral=True, delete_after=60
            )
            traceback.print_exception(type(e), e, e.__traceback__)

    def get_message(self, key):
        messages = {
            "ru": {
                "bitrate_set": "Битрейт установлен на {} kbps!",
                "bitrate_range": "Битрейт должен быть между 8 и 96!",
                "invalid_format": "Неверный формат битрейта!",
                "error": "Произошла ошибка при установке битрейта.",
            },
            "en": {
                "bitrate_set": "Bitrate set to {} kbps!",
                "bitrate_range": "Bitrate must be between 8 and 96!",
                "invalid_format": "Invalid bitrate format!",
                "error": "An error occurred while setting the bitrate.",
            },
        }
        return messages[self.lang].get(key)


class RenameCategory(discord.ui.Modal):
    def __init__(self, title, label, placeholder, lang, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.lang = lang
        self.new_name = discord.ui.TextInput(
            label=label,
            placeholder=placeholder,
            min_length=2,
            max_length=99,
        )
        self.add_item(self.new_name)

    async def on_submit(self, interaction: discord.Interaction):
        with open("names.json") as file:
            data = json.load(file)
        if self.new_name.value.strip() == "":
            return await interaction.response.send_message(
                content=self.get_message("empty_name"),
                ephemeral=True,
                delete_after=60,
            )

        try:
            category = discord.utils.get(
                interaction.guild.categories,
                id=data[str(interaction.guild.id)]["category_id"],
            )
            await category.edit(name=self.new_name.value)
        except Exception as e:
            await interaction.response.defer()
            await interaction.followup.send(
                content=self.get_message("error"),
                ephemeral=True,
                delete_after=60,
            )
            return traceback.print_exception(type(e), e, e.__traceback__)

        await interaction.response.send_message(
            content=self.get_message("name_changed").format(self.new_name.value),
            ephemeral=True,
            delete_after=60,
        )

    def get_message(self, key):
        messages = {
            "ru": {
                "empty_name": "Название категории не может быть пустым!",
                "error": "Произошла ошибка при смене названия категории.",
                "name_changed": "Название категории изменено на {}!",
            },
            "en": {
                "empty_name": "Category name cannot be empty!",
                "error": "An error occurred while changing the category name.",
                "name_changed": "Category name changed to {}!",
            },
        }
        return messages[self.lang].get(key)


class RenameChannel(discord.ui.Modal):
    def __init__(self, title, label, placeholder, lang, *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.lang = lang
        self.new_name = discord.ui.TextInput(
            label=label,
            placeholder=placeholder,
            min_length=2,
            max_length=99,
        )
        self.add_item(self.new_name)

    async def on_submit(self, interaction: discord.Interaction):
        with open("names.json") as file:
            data = json.load(file)
        if self.new_name.value.strip() == "":
            return await interaction.response.send_message(
                content=self.get_message("empty_name"),
                ephemeral=True,
                delete_after=60,
            )
        elif (
            self.new_name.value
            == discord.utils.get(
                interaction.guild.channels,
                id=data[str(interaction.guild.id)]["voice_channel_id"],
            ).name
        ):
            ch = discord.utils.get(
                interaction.guild.channels,
                id=data[str(interaction.guild.id)]["voice_channel_id"],
            )
            return await interaction.response.send_message(
                content=self.get_message("name_conflict").format(ch.mention),
                ephemeral=True,
                delete_after=60,
            )
        try:
            channel = interaction.guild.get_channel(
                int(private_channels[str(interaction.user.id)])
            )
            await channel.edit(name=self.new_name.value)
        except Exception as e:
            await interaction.response.defer()
            await interaction.followup.send(
                content=self.get_message("error"),
                ephemeral=True,
                delete_after=60,
            )
            return traceback.print_exception(type(e), e, e.__traceback__)

        await interaction.response.send_message(
            content=self.get_message("name_changed").format(self.new_name.value),
            ephemeral=True,
            delete_after=60,
        )

    def get_message(self, key):
        messages = {
            "ru": {
                "empty_name": "Название канала не может быть пустым!",
                "name_conflict": "Название канала не должно совпадать с каналом {}",
                "error": "Произошла ошибка при смене названия канала.",
                "name_changed": "Название канала изменено на {}!",
            },
            "en": {
                "empty_name": "Channel name cannot be empty!",
                "name_conflict": "Channel name must not match the channel {}",
                "error": "An error occurred while changing the channel name.",
                "name_changed": "Channel name changed to {}!",
            },
        }
        return messages[self.lang].get(key)


class UserSelectView(discord.ui.View):
    def __init__(self, task, lang):
        super().__init__()
        self.add_item(UserSelect(task, lang))


class UserSelect(discord.ui.UserSelect):
    def __init__(self, task, lang):
        self.task = task
        self.lang = lang
        super().__init__(
            placeholder=self.get_placeholder(), max_values=19, min_values=1
        )

    def get_placeholder(self):
        placeholders = {"ru": "Выберите пользователя...", "en": "Select a user..."}
        return placeholders.get(self.lang, "Select a user...")

    def get_message(self, key):
        messages = {
            "ru": {
                "invite_sent": "Приглашение отправлено!",
                "invite_failed": "Не удалось отправить приглашение!",
                "user_banned": "Пользователь успешно заблокирован!",
                "user_permitted": "Пользователь успешно разрешен!",
                "chat_allowed": "Пользователю разрешено писать в чат!",
                "user_moved": "Выбранный пользователь {user} успешно присоединился к {channel}!",
                "not_in_channel": "Выбранный пользователь {user} не находится в вашем канале!",
                "not_in_voice": "Выбранный пользователь {user} не находится в голосовом канале!",
                "cannot_claim_own": "Вы не можете выдать самому себе права на канал!",
                "claimed_success": "Выбранный пользователь {user} успешно получил права к {channel}!",
                "cannot_transfer_own": "Вы не можете забрать у себя права на канал!",
                "rights_removed": "У выбранного пользователя {user} успешно убраны права на канал {channel}!",
                "no_rights": "У выбранного пользователя {user} нет прав на канал {channel}!",
                "no_ownership": "Вы не имеете права в каналах!",
            },
            "en": {
                "invite_sent": "Invitation sent!",
                "invite_failed": "Failed to send invitation!",
                "user_banned": "User successfully banned!",
                "user_permitted": "User successfully permitted!",
                "chat_allowed": "User allowed to chat!",
                "user_moved": "Selected user {user} successfully moved to {channel}!",
                "not_in_channel": "Selected user {user} is not in your channel!",
                "not_in_voice": "Selected user {user} is not in a voice channel!",
                "cannot_claim_own": "You cannot claim ownership of the channel for yourself!",
                "claimed_success": "Selected user {user} successfully claimed the channel {channel}!",
                "cannot_transfer_own": "You cannot transfer ownership of the channel to yourself!",
                "rights_removed": "Rights for selected user {user} successfully removed from channel {channel}!",
                "no_rights": "Selected user {user} has no rights to the channel {channel}!",
                "no_ownership": "You do not own any channels!",
            },
        }
        return messages.get(self.lang, {}).get(key, "Unknown message")

    async def callback(self, interaction: discord.Interaction):
        global private_channels
        channel = interaction.guild.get_channel(
            private_channels[str(interaction.user.id)]
        )
        for selected_user in self.values:
            if self.task == "invite":
                emb = discord.Embed(
                    title=(
                        "Новое приглашение!" if self.lang == "ru" else "New Invitation!"
                    ),
                    description=(
                        f"{interaction.user.mention} пригласил вас присоединиться к {channel.mention}"
                        if self.lang == "ru"
                        else f"{interaction.user.mention} invited you to join {channel.mention}"
                    ),
                    color=discord.Color.from_rgb(0, 255, 0),
                )
                await channel.set_permissions(selected_user, connect=True)
                try:
                    await selected_user.send(embed=emb)
                except:
                    return await interaction.response.edit_message(
                        content=self.get_message("invite_failed"),
                        embed=None,
                        view=None,
                    )
                await interaction.response.edit_message(
                    content=self.get_message("invite_sent"),
                    embed=None,
                    view=None,
                )

            elif self.task == "ban":
                if selected_user.voice and int(selected_user.voice.channel.id) == int(
                    channel.id
                ):
                    try:
                        await selected_user.move_to(None)
                    except:
                        pass
                await channel.set_permissions(
                    selected_user,
                    connect=False,
                    read_message_history=False,
                    send_messages=False,
                )
                await interaction.response.edit_message(
                    content=self.get_message("user_banned"),
                    embed=None,
                    view=None,
                )

            elif self.task == "permit":
                await channel.set_permissions(selected_user, overwrite=None)
                await interaction.response.edit_message(
                    content=self.get_message("user_permitted"),
                    embed=None,
                    view=None,
                )

            elif self.task == "chat":
                await channel.set_permissions(
                    selected_user,
                    read_messages=True,
                    read_message_history=True,
                    send_messages=True,
                )
                await interaction.response.edit_message(
                    content=self.get_message("chat_allowed"),
                    embed=None,
                    view=None,
                )

            elif self.task == "wait":
                if selected_user.voice and int(selected_user.voice.channel.id) == int(
                    channel.id
                ):
                    with open("names.json") as file:
                        data = json.load(file)
                    maincategory = discord.utils.get(
                        interaction.guild.categories,
                        id=data[str(interaction.guild.id)]["category_id"],
                    )
                    reference_channel_for_priv = discord.utils.get(
                        interaction.guild.channels,
                        id=data[str(interaction.guild.id)]["voice_channel_id"],
                    )

                    overwrites = {
                        interaction.guild.default_role: discord.PermissionOverwrite(
                            read_messages=False,
                            read_message_history=False,
                            send_messages=False,
                            connect=False,
                        ),
                        selected_user: discord.PermissionOverwrite(connect=True),
                        interaction.user: discord.PermissionOverwrite(connect=True),
                    }

                    waiting_channel = await interaction.guild.create_voice_channel(
                        name=f"{interaction.user.name}'s waiting channel",
                        category=maincategory,
                        position=reference_channel_for_priv.position + 1,
                        overwrites=overwrites,
                    )

                    await waiting_channel.edit(user_limit=2)
                    await selected_user.move_to(waiting_channel)
                    return await interaction.response.edit_message(
                        content=self.get_message("user_moved").format(
                            user=selected_user.mention, channel=waiting_channel.mention
                        ),
                        embed=None,
                        view=None,
                    )
                else:
                    await interaction.response.edit_message(
                        content=self.get_message("not_in_channel").format(
                            user=selected_user.mention
                        ),
                        embed=None,
                        view=None,
                    )

            elif self.task == "claim":
                if interaction.user.id == selected_user.id:
                    return await interaction.response.edit_message(
                        content=self.get_message("cannot_claim_own"),
                        embed=None,
                        view=None,
                        delete_after=60,
                    )
                if selected_user.voice and int(selected_user.voice.channel.id) == int(
                    channel.id
                ):
                    private_channels[str(selected_user.id)] = private_channels[
                        str(interaction.user.id)
                    ]
                    await interaction.response.edit_message(
                        content=self.get_message("claimed_success").format(
                            user=selected_user.mention, channel=channel.mention
                        ),
                        embed=None,
                        view=None,
                    )
                else:
                    await interaction.response.edit_message(
                        content=self.get_message("not_in_channel").format(
                            user=selected_user.mention
                        ),
                        embed=None,
                        view=None,
                    )

            elif self.task == "transfer":
                if interaction.user.id == selected_user.id:
                    return await interaction.response.edit_message(
                        content=self.get_message("cannot_transfer_own"),
                        embed=None,
                        view=None,
                        delete_after=60,
                    )
                if str(interaction.user.id) in private_channels:
                    if (
                        str(selected_user.id) in private_channels
                        and private_channels[str(interaction.user.id)]
                        == private_channels[str(selected_user.id)]
                    ):
                        private_channels.pop(str(selected_user.id))
                        await interaction.response.edit_message(
                            content=self.get_message("rights_removed").format(
                                user=selected_user.mention, channel=channel.mention
                            ),
                            embed=None,
                            view=None,
                        )
                    else:
                        await interaction.response.edit_message(
                            content=self.get_message("no_rights").format(
                                user=selected_user.mention, channel=channel.mention
                            ),
                            embed=None,
                            view=None,
                        )
                else:
                    await interaction.response.edit_message(
                        content=self.get_message("no_ownership"),
                        embed=None,
                        view=None,
                        delete_after=60,
                    )


class RegionSelect(discord.ui.Select):
    def __init__(self, lang="ru"):
        self.lang = lang

        options = [
            discord.SelectOption(label=self.get_label("automatic"), value="-"),
            discord.SelectOption(label="Brazil", emoji="🇧🇷", value="brazil"),
            discord.SelectOption(label="Hong Kong", emoji="🇭🇰", value="hongkong"),
            discord.SelectOption(label="India", emoji="🇮🇳", value="india"),
            discord.SelectOption(label="Japan", emoji="🇯🇵", value="japan"),
            discord.SelectOption(label="Rotterdam", emoji="🇳🇱", value="rotterdam"),
            discord.SelectOption(label="Russia", emoji="🇷🇺", value="russia"),
            discord.SelectOption(label="Singapore", emoji="🇸🇬", value="singapore"),
            discord.SelectOption(label="South Africa", emoji="🇿🇦", value="southafrica"),
            discord.SelectOption(label="Sydney", emoji="🇦🇺", value="sydney"),
            discord.SelectOption(label="US Central", emoji="🇺🇸", value="us-central"),
            discord.SelectOption(label="US East", emoji="🇺🇸", value="us-east"),
            discord.SelectOption(label="US South", emoji="🇺🇸", value="us-south"),
            discord.SelectOption(label="US West", emoji="🇺🇸", value="us-west"),
        ]
        super().__init__(placeholder=self.get_placeholder(), options=options)

    def get_placeholder(self):
        placeholders = {
            "ru": "Выберите регион канала...",
            "en": "Select channel region...",
        }
        return placeholders.get(self.lang, "Select channel region...")

    def get_label(self, key):
        labels = {
            "ru": {
                "automatic": "Автоматический выбор",
            },
            "en": {
                "automatic": "Automatic selection",
            },
        }
        return labels.get(self.lang, {}).get(key, key)

    async def callback(self, interaction: discord.Interaction):
        selected_region = self.values[0]
        channel = interaction.guild.get_channel(
            private_channels[str(interaction.user.id)]
        )
        if selected_region != "-":
            await channel.edit(rtc_region=selected_region)
            if selected_region == "southafrica":
                selected_region = "South Africa"
            elif selected_region == "us-central":
                selected_region = "US Central"
            elif selected_region == "us-east":
                selected_region = "US East"
            elif selected_region == "us-south":
                selected_region = "US South"
            elif selected_region == "us-west":
                selected_region = "US West"
            else:
                selected_region = selected_region.capitalize()

            response_message = {
                "ru": f"Регион канала установлен: {selected_region}",
                "en": f"Channel region set to: {selected_region}",
            }
            await interaction.response.edit_message(
                embed=None,
                view=None,
                content=response_message.get(self.lang, response_message["en"]),
            )
        else:
            await channel.edit(rtc_region=None)
            response_message = {
                "ru": "Регион канала установлен: Автоматический выбор",
                "en": "Channel region set to: Automatic selection",
            }
            await interaction.response.edit_message(
                embed=None,
                view=None,
                content=response_message.get(self.lang, response_message["en"]),
            )


class RegionSelectView(discord.ui.View):
    def __init__(self, lang="ru"):
        super().__init__()
        self.add_item(RegionSelect(lang))
