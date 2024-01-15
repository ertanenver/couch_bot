import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from handlers import general, kvit, sverka, admin
from settings import settings
from aiogram.filters import Command
from aiogram.methods.stop_poll import StopPoll

async def start_bot(bot: Bot):

    await bot.send_message(settings.bots.admin_id, text='Запущен бот\n"Соревновательный"\n\n/start')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text=f'Остановлен бот\n"Соревновательный"\n\n<u><i>Всего подключилось</i>:50000</u>')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "%(message)s - (%(filename)s).%(funcName)s(%(lineno)d)")
                        
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(general.router, kvit.router, sverka.router, admin.router)

    @dp.message(Command('kill'))
    async def stop(message: Message):
        if message.from_user.id == settings.bots.admin_id:
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