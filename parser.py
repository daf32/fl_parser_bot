from buttons import *
import requests
from bs4 import BeautifulSoup
import telebot
URL='https://www.fl.ru/projects/category/programmirovanie/'
pages = {1:'?kind=5', 2:'?page=2&kind=5',3:'?page=3&kind=5',4:'?page=4&kind=5',5:'?page=5&kind=5',6:'?page=6&kind=5'}
page = 1
def parsing(URL):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    orders = soup.find_all(name='a',class_='b-post__link')
    order = ''
    for i in range(int(len(orders))):
        order += f'{i+1}. {orders[i].text}\n'
    return order
bot = telebot.TeleBot('5522962137:AAFf59l06mGDxEgKRhUOjzljnPCWHM3HjPc')
@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=["start"])
def send_text(message):
    if message.text.lower() == '/start' or message.text.lower() == '/старт' or message.text.lower() == 'start' or message.text.lower() == 'старт':
        bot.send_message(message.chat.id,
                         f'Страница {page}:\n{parsing(URL+pages[page])}',reply_markup=start_markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global page
    if call.data == 'left':
        if page == 1:
            page=6
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id,
                                  text=f'Страница {page}:\n{parsing(URL+pages[page])}',reply_markup=start_markup)
        else:
            page-=1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'Страница {page}:\n{parsing(URL + pages[page])}', reply_markup=start_markup)
    if call.data == 'right':
        if page==6:
            page=1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'Страница {page}:\n{parsing(URL + pages[page])}', reply_markup=start_markup)
        else:
            page+=1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=f'Страница {page}:\n{parsing(URL + pages[page])}', reply_markup=start_markup)
bot.polling()