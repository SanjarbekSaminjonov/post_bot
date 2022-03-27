from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action", "user", "post_message_id")


def create_post_cancel_button(user, post_message_id):
    confirmation_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🆗 Chop etish",
                    callback_data=post_callback.new(
                        action="post",
                        user=user,
                        post_message_id=post_message_id
                    )
                ),
                InlineKeyboardButton(
                    text="❌ Rad etish",
                    callback_data=post_callback.new(
                        action="cancel",
                        user=user,
                        post_message_id=post_message_id
                    )
                ),
            ]
        ]

    )
    return confirmation_keyboard
