from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(F.text == "/start")
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text = "text: ru", callback_data="btn_pressed"))
    await message.answer(text = "Выберите язык", reply_markup = builder.as_markup())

@start_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Да! Обращайся, конечно!")

@start_router.message(F.text.lower() == "Как дела?".lower())
async def cmd_qstn(message: types.Message):
    await message.answer("Да отлично все, сам как ?")

@start_router.callback_query(F.data == "btn_pressed")
async def btn_pressed(callback: types.CallbackQuery):
    await callback.answer("Кнопка нажата")
    await callback.message.answer("Подтверждаю нажатие!")
    await callback.message.delete()