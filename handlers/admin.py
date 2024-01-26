from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from aiogram.utils.markdown import hlink
from aiogram.types import FSInputFile
from aiogram import Bot
from keyboards.inline import get_inlane_keyboard
from funcs.get_month import get_month
from funcs.kvit import read_excel
from funcs.toExcel import toExcel
from settings import settings
from database.insert_db import insert_permission

router = Router()

class Admin(StatesGroup):
    panel = State()
    whats_new = State()
    super_user = State()
    super_user_password = State()


@router.message(Command('admin_panel'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Admin.panel)
    await message.answer(f'Вы можете со мной связаться <i>здесь - @shinyaa17</i>')

@router.message(Command('admin_panel_super_user'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Admin.super_user)
    await message.answer(f'Для получения прав супер пользователя введите пароль.')

@router.message(F.text and Admin.super_user)
async def password(message: Message, state: FSMContext):
    await state.set_state(Admin.super_user_password)
    if message.text == settings.bots.super_user_password:
        insert_permission(id=message.from_user.id, permission='super_user')
        await message.answer(f'Поздравляю, вы теперь супер пользователь. Теперь вы можете:\n1. Запрашивать чужие сверки\n2. Загружать банковскую выписку\n3. Просматривать активность пользователей, блокировать их и создавать новых\n4. завершать работу бота командой /stop')
    else:
        await message.answer_sticker(sticker='CAACAgIAAxkBAAIHKmWlI-9p2YHzsboRA0do6Ilxszq6AAJ-AAPBnGAMCxR_3b0i_fM0BA')
        await message.answer(f'Неправильный пароль\n\n<i><u>Возможно стоит попробовать еще раз</u></i>')