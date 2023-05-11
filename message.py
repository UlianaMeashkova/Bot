import asyncio
import os
import aioredis
import random

from telegram import Bot

with open("token.txt", "r") as f:
    BOT_TOKEN = f.read()


redis = aioredis.from_url("redis://redis")


async def send_message(chat_id: int, text: str) -> None:
    bot = Bot(BOT_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)

async def send_message_to_all(text: str) -> None:
     for index in range(0,await redis.llen("chats")):
          chat_id = await redis.lindex("chats", index)
          await send_message(chat_id=int(chat_id), text=text)


if __name__ == "__main__":
    # chat_id = int(input("Enter chat ID: "))
    # text = input("Your message: ")
    # asyncio.run(send_message(chat_id=chat_id, text=text))

     text = input("Your message: ")
     asyncio.run(send_message_to_all(text=text))