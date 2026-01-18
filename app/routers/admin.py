from aiogram import Router, types, F
from aiogram.filters import Command

from app.dao import get_leads

admin_id = 582690569

router = Router()


@router.message(Command("leads"))
async def send_leads(message: types.Message):
    if message.from_user.id != admin_id:
        return
    leads = await get_leads()

    if not leads:
        await message.answer("Заявок на данный момент нет")
        return
    response = "**Последние заявки:**\n\n"
    for lead in leads:
        response += f" 🆔:{lead.id}\n 👤:{lead.name}\n 📞:{lead.phone}\n 💬:{lead.comment or "без комм."}\n─────────────\n"
    await message.answer(response, parse_mode="Markdown")
