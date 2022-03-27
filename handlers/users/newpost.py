from os import remove as remove_photo

from aiogram.types import InputFile
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from loader import dp, bot

from keyboards.default import confirmKeys, main_buttons
from keyboards.inline.manage_post import create_post_cancel_button, post_callback
from data.config import ADMINS, CHANNELS
from states.newpost import AccountData

from .makePostCaption import make_post_caption


@dp.message_handler(text="📖 Admin haqida ma'lumot")
async def about_admin(message):
    text = "♻️ Bot @PesUzTime kanalining rasmiy boti hisoblanadi. " \
           "Botning asosiy vazifasi `Sale` kanal uchun post joylash ✅\n"
    text += "♻️ Bot admini - @mamajonoff ✅\n"
    text += "📝 Savol yoki takliflar boʻlsa adminga murojaat qiling ✅"
    await message.answer(text)  # ADMIN HAQIDA MA"LUMOT


@dp.message_handler(text_contains="E'lon berish")
async def create_post(message: Message, state: FSMContext):
    await message.answer("Account rasmini yuboring", reply_markup=main_buttons.cancel)
    await AccountData.accountImage.set()


@dp.message_handler(content_types=['photo'], state=AccountData.accountImage)
async def create_post(message: Message, state: FSMContext):
    file_name = str(message.from_user.id) + '_' + str(message.message_id) + '.png'
    try:
        await message.photo[-1].download(file_name)
    except:
        file_name = 'no_image.png'
    await state.update_data({'accountImage': file_name})
    await message.answer("Nima qilmoqchisiz (sotiladi yoki obmen)")
    await AccountData.sellingType.set()


@dp.message_handler(state=AccountData.sellingType)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'sellingType': message.text})
    await message.answer("Jami oʻyinchilar soni?")
    await AccountData.allPlayersCount.set()


@dp.message_handler(state=AccountData.allPlayersCount)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'allPlayersCount': message.text})
    await message.answer("FT oʻyinchilar soni?")
    await AccountData.ftPlayersCount.set()


@dp.message_handler(state=AccountData.ftPlayersCount)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'ftPlayersCount': message.text})
    await message.answer("IM oʻyinchilar soni?")
    await AccountData.imPlayersCount.set()


@dp.message_handler(state=AccountData.imPlayersCount)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'imPlayersCount': message.text})
    await message.answer('Legend oʻyinchilar soni?')
    await AccountData.legendPlayersCount.set()


@dp.message_handler(state=AccountData.legendPlayersCount)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'legendPlayersCount': message.text})
    await message.answer('Coins soni?')
    await AccountData.coinsCount.set()


@dp.message_handler(state=AccountData.coinsCount)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'coinsCount': message.text})
    await message.answer('Akkount narxini kiriting')
    await AccountData.price.set()


@dp.message_handler(state=AccountData.price)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'price': message.text})
    await message.answer('Shu accountni sotib olish yoki obmen qilish kimga murojaat qilinsin?')
    await AccountData.contact.set()


@dp.message_handler(state=AccountData.contact)
async def create_post(message: Message, state: FSMContext):
    await state.update_data({'contact': message.text})

    data = await state.get_data()
    await state.reset_data()

    text = make_post_caption(data)

    photo_link = data.get('accountImage')
    photo = InputFile(path_or_bytesio=photo_link)

    sent_msg = await message.answer_photo(photo, parse_mode="HTML", caption=text)
    await state.update_data({'message_id': sent_msg.message_id})

    await message.answer("Hammasi tayyor, ma'lumotlar to'g'rimi?", reply_markup=confirmKeys.buttons)

    remove_photo(photo_link)
    await AccountData.finishPost.set()


@dp.message_handler(text_contains="yuborilsin", state=AccountData.finishPost)
async def create_post(message: Message, state: FSMContext):
    data = await state.get_data()

    message_id = data.get('message_id')
    sent_msg = await bot.copy_message(chat_id=ADMINS[0], from_chat_id=message.from_user.id, message_id=message_id)

    mention = message.from_user.get_mention()
    request_buttons = create_post_cancel_button(user=message.from_user.id, post_message_id=str(sent_msg.message_id))

    await bot.send_message(
        chat_id=ADMINS[0],
        text=f"Foydalanuvchi {mention} yuqoridagi e'lonni qoldirdi.",
        reply_markup=request_buttons
    )

    await message.answer(
        "Post tekshiruv uchun adminga yuborildi. Admin tasdiqlasa "
        "@Uzefootball kanaliga joylanadi va bu haqida sizga xabar beriladi.",
        reply_markup=main_buttons.buttons
    )

    await state.finish()


@dp.message_handler(text_contains="Yo'q xatolik bor", state=AccountData.finishPost)
async def create_post(message: Message, state: FSMContext):
    await message.answer("E'lonni bekor qildingiz.", reply_markup=main_buttons.buttons)
    await state.finish()


# Kanal bo'shqaruvi

@dp.callback_query_handler(post_callback.filter(action="post"))
async def approve_post(call: CallbackQuery):
    data = call.data.split(":")
    user_id = data[-2]
    message_id = data[-1]

    await bot.copy_message(chat_id=CHANNELS[0], from_chat_id=ADMINS[0], message_id=message_id)
    await call.answer("Post kanalga joylandi.", show_alert=True)

    await bot.copy_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message_id)
    await bot.send_message(chat_id=user_id, text="Ushbu e'loningiz kanalga joylandi")

    await call.message.edit_reply_markup()


@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def approve_post(call: CallbackQuery):
    data = call.data.split(":")
    user_id = data[-2]
    message_id = data[-1]

    await call.answer("Post rad etildi.", show_alert=True)

    await bot.copy_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message_id)
    await bot.send_message(
        chat_id=user_id,
        text="Ushbu e'loningiz admin tomonidan rad etildi.\nQayta urinib ko'ring, yoki admin bilan bog'laning!"
    )

    await call.message.edit_reply_markup()
