import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from handlers import general, kvit, settings_bot, sverka, admin
from settings import settings
from aiogram.filters import Command
from database.create_db import create_db
from database.get_from_db import count_users, get_permission, get_permission_list, is_login
from database.insert_db import insert_id,insert_fio,insert_permission

async def start_bot(bot: Bot):
    for admin in get_permission_list():
        await bot.send_message(admin, text='Запущен бот\n"Соревновательный"\n\n/start')

async def stop_bot(bot: Bot):
    for admin in get_permission_list():
        await bot.send_message(admin, text=f'Остановлен бот\n"Соревновательный"\n\n<u><i>Всего пользователей</i>: {count_users()}</u>')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "%(message)s - (%(filename)s).%(funcName)s(%(lineno)d)")
                        
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    create_db()
    
    if is_login(1) != "[]":
        insert_id(1)
        insert_fio(1,"admin")
        insert_permission(1,'super_user')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(general.router, kvit.router, sverka.router, admin.router, settings_bot.router)

    @dp.message(Command('stop'))
    async def stop(message: Message):
        if message.from_user.id == settings.bots.admin_id or get_permission(id=message.from_user.id) == 'super_user':
            await message.answer("Вы уверены, что хотите выключить бота? Отменить это действие будет нельзя. Для продолжения работы, будет необходимо запустить его вручную\n\nЕсли согласны, напишите: /kill")
        else:
            await message.answer_sticker(sticker='CAACAgIAAxkBAAIHKmWlI-9p2YHzsboRA0do6Ilxszq6AAJ-AAPBnGAMCxR_3b0i_fM0BA')
            await message.answer(f'Ты не похож на админа\n\n<i><u>Возможно стоит сменить аккаунт?)</u></i>')



    @dp.message(Command('kill'))
    async def stop(message: Message):
        if message.from_user.id == settings.bots.admin_id or get_permission(id=message.from_user.id) == 'super_user':
            await message.answer(f'Окей, бот будет выключен')
            quit()
        else:
            await message.answer_sticker(sticker='CAACAgIAAxkBAAIHKmWlI-9p2YHzsboRA0do6Ilxszq6AAJ-AAPBnGAMCxR_3b0i_fM0BA')
            await message.answer(f'Ты не похож на админа\n\n<i><u>Возможно стоит сменить аккаунт?)</u></i>')



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ =='__main__':
    asyncio.run(start())