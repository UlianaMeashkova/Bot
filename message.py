import asyncio
import os

from telegram import Bot

with open("token.txt", "r") as f:
    BOT_TOKEN = f.read()


async def send_message(chat_id: int, text: str) -> None:
    bot = Bot(BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)


if __name__ == "__main__":
    chat_id = input("Enter chat ID: ")
    text = input("Your message: ")
    asyncio.run(send_message(chat_id=chat_id, text=text))
