from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import get_inlane_keyboard
from aiogram.utils.markdown import hlink
router = Router()

class Base(StatesGroup):
    start = State()
    help = State()
    kvit = State()
    info = State()
    act = State()
    owner = State()
    stat = State()

@router.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    await state.set_state(Base.start)
    await message.answer(f'Привет!👋', reply_markup=get_inlane_keyboard('welcome_msg'))

@router.message(Command('help'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'🆘 Помощь!\n\nЧто-то некорректно работает? <i>Пишите @shinyaa17</i>')

@router.message(Command('owner'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'Вы можете со мной связаться <i>здесь - @shinyaa17</i>')

@router.message(Command('act'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'У вас пока нет доступа')

@router.message(Command('check'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'У вас пока нет доступа')

@router.message(Command('stat'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'У вас пока нет доступа')

@router.message(Command('info'))
async def info(message: Message, state: FSMContext):
    url = "https://docs.google.com/spreadsheets/d/1Y9reMBF4_aUSrJDeZ4VFnERJ9JkYlGJK/edit?usp=sharing&ouid=105467863721396286205&rtpof=true&sd=true"
    await state.set_state(Base.help)
    await message.answer(f'По {hlink("ссылке", url)} формат файла сверки.\n\nВ столбце А могут находится лишь <u>фамилии и названия групп.</u> '
                         f'В столбце В могут находится <u>сумма платежей(только цифры) и любое слово, например сумма, как в примере, для обозначения группы</u>')
    await message.answer('0 в суммах не учитываются, квитанции на них не создаются, пустых строк для разделения групп может быть не больше 1')

@router.callback_query(F.data == 'button_0')
async def main_menu(call: CallbackQuery, state: FSMContext):
    await state.set_state(Base.start)
    await call.message.answer(f'Привет!👋', reply_markup=get_inlane_keyboard('welcome_msg'))
    await call.answer()
