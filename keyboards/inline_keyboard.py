from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_kb1 = InlineKeyboardButton(text="🎵 MP3", callback_data="download_mp3")
inline_kb2 = InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")

inline_row = InlineKeyboardMarkup(inline_keyboard=[[inline_kb1], [inline_kb2]])
