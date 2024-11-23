from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu =  ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="royxatdan otish"),
            KeyboardButton(text="bot haqida"),
            KeyboardButton(text="kurslar")

        ],
        [
            KeyboardButton(text="statiska"),
            KeyboardButton(text="hamyon")
        ]
    ],
    resize_keyboard=True
)