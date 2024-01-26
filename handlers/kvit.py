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



class Kvit(StatesGroup):
    FileExcel = State()
    FilePdf = State()
    Purpose = State()



# Обработчик на нажатие кнопки "Квитанции" в основном меню.
# Ссылка на .xlsx документ с примером сверки
@router.callback_query(F.data == 'kvit_mode')
async def kvit_mode(call: CallbackQuery, state: FSMContext):
    url = "https://docs.google.com/spreadsheets/d/1Y9reMBF4_aUSrJDeZ4VFnERJ9JkYlGJK/edit?usp=sharing&ouid=105467863721396286205&rtpof=true&sd=true"
    text_with_example = markdown.text(
        "Либо напишите прямо здесь\n\nПример:",
        markdown.markdown_decoration.pre_language(markdown.text("Иванов Иван Иванович 500\nПетров Петр 1000"),
                                                  language=""))
    await call.answer('Для изменения вида квитанций возвращайтесь в настройки')
    await call.message.answer(text= f"Пришлите мне файл сверки {hlink('Excel', url)}\n\n<i>Подробнее о нем можете узнать нажав /info</i>", parse_mode=ParseMode.HTML)
    await call.message.answer(text=text_with_example, parse_mode=ParseMode.MARKDOWN_V2)
    await state.set_state(Kvit.FileExcel)



# обработчик команды /kvit, работает точно также, как и хендлер выше
@router.message(Command('kvit'))
async def kvit_mode(message: Message, state: FSMContext):
    url = "https://docs.google.com/spreadsheets/d/1Y9reMBF4_aUSrJDeZ4VFnERJ9JkYlGJK/edit?usp=sharing&ouid=105467863721396286205&rtpof=true&sd=true"
    text_with_example = markdown.text(
        "Либо напишите прямо здесь\n\nПример:",
        markdown.markdown_decoration.pre_language(markdown.text("Иванов Иван Иванович 500\nПетров Петр 1000"),
                                                  language=""))
    await message.answer(text= f"Пришлите мне файл сверки {hlink('Excel', url)}\n\n<i>Подробнее о нем можете узнать нажав /info</i>", parse_mode=ParseMode.HTML)
    await message.answer(text=text_with_example, parse_mode=ParseMode.MARKDOWN_V2)
    await state.set_state(Kvit.FileExcel)



# обработчик сверки при отправке ее текстом
# toExcel(str - сообщение пользователя,str - название файла, который создаетс с его id)
@router.message(Kvit.FileExcel, F.text)
async def excel(message: Message, state: FSMContext):
    toExcel(text=message.text,Excel=f'{message.from_user.id}.xlsx')
    await state.set_state(Kvit.Purpose)
    await message.answer("Выберете назначение платежа",
                         reply_markup=get_inlane_keyboard('kvit_purpose'))



# обработчик файла сверки, есть проверка на то, что файл .xlsx
# созраняется под id пользователя, отправившего файл
@router.message(F.document and Kvit.FileExcel)
async def excel(message: Message, state: FSMContext, bot: Bot):
    if '.xlsx' in message.document.file_name:
        await bot.download(
            message.document,
            destination=f"{message.from_user.id}.xlsx"
        )
        await state.set_state(Kvit.Purpose)
        await message.answer("Выберете назначение платежа", reply_markup=get_inlane_keyboard('kvit_purpose'))

    else:
        await message.answer("Неправильный формат файла, попробуйте еще раз")



# ввод назначения платежа самостоятельно, без использования клавиатуры
@router.callback_query(F.data == 'kvit_input_purpose_mode')
async def purpose(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Каким будет ваше назначение платежа?")
    await call.answer()
    await state.set_state(Kvit.Purpose)



# Обработка назначения при самостоятельном вводе
# Отправляем пользователю действие - "Отправка файла"
# Вызываем функции по созданию квитанций
@router.message(Kvit.Purpose, F.text)
async def purpose(message: Message, state: FSMContext):
    await message.bot.send_chat_action(
        chat_id=message.from_user.id,
        action="upload_document"
    )

    await state.set_state(Kvit.FilePdf)
    
    purpose = str(message.text)
    file_from_pc = f"{message.from_user.id}.xlsx"

    if message.from_user.id == 1190681639:
        FilePDF=f'Квитанции {purpose}.pdf'
    else:
        FilePDF=f'Квитанции {purpose} {message.from_user.id}.pdf'

    read_excel(FileExcel=file_from_pc,month=purpose,FilePDF=FilePDF, id=message.from_user.id)

    await message.answer_document(FSInputFile(FilePDF), caption=purpose)

    os.remove(FilePDF)



# Обработка прошлого месяца
@router.callback_query(F.data == 'kvit_purpose_previous_month')
async def purpose(call: CallbackQuery, state: FSMContext):
    await call.bot.send_chat_action(
        chat_id=call.from_user.id,
        action="upload_document",
    )
    
    await state.set_state(Kvit.FilePdf)

    dict = get_month()
    purpose = dict["previous_month"]

    file_from_pc = f"{call.from_user.id}.xlsx"

    if call.from_user.id == 1190681639:
        FilePDF=f'Квитанции {purpose}.pdf'
    else:
        FilePDF=f'Квитанции {purpose} {call.from_user.id}.pdf'

    read_excel(FileExcel=file_from_pc,month=purpose,FilePDF=FilePDF, id=call.from_user.id)

    await call.message.answer_document(FSInputFile(FilePDF), caption=purpose)
    await call.answer()

    os.remove(FilePDF)



# обработка текущего месяца
@router.callback_query(F.data == 'kvit_purpose_current_month')
async def purpose(call: CallbackQuery, state: FSMContext):
    await call.bot.send_chat_action(
        chat_id=call.from_user.id,
        action="upload_document"
    )

    await state.set_state(Kvit.FilePdf)

    dict = get_month()
    purpose = dict["current_month"]

    file_from_pc = f"{call.from_user.id}.xlsx"

    if call.from_user.id == 1190681639:
        FilePDF=f'Квитанции {purpose}.pdf'
    else:
        FilePDF=f'Квитанции {purpose} {call.from_user.id}.pdf'

    read_excel(FileExcel=file_from_pc,month=purpose,FilePDF=FilePDF, id=call.from_user.id)

    await call.message.answer_document(FSInputFile(FilePDF),caption=purpose)
    await call.answer()

    os.remove(FilePDF)



# обработка следующего месяца
@router.callback_query(F.data == 'kvit_purpose_following_month')
async def purpose(call: CallbackQuery, state: FSMContext):
    await call.bot.send_chat_action(
        chat_id=call.from_user.id,
        action="upload_document"
    )

    await state.set_state(Kvit.FilePdf)

    dict = get_month()
    purpose = dict["following_month"]

    file_from_pc = f"{call.from_user.id}.xlsx"

    if call.from_user.id == 1190681639:
        FilePDF=f'Квитанции {purpose}.pdf'
    else:
        FilePDF=f'Квитанции {purpose} {call.from_user.id}.pdf'

    read_excel(FileExcel=file_from_pc,month=purpose,FilePDF=FilePDF, id=call.from_user.id)

    await call.message.answer_document(FSInputFile(FilePDF),caption=purpose)
    await call.answer()

    os.remove(FilePDF)



# Обработка ежегодного членского взноса
@router.callback_query(F.data == 'kvit_yearly_fee_mode')
async def purpose(call: CallbackQuery, state: FSMContext):
    await call.bot.send_chat_action(
        chat_id=call.from_user.id,
        action="upload_document"
    )

    await state.set_state(Kvit.FilePdf)

    purpose = "Ежегодный благотворительный членский взнос"
    purpose_short = "Ежегодный членский взнос"
    file_from_pc = f"{call.from_user.id}.xlsx"

    if call.from_user.id == 1190681639:
        FilePDF=f'Квитанции {purpose_short}.pdf'
    else:
        FilePDF=f'Квитанции {purpose_short} {call.from_user.id}.pdf'

    read_excel(FileExcel=file_from_pc,month=purpose,FilePDF=FilePDF, id=call.from_user.id)

    await call.message.answer_document(FSInputFile(FilePDF),caption=purpose)
    await call.answer()
    
    os.remove(FilePDF)


