from aiogram import Router, types, F
from aiogram.filters import Command
import logging

from app.dao import get_leads, delete_all_leads
from app.keyboards import admin_kb

admin_id = 582690569

router = Router()
logger = logging.getLogger(__name__)

@router.message(Command("admin"))
async def admin(message: types.Message):
    if message.from_user.id != admin_id:
        return
    await message.answer("Вы в админ меню", reply_markup=admin_kb())

@router.callback_query(F.data == "check_leads")
async def send_leads(callback: types.CallbackQuery):
    logger.debug("Check leads entered")
    await callback.answer()
    if callback.from_user.id != admin_id:
        return
    leads = await get_leads()

    if not leads:
        await callback.message.answer("Заявок на данный момент нет")
        return
    response = "**Последние заявки:**\n\n"
    for lead in leads:
        response += f" 🆔:{lead.id}\n 👤:{lead.name}\n 📞:{lead.phone}\n 💬:{lead.comment or "без комм."}\n─────────────\n"
    await callback.message.answer(response, parse_mode="Markdown")

@router.callback_query(F.data == "delete_leads")
async def delete_leads(callback: types.CallbackQuery):
    if callback.from_user.id != admin_id:
        return
    await delete_all_leads()
    await callback.message.answer("Все заявки были удалены")
    await callback.answer()


@router.callback_query(F.data == "get_lead")
async def delete_leads(callback: types.CallbackQuery):
    if callback.from_user.id != admin_id:
        return
    await callback.message.answer("В данный момент функция не реализована")
    await callback.answer()