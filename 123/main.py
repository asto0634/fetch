import asyncio
import requests
import random

from mistralai.client import Mistral

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8610973300:AAEqorAKwQtZaIDwwMfWuO-OOiEhVzc-w8Y"

api_key = "4gT2RzghgFoN2mGSbqBp6l920BhHDrlN"
model = "mistral-medium-latest"

client = Mistral(api_key=api_key)

dp = Dispatcher()

def language_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="O'zbek")],
            [KeyboardButton(text="Русский")]
        ],
        resize_keyboard=True
    )

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Top 10 Kino")],
            [KeyboardButton(text="Top 10 Multfilm")],
            [KeyboardButton(text="Top 10 Musiqa")],
            [KeyboardButton(text="Top 10 Oyinlar")]
        ],
        resize_keyboard=True
    )


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Tilni tanlang:",
        reply_markup=language_keyboard()
    )

@dp.message(F.text == "O'zbek")
async def uzbek_handler(message: Message):
    await message.answer(
        "Kerakli bo‘limni tanlang:",
        reply_markup=main_keyboard()
    )

@dp.message(F.text == "Top 10 Kino")
async def top_movies_handler(message: Message):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Answer only in Uzbek language",
            },
            {
                "role": "user",
                "content": "Top 10 kinolar haqida ma'lumot ber",
            },
        ]
    )
    print(message.answer(chat_response.choices[0].message.content))
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")


@dp.message(F.text == "Top 10 Multfilm")
async def top_movies_handler(message: Message):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Answer only in Uzbek language",
            },
            {
                "role": "user",
                "content": "Top 10 Multfilmlar haqida ma'lumot ber",
            },
        ]
    )
    print(message.answer(chat_response.choices[0].message.content))
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")


@dp.message(F.text == "Top 10 Musiqa")
async def top_movies_handler(message: Message):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Answer only in Uzbek language",
            },
            {
                "role": "user",
                "content": "Top 10 Musiqalar haqida ma'lumot ber",
            },
        ]
    )
    print(message.answer(chat_response.choices[0].message.content))
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")


@dp.message(F.text == "Top 10 Oyinlar")
async def top_movies_handler(message: Message):
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "Answer only in Uzbek language",
            },
            {
                "role": "user",
                "content": "Top 10 Oyinlar haqida ma'lumot ber",
            },
        ]
    )
    print(message.answer(chat_response.choices[0].message.content))
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")

async def main():
    bot = Bot(token=TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
