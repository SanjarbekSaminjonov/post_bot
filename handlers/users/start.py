from aiogram import types
from data.config import FORCED_CHANNELS as CHANNELS
from keyboards.inline.subscription import check_button
from keyboards.default.main_buttons import buttons, cancel
from loader import bot, dp
from aiogram.dispatcher import FSMContext
from utils.misc import subscription


@dp.message_handler(commands=['start'], state='*')
async def show_channels(message: types.Message, state: FSMContext):
    await state.finish()
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()

        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    a = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"<b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"

        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
            a = False

    await call.message.answer(result, reply_markup=check_button, disable_web_page_preview=True)

    await call.message.answer("Harakatlardan birni tanlang!", reply_markup=buttons)
