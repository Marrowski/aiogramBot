import asyncio
import requests

from keyboard import main_keyboard
from time_file import formatted_time

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram import Bot, Dispatcher, html, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token='7672929489:AAEO7LFKtXmdoSepJmaAgScFFRnaKMX4-M0')
dp = Dispatcher()
API_KEY = 'a6fb4d9c8a6d29df78711ba6ee93a935'

class WeatherStates(StatesGroup):
    waiting_for_city = State()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Вітаю у застосунку, {message.from_user.full_name}!')
    await message.answer(f'Поточний час: {formatted_time}')
    await message.answer('Обери потрібну дію.', reply_markup=main_keyboard)


@dp.message(F.text == 'Допомога')
async def help(message: Message):
    await message.answer('Це вікно допомоги.')
    await message.answer('Щоб отримати актуальну погоду твого міста, просто введи його назву')


@dp.message(F.text == 'Обрати місто')
async def city(message: Message, state: FSMContext):
    await message.answer('Введіть назву міста(англійською):')
    await state.set_state(WeatherStates.waiting_for_city)

@dp.message(WeatherStates.waiting_for_city)
async def weather_info(message: types.Message, state: FSMContext):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_KEY}')
    json_resp = response.json()
    await message.answer('Інформація про вибране місто')
    await message.answer('------------------------------')
    await message.answer(f'Країна: {json_resp['sys']['country']}\n'
          f'Місто: {json_resp['name']}\n'
          f'Погода:{json_resp['weather'][0]['main']}\n'
          f'Температура:{json_resp['main']['temp'] - 272}\n'
          f'Швидкість вітру:{json_resp['wind']['speed']}')
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот спить.')