from aiogram import F, Router
from aiogram.filters import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import  inline_keyb, simp_keyb
from aiogram import types
from aiogram.fsm.state import StatesGroup, State

router = Router()

class Auth(StatesGroup):
    login = State()
    password = State()
    phone_number = State()

@router.message(Auth.login)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(login=message.text)
    for login in range(len(user_list)):
        #print(message)
        if message.text == user_list[login][1] or message.text == user_list[login][2] or message.text == user_list[login][3]:
            await message.answer(f"Введенный логин: <u><i>{message.text}</i></u>")
            await message.answer(f'Теперь введите пароль')
            await state.update_data(line=login)
            await state.set_state(Auth.password)
            break
    else:
         await message.answer(f"Введенный логин: <u><i>{message.text}</i></u> не зарегистрирован.\n\nПопробуйте еще раз или напишите @shinyaa17")
             
    



@router.message(Auth.password)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    if message.text == user_list[int(user_data['line'])][-1]:
        await message.answer(f"Введенный логин: <u><i>{user_data['login']}</i></u>")
        await message.answer(f"Введенный пароль: <u><i>{len(message.text)*'*'}</i></u>")
        authorised_users.append(user_list[int(user_data['line'])][1])
        await state.update_data(FIO=user_list[int(user_data['line'])][1])
        print(authorised_users,user_data['login'])


    await state.set_state(Auth.password)