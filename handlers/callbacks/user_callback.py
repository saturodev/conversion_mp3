from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from services.api.youtubeMP3 import get_url
from utils.database.insert_to_db import add_to_music, get_music_by_url_id

router = Router()


@router.callback_query(lambda c: c.data == "download_mp3")
async def process_show_id_callback(
    callback_query: CallbackQuery,
    state: FSMContext,
):
    # ⚡ Снимаем белую подсветку сразу
    await callback_query.answer()
    await callback_query.message.delete()
    loading_msg = await callback_query.message.answer(
        "⏳ Скачиваю... Пожалуйста, подождите"
    )
    data = await state.get_data()
    url = data.get("link")
    video_id = get_url(url)
    music = get_music_by_url_id(video_id)
    if not music:
        mp3_url = video_id[0]
        msg = await callback_query.message.answer_audio(
            audio=mp3_url,
        )
        add_to_music(
            callback_query.from_user.id,
            msg.audio.title,
            msg.audio.file_id,
            video_id[1],
        )
    else:
        file_id = music[3]
        await callback_query.message.answer_audio(
            audio=file_id,
        )
    await loading_msg.delete()


# === Отмена ===
@router.callback_query(lambda c: c.data == "cancel")
async def process_cancel(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer("❌ Отмена")
