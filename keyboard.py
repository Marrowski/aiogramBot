from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Обрати місто')],
                                              [KeyboardButton(text='Найпопулярніші міста')]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Оберіть пункт меню')