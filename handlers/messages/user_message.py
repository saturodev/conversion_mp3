from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from services.api.youtubeMP3 import get_youtube, is_music
from keyboards.inline_keyboard import inline_row

router = Router()


class LinkState(StatesGroup):
    link = State()


@router.message(F.text == "🚑Помощь🚑")
async def help_for_user(message: Message):
    await message.answer(
        "👋 Что случилось?\n\n"
        "Просто скинь мне ссылку на песню — и я пришлю тебе готовый аудиофайл (mp3).\n\n"
        "⚠️ Я умею работать только с музыкальными видео."
    )


@router.message(F.text.startswith("https"))
async def get_link(message: Message, state: FSMContext):
    url = message.text.strip()
    if "youtube.com" in url or "youtu.be" in url:
        category_id = is_music(url)
        if category_id is True:
            # сохраняем ссылку в FSM
            await state.update_data(link=url)

            await message.delete()

            thumbnail, title = get_youtube(url)
            await message.answer_photo(
                photo=thumbnail,
                caption=title,
                reply_markup=inline_row,
            )
        else:
            await message.answer(category_id)
    else:
        await message.answer("Это не ссылка на YouTube!")
