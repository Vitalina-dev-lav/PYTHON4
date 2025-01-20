from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Стоимость'),
            KeyboardButton(text="О нас")
        ]

    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя Игра", callback_data='medium')],
        [InlineKeyboardButton(text="", callback_data="big")],
        [InlineKeyboardButton(text="", callback_data="mega")],
        [InlineKeyboardButton(text="",callback_data="other")]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url="http://ya.ru")]
    ]
)