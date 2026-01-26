import time
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int = 2):
        self.limit = time_limit
        self.storage = {}

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message, data: Dict[str, Any]) -> Any:
        user = event.from_user.id
        if user in self.storage:
            if (time.time() - self.storage[user]) < self.limit:
                await event.answer("Не спеши!")
                return None
        self.storage[user] = time.time()
        return await handler(event, data)
