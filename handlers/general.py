from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import get_inlane_keyboard
router = Router()

class Base(StatesGroup):
    start = State()
    help = State()
    kvit = State()

@router.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    await state.set_state(Base.start)
    await message.answer(f'Привет!👋', reply_markup=get_inlane_keyboard('welcome_msg'))

@router.message(Command('help'))
async def welcome(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'Помощь!')

@router.message(Command('info'))
async def welcome(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'Информация!')

@router.callback_query(F.data == 'button_0')
async def purpose(call: CallbackQuery, state: FSMContext):
    await state.set_state(Base.start)
    await call.message.answer(f'Привет!👋', reply_markup=get_inlane_keyboard('welcome_msg'))
    await call.answer()
