from aiogram import Router, types
from aiogram.filters import Command

from src.config import welcome_message

router = Router()


@router.message(Command(commands="start"))
async def send_welcome(message: types.Message):
    await message.answer(welcome_message)
