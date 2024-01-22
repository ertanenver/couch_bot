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
import os

router = Router()

class Settings(StatesGroup):
    Feature = State()
    Notification = State()
    Auth = State()
    Sum_kvit = State()

@router.callback_query(F.data == 'settings')
async def settings(call: CallbackQuery):
    await call.message.answer("Настройки", reply_markup=get_inlane_keyboard('settings'))
    await call.answer()
    
@router.callback_query(F.data == 'settings_sum_kvit')
async def settings_sum_kvit_on_page(call: CallbackQuery, state: FSMContext):
    await state.set_state(Settings.Sum_kvit)
    await call.message.answer("Кол-во квитанций на один лист", reply_markup=get_inlane_keyboard('settings_sum_kvit'))
    await call.answer()
    
@router.callback_query(F.data == 'settings_feature')
async def settings_sum_kvit_on_page(call: CallbackQuery, state: FSMContext):
    await state.set_state(Settings.Feature)
    await call.message.answer(text="Вы можете добавить уникальные символы, инициалы, что угодно на свои квитанции.\n\nВне зависимости от вашего выбора назначения, фича будет писаться в конце. Напишите свою мне",
                               reply_markup=get_inlane_keyboard('main_menu'))
    await call.answer()

@router.message(F.text and Settings.Feature)
async def feature(message: Message, state: FSMContext):
    await message.answer(f'Здесь записываем {message.text} в БД, а потом добавляешь проверку на нее в хендлере квитанций')