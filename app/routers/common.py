from aiogram import Router, types, F
from aiogram.filters import Command

from app.keyboards import main_kb, services_kb, back_kb

router = Router()


@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer(text="Главное меню", reply_markup=main_kb())


@router.callback_query(F.data == "main_menu")
async def back_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(text="Вы вновь в главном меню", reply_markup=main_kb())
    await callback.answer()


@router.callback_query(F.data == "services")
async def service_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(text="На данный момент вы выбираете услуги:", reply_markup=services_kb())
    await callback.answer()


@router.callback_query(F.data == "about")
async def about_menu(callback: types.CallbackQuery):
    await callback.message.edit_text(text="Это просто тренировочный бот, тут может быть много всего, мало смысла",
                                     reply_markup=back_kb())
    await callback.answer()


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Да! Обращайся, конечно!")
