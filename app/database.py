from datetime import datetime
from sqlalchemy import BigInteger, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from app.config import config


engine = create_async_engine(config.DATABASE_URL, echo = False)

async_session = async_sessionmaker(engine, expire_on_commit = False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    tg_id: Mapped[int] = mapped_column(BigInteger, unique = True)

    username: Mapped[str | None] = mapped_column(String(128))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    name: Mapped[str] = mapped_column(String(128))
    phone: Mapped[str] = mapped_column(String(24))
    comment: Mapped[str] = mapped_column(String(1024))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)