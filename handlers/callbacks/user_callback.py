from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from services.api.youtubeMP3 import get_url
from utils.database.insert_to_db import add_to_music, get_music_by_url_id
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


@router.callback_query(lambda c: c.data == "download_mp3")
async def process_show_id_callback(
    callback_query: CallbackQuery,
    state: FSMContext,
):

    # Снимаем белую подсветку сразу
    await callback_query.answer()
    await callback_query.message.delete()
    data = await state.get_data()
    url = data.get("link")
    video_id = get_url(url)
    music = get_music_by_url_id(video_id)
    if not music:
        # Сообщение о загрузке
        loading_msg = await callback_query.message.answer(
            "⏳ Скачиваю... Пожалуйста, подождите"
        )
        mp3_url = video_id[0]

        try:
            # пробуем отправить как аудио
            msg = await callback_query.message.answer_audio(audio=mp3_url)

            # сохраняем в БД (успешно)
            add_to_music(
                callback_query.from_user.id,
                msg.audio.title,
                msg.audio.file_unique_id,
                1,  # это file_id
                video_id[1],
            )
            await loading_msg.delete()
        except TelegramBadRequest:
            # если не получилось → даём кнопку "Скачать"
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="⬇️ Скачать MP3", url=mp3_url)]
                ]
            )
            await callback_query.message.answer(
                "⚠️ Telegram не смог загрузить файл. Но вы можете скачать его по ссылке:",
                reply_markup=keyboard,
            )

            # сохраняем в БД как "только ссылка"
            add_to_music(
                callback_query.from_user.id,
                "Unknown",  # можно подставить название
                mp3_url,  # тут не file_id, а сам url
                0,  # это ссылка
                video_id[1],
            )
            await loading_msg.delete()
    else:
        file_or_url = music[3]
        is_file_id = music[4]

        if is_file_id == 1:
            await callback_query.message.answer_audio(audio=file_or_url)

        else:
            keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(text="⬇️ Скачать MP3", url=file_or_url)]
                ]
            )
            await callback_query.message.answer(
                "⚠️ Telegram не смог загрузить файл. Но вы можете скачать его по ссылке:",
                reply_markup=keyboard,
            )


# === Отмена ===
@router.callback_query(lambda c: c.data == "cancel")
async def process_cancel(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer("❌ Отмена")
