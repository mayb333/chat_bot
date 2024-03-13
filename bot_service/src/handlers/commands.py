from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command(commands="start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет, Я чат-бот для Банка России. Можешь задать мне вопрос")
