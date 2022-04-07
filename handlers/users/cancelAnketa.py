from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.main_buttons import buttons

import os


@dp.message_handler(text="❌ Bekor qilish", state='*')
async def cancel_post(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if 'accountImage' in data:
        photo_link = data.get('accountImage')
        os.remove(photo_link)
    await state.finish()
    await message.answer("Bekor qilindi!", reply_markup=buttons)