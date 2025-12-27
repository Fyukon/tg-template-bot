from sqlalchemy import select
import logging

from app.database import async_session, User, Lead


async def set_user(tg_id: int, username: str | None):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, username=username))

            await session.commit()


async def set_lead(tg_id: int, data: dict):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            new_lead = Lead(user_id=user.id, name=data['name'], phone=data['phone_number'],
                            comment=data.get('comment'))

            session.add(new_lead)
            await session.commit()
            logging.info(f"Заявка от {user.id} принята!")
        else:
            logging.info(f"Заявка от {tg_id} не прошла. Пользователя не существует!")
