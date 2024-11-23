import asyncio
import logging
import sys
from os import getenv

from keyboard import main_keyboard
from time_file import formatted_time

from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token='7672929489:AAEO7LFKtXmdoSepJmaAgScFFRnaKMX4-M0')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Вітаю у застосунку, {message.from_user.full_name}!')
    await message.answer(f'Поточний час: {formatted_time}')
    await message.answer('Обери потрібну дію.', reply_markup=main_keyboard)


@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Це вікно допомоги.')
    await message.answer('Щоб отримати актуальну погоду твого міста, просто введи його назву, '
                         'або вибери із найпопулярніших')



async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот спить.')