from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Обрати місто')],
                                              [KeyboardButton(text='Допомога')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Оберіть пункт меню')
