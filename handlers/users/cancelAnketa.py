from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.main_buttons import buttons


@dp.message_handler(text="❌ Bekor qilish", state='*')
async def about_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Bekor qilindi!", reply_markup=buttons)  # ADMIN HAQIDA MA"LUMOT