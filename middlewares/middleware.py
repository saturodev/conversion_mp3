import logging
from datetime import datetime
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        start_time = datetime.now()

        logging.info(
            f"[{event.date}] Сообщение от {event.from_user.full_name} "
            f"(ID: {event.from_user.id}): {event.text}"
        )

        result = await handler(event, data)

        processing_time = datetime.now() - start_time
        logging.info(f"Обработка заняла: {processing_time}")

        return result
