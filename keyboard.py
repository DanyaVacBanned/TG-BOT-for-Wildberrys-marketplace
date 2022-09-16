from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button_help = KeyboardButton('/help')
button_start = KeyboardButton('Приступить')

Keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

Keyboard.add(button_start).add(button_help)
btnPay_inline = InlineKeyboardMarkup(row_width=1)
btnPay = InlineKeyboardButton(text='Оплатить', callback_data='payment')
btnPay_inline.insert(btnPay)