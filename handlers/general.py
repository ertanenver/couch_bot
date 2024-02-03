from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import get_inlane_keyboard
from aiogram.utils.markdown import hlink
from database.insert_db import insert_id, insert_fio, insert_phone_number
from database.get_from_db import is_login, count_users, is_ok_fio
from database.delete_from_db import delete_all, delete_fio, delete_phone_number
import re

router = Router()

class Base(StatesGroup):
    start = State()
    help = State()
    kvit = State()
    info = State()
    act = State()
    owner = State()
    stat = State()
    fio = State()
    phone_number = State()

@router.message(CommandStart())
async def welcome(message: Message, state: FSMContext):
    fio = is_ok_fio(message.from_user.id)
    print(fio)
    if fio == True:   
        await state.set_state(Base.start)
        await message.answer(f'Привет!👋\nЯ тренерский бот Федерации тхэквон-до Тамбовской области\n\nЧто вы хотите сделать?👇', reply_markup=get_inlane_keyboard('welcome_msg'))
    else:
        delete_all(message.from_user.id)
        insert_id(id=message.from_user.id)
        await state.set_state(Base.fio)
        await message.answer(f'Привет👋, кажется мы еще не знакомы. Доступ к боту могут иметь лишь тренера.\n\nДля авторизации пришли мне свое ФИО, пожалуйста')



@router.message(F.text and Base.fio)
async def reg_fio(message:Message,state: FSMContext):
    pattern = r'^[а-яА-Я]+\s[а-яА-Я]+\s[а-яА-Я]+$'
    match = re.match(pattern, message.text)
    if match:
        insert_fio(id=message.from_user.id, fio=message.text)
        await message.answer(f'Хорошо, запомню вас как <i>{message.text}</i>')
        await state.set_state(Base.phone_number)
        await message.answer(f'Осталось чуть-чуть...\nПередайте мне теперь свой номер телефона\n\nОбратите внимание, для безопасности данных, можно использовать только один аккаунт в тг для его смены придется обращаться к администратору')
    else:
        await message.answer(f'Кажется: <i>{message.text}</i>, не похоже на ФИО. Попробуйте еще раз')
    

    
@router.message(F.text and Base.phone_number or F.contact and Base.phone_number)
async def reg_phone_number(message:Message,state: FSMContext):
    digits_pattern = r'\d'
    matches = re.findall(digits_pattern, message.text)

    if len(matches) >= 10:
        phone = re.sub(r'\D', '', message.text)

        # Проверка длины номера телефона
        if len(phone) == 10:
            phone = '+7 (' + phone[:3] + ') ' + phone[3:6] + '-' + phone[6:]
        elif len(phone) == 11:
            phone = '+7 (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:]
        elif len(phone) == 12:
            phone = '+' + phone[:1] + ' (' + phone[2:5] + ') ' + phone[5:8] + '-' + phone[8:]
        insert_phone_number(id=message.from_user.id, phone_number= phone)
        await message.answer(f'Записываю ваш номер как <u>{phone}</u>')
        await state.set_state(Base.start)
        await message.answer(f'Привет!👋\nЯ тренерский бот Федерации тхэквон-до Тамбовской области\n\nЧто вы хотите сделать?👇', reply_markup=get_inlane_keyboard('welcome_msg'))    
    else:
        await message.answer(f'Ваш ввод: <u>{message.text}</u> не похож на номер телефона, попробуйте еще раз')



@router.message(Command('help'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.help)
    await message.answer(f'🆘 Помощь!\n\nЧто-то некорректно работает? <i>Пишите @shinyaa17</i>')

@router.message(Command('owner'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.owner)
    await message.answer(f'Вы можете со мной связаться <i>здесь - @shinyaa17</i>')

@router.message(Command('act'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.act)
    await message.answer(f'У вас пока нет доступа')

@router.message(Command('check'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.check)
    await message.answer(f'У вас пока нет доступа')

@router.message(Command('stat'))
async def help(message: Message, state: FSMContext):
    await state.set_state(Base.stat)
    await message.answer(f'Кол-во подключенных пользователей: {count_users()}')

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
    await call.message.answer(f'Привет!👋\nЯ тренерский бот Федерации тхэквон-до Тамбовской области\n\nЧто вы хотите сделать?👇', reply_markup=get_inlane_keyboard('welcome_msg'))
    await call.answer()

