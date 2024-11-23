from aiogram import types
from loader import dp
from states.sign_up import sign
from keyboards.inline.inline_keys import inline_bt
@dp.message_handler(text="royxatdan otish")
async def replt_royhat(message:types.Message):
    await message.answer("Iltimos, ismingizni kiriting: ")
    await sign.name.set()

@dp.message_handler(text="bot haqida")
async def replt_royhat(message:types.Message):
    await message.answer("<b>bu bot uchun</b> <i>hdgedbikfjr</i> ")


@dp.message_handler(text="kurslar")
async def replt_royhat(message: types.Message):
    await message.answer("<b>bunda kurd</b> ", reply_markup=inline_bt)


@dp.callback_query_handler(text="py")
async def callback_button(call:types.CallbackQuery):
    await call.message.answer("siz pyhon tanlading ")
