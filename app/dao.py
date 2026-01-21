import logging

from sqlalchemy import select, desc, delete, update

from app.database import async_session, User, Lead

logger = logging.getLogger(__name__)


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
            logger.info(f"Заявка от {user.id} принята!")
        else:
            logger.info(f"Заявка от {tg_id} не прошла. Пользователя не существует!")


async def get_lead():
    pass

async def get_leads():
    async with async_session() as session:
        query = select(Lead)

        result = await session.scalars(query)
        return result.all()


async def delete_all_leads():
    async with async_session() as session:
        await session.execute(delete(Lead))
        await session.commit()
        logger.warning("Все заявки были удалены")
