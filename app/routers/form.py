from aiogram import F, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.keyboards import back_kb

router = Router()


class Request(StatesGroup):
    name = State()
    contact = State()
    comment = State()


@router.callback_query(F.data == "request")
async def handle_request(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Request.name)
    await callback.message.answer("Введите, пожалуйста, свое имя:", reply_markup=back_kb())
    await callback.answer()

@router.callback_query(Request(), F.data == "main_menu")
async def handle_back(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Вы вновь в главном меню")


@router.message(Request.name)
async def handle_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Request.contact)
    await message.answer("Отправьте свой контакт", reply_markup=back_kb())


