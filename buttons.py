import telebot

start_markup = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('<=', callback_data='left')
btn2 = telebot.types.InlineKeyboardButton('=>', callback_data='right')
start_markup.row(btn1,btn2)
