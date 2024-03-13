from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.utils.schemas import FeedbackCallback


def inline_markup(message_id: int) -> InlineKeyboardMarkup:
    """
    This function creates and returns an InlineKeyboardMarkup with two buttons (👍 and 👎) for user 
    feedback on a message, using the given message_id.
    """
    buttons = [
        InlineKeyboardButton(
            text="👍",
            callback_data=FeedbackCallback(
                type="user_evaluation", message_id=str(message_id), feedback="like"
            ).pack(),
        ),
        InlineKeyboardButton(
            text="👎",
            callback_data=FeedbackCallback(
                type="user_evaluation", message_id=str(message_id), feedback="dislike"
            ).pack(),
        ),
    ]

    return InlineKeyboardMarkup(inline_keyboard=[buttons])