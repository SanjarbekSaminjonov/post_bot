from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("✅ Ha, Adminga yuborilsin"),
            KeyboardButton("❌ Yo'q xatolik bor")
        ]
    ],
    resize_keyboard=True
)
