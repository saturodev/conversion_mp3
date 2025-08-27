from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.reply_keyboard import keyboard_single_row
from utils.database.insert_to_db import add_to_user, get_user_by_id

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user = get_user_by_id(message.from_user.id)
    if not user:
        add_to_user(
            message.from_user.id,
            message.from_user.is_bot,
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_user.is_premium,
        )
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!\n\n"
            "Я бот, который помогает скачать музыку из YouTube.\n"
            "Просто пришли мне ссылку на видео, и я отправлю тебе аудио.\n\n"
            "👉 Отправь ссылку с YouTube и наслаждайся музыкой!",
            reply_markup=keyboard_single_row,
        )
    else:
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!\n\n"
            "Я бот, который помогает скачать музыку из YouTube.\n"
            "Просто пришли мне ссылку на видео, и я отправлю тебе аудио.\n\n"
            "👉 Отправь ссылку с YouTube и наслаждайся музыкой!",
            reply_markup=keyboard_single_row,
        )
