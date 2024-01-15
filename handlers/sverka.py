from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from funcs.excel_couch import excel_couch

router = Router()

class Sverka(StatesGroup):
    ddd = State()

@router.callback_query(F.data == 'sverka_mode')
async def kvit_mode(call: CallbackQuery, state: FSMContext):

    print(excel_couch("coach.xlsx"))
    await state.set_state(Sverka.ddd)
    await call.answer('Может быть позже?)')

@router.callback_query(F.data == 'settings')
async def kvit_mode(call: CallbackQuery, state: FSMContext):
    await state.set_state(Sverka.ddd)
    await call.answer('Может быть позже?)')
