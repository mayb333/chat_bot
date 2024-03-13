import aiohttp
from aiogram import Router, types

from src.utils.markup import inline_markup


router = Router()

@router.message()
async def answer(message: types.Message):
    query = message.text

    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://127.0.0.1:8000/predict?query={query}") as response:
            result = await response.json()
            answer = result.get("text", "")
            relevant_urls = result.get("urls", []) 

    print(answer, relevant_urls)

    relevant_docs = [
        f"[Документ {i+1}]({url})" for i, url in enumerate(relevant_urls)
    ]

    result = answer + "\n\n\n" + "• " + "\n• ".join(relevant_docs)

    await message.answer(result, reply_markup=inline_markup(message_id=message.message_id), parse_mode="markdown")
