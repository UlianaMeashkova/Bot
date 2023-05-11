import os
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import aioredis



with open("token.txt", "r") as f:
    BOT_TOKEN = f.read()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis = aioredis.from_url("redis://redis")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(
        f"Start chat #{update.effective_chat.id} - username {update.effective_user.first_name}"
    )
    await redis.lpush("chats", update.effective_chat.id)

    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}"
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(
        f"Message {update.message.text} from chat #{update.effective_chat.id}"
    )
    await update.message.reply_text(
        f"Hello {update.effective_user.first_name}"
    )


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()