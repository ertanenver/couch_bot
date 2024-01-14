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
router = Router()

class Sverka(StatesGroup):
    ddd = State()

@router.callback_query(F.data == 'sverka_mode')
async def kvit_mode(call: CallbackQuery, state: FSMContext):
    await state.set_state(Sverka.ddd)
    await call.answer('Может быть позже?)')

@router.callback_query(F.data == 'settings')
async def kvit_mode(call: CallbackQuery, state: FSMContext):
    await state.set_state(Sverka.ddd)
    await call.answer('Может быть позже?)')
