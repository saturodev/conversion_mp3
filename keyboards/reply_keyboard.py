from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание кнопок
button_1 = KeyboardButton(text="🚑Помощь🚑")


# Создание клавиатуры с одной кнопкой в ряду
keyboard_single_row = ReplyKeyboardMarkup(
    keyboard=[[button_1]],
    resize_keyboard=True,  # Изменяет размер клавиатуры под контент
    # one_time_keyboard=True,  # Скрывает клавиатуру после использования
    input_field_placeholder="🔗Пришлите мне ссылку c YouTube",
    # Подсказка в поле ввода
)
