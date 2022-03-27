from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📝 E'lon berish"),
            KeyboardButton("📖 Admin haqida ma'lumot")
        ]
    ],
    resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("❌ Bekor qilish")
        ]
    ],
    resize_keyboard=True
)
