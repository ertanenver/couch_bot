import asyncio
import logging
from aiogram import F, Router, types
from aiogram import Bot, Dispatcher
from handlers import general, kvit, sverka
from settings import settings

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
    dp.include_routers(general.router, kvit.router, sverka.router)
            

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ =='__main__':
    asyncio.run(start())