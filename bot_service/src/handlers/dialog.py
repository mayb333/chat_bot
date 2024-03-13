from aiogram import Router, types

from src.utils.markup import inline_markup


router = Router()

@router.message()
async def answer(message: types.Message):
    query = message.text

    await message.answer("Какой-то ответ", reply_markup=inline_markup(message_id=message.message_id))
