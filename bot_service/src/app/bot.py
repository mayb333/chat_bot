import asyncio
from loguru import logger

from src.app.loader import bot, dp
from src.handlers.commands import router as router_commands
from src.handlers.dialog import router as router_dialog
from src.handlers.callbacks import router as router_callbacks


class BankChatBot:
    def __init__(self):
        """
        Initializes the object and registers the startup and shutdown events.
        Also includes the specified routers for commands, callbacks, and dialog.
        """
        dp.startup.register(self.startup_event)
        dp.shutdown.register(self.shutdown_event)

        dp.include_router(router_commands)
        dp.include_router(router_dialog)
        dp.include_router(router_callbacks)
 
    async def start(self):
        """
        Starts the bot by polling the dispatcher.
        """
        await dp.start_polling(bot)

    async def startup_event(self):
        """
        An asynchronous function to handle the startup event. It sets the bot commands and logs a warning message.
        """
        logger.warning("Registered commands")
        logger.warning("Bot started")

    async def shutdown_event(self):
        """
        Asynchronous function to handle the shutdown event of the bot.
        """
        logger.warning("Bot stopped")


if __name__ == "__main__":
    bot_runner = BankChatBot()
    asyncio.run(bot_runner.start())