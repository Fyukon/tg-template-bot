import logging
from curses.ascii import isdigit

from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.dao import set_lead
from app.keyboards import back_kb, contact_kb, main_kb

router = Router()
logger = logging.getLogger(__name__)


class Request(StatesGroup):
    name = State()
    contact = State()
    comment = State()


@router.callback_query(F.data == "request")
async def handle_request(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Request.name)
    await callback.message.answer("Введите, пожалуйста, свое имя:", reply_markup=back_kb())
    await callback.message.delete()
    await callback.answer()


@router.callback_query(Request(), F.data == "main_menu")
async def handle_back(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Вы вновь в главном меню", reply_markup=main_kb())
    await callback.message.delete()
    await callback.answer()


@router.message(Request.name)
async def handle_name(message: types.Message, state: FSMContext):
    if len(message.text) < 2 or sum(map(isdigit, message.text)):
        await message.answer("Имя не может быть слишком коротким или содержать цифры")
        return
    await state.update_data(name=message.text)
    await state.set_state(Request.contact)
    await message.answer("Отправьте свой контакт", reply_markup=contact_kb())


@router.message(Request.contact, F.contact)
async def handle_contact(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await state.set_state(Request.comment)
    await message.answer("Комментарий (если есть)", reply_markup=types.ReplyKeyboardRemove())


@router.message(Request.contact, F.text)
async def handle_contact(message: types.Message, state: FSMContext):
    await message.answer("Отправьте, пожалуйста, контакт кнопкой внизу")


@router.message(Request.comment)
async def handle_comment(message: types.Message, state: FSMContext):
    logger.debug("Зашел в comment")
    await state.update_data(comment=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer(f"Ваша заявка принята! \n{data['name']} \n{data['phone_number']} \n{data['comment']}")
    await set_lead(message.from_user.id, data)
