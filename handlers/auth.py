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



