import telebot
import requests
from bs4 import BeautifulSoup as b
from telebot import types
import configparser 
bot = telebot.TeleBot("5580767673:AAG4LKS7lEEXL0H5bjBYocVfikIzI2vtv_o")

url_brest = "https://select.by/brest/kurs"
r_brest = requests.get(url_brest)
soup_brest = b(r_brest.text, 'html.parser')
rate_brest = soup_brest.find_all("span", itemprop="price")
clear_rate_brest = []
for i in rate_brest:
    clear_rate_brest.append(i.text)

url_grodno = "https://select.by/grodno/kurs"
r_grodno = requests.get(url_grodno)
soup_grodno = b(r_grodno.text, 'html.parser')
rate_grodno = soup_grodno.find_all("span", itemprop="price")
clear_rate_grodno = []
for i in rate_grodno:
    clear_rate_grodno.append(i.text)

url_vitebsk = "https://select.by/vitebsk/kurs"
r_vitebsk = requests.get(url_vitebsk)
soup_vitebsk = b(r_vitebsk.text, 'html.parser')
rate_vitebsk = soup_vitebsk.find_all("span", itemprop="price")
clear_rate_vitebsk = []
for i in rate_vitebsk:
    clear_rate_vitebsk.append(i.text)

url_gomel = "https://select.by/gomel/kurs"
r_gomel = requests.get(url_gomel)
soup_gomel = b(r_gomel.text, 'html.parser')
rate_gomel = soup_gomel.find_all("span", itemprop="price")
clear_rate_gomel = []
for i in rate_gomel:
    clear_rate_gomel.append(i.text)

url_mogilev = "https://select.by/mogilev/kurs"
r_mogilev = requests.get(url_mogilev)
soup_mogilev = b(r_mogilev.text, 'html.parser')
rate_mogilev = soup_mogilev.find_all("span", itemprop="price")
clear_rate_mogilev = []
for i in rate_mogilev:
    clear_rate_mogilev.append(i.text)

url_minsk = "https://select.by/minsk/kurs"
r_minsk = requests.get(url_minsk)
soup_minsk = b(r_minsk.text, 'html.parser')
rate_minsk = soup_minsk.find_all("span", itemprop="price")
clear_rate_minsk = []
for i in rate_minsk:
    clear_rate_minsk.append(i.text)

url_NB = "https://select.by/kursy-valyut/natsbank-rb"
r_NB = requests.get(url_NB)
soup_NB = b(r_NB.text, 'html.parser')
rate_NB = soup_NB.find_all("span", itemprop="price")
clear_rate_NB = []
for i in rate_NB:
    clear_rate_NB.append(i.text)

dollar_brest = f'🇺🇸      *1 USD:* покупка {clear_rate_brest[0]}, продажа {clear_rate_brest[1]}'
euro_brest = f'🇪🇺      *1 EUR:* покупка {clear_rate_brest[2]}, продажа {clear_rate_brest[3]}'
ros_rubel_brest = f'🇷🇺 *100 RUB:* покупка {clear_rate_brest[4]}, продажа {clear_rate_brest[5]}'
zl_brest = f'🇵🇱   *10 PLN:* покупка {clear_rate_brest[6]}, продажа {clear_rate_brest[7]}'

dollar_grodno = f'🇺🇸      *1 USD:* покупка {clear_rate_grodno[0]}, продажа {clear_rate_grodno[1]}'
euro_grodno = f'🇪🇺      *1 EUR:* покупка {clear_rate_grodno[2]}, продажа {clear_rate_grodno[3]}'
ros_rubel_grodno = f'🇷🇺 *100 RUB:* покупка {clear_rate_grodno[4]}, продажа {clear_rate_grodno[5]}'
zl_grodno = f'🇵🇱   *10 PLN:* покупка {clear_rate_grodno[6]}, продажа {clear_rate_grodno[7]}'

dollar_vitebsk = f'🇺🇸      *1 USD:* покупка {clear_rate_vitebsk[0]}, продажа {clear_rate_vitebsk[1]}'
euro_vitebsk = f'🇪🇺      *1 EUR:* покупка {clear_rate_vitebsk[2]}, продажа {clear_rate_vitebsk[3]}'
ros_rubel_vitebsk = f'🇷🇺 *100 RUB:* покупка {clear_rate_vitebsk[4]}, продажа {clear_rate_vitebsk[5]}'
zl_vitebsk = f'🇵🇱   *10 PLN:* покупка {clear_rate_vitebsk[6]}, продажа {clear_rate_vitebsk[7]}'

dollar_gomel = f'🇺🇸      *1 USD:* покупка {clear_rate_gomel[0]}, продажа {clear_rate_gomel[1]}'
euro_gomel = f'🇪🇺      *1 EUR:* покупка {clear_rate_gomel[2]}, продажа {clear_rate_gomel[3]}'
ros_rubel_gomel = f'🇷🇺 *100 RUB:* покупка {clear_rate_gomel[4]}, продажа {clear_rate_gomel[5]}'
zl_gomel = f'🇵🇱   *10 PLN:* покупка {clear_rate_gomel[6]}, продажа {clear_rate_gomel[7]}'

dollar_mogilev = f'🇺🇸      *1 USD:* покупка {clear_rate_mogilev[0]}, продажа {clear_rate_mogilev[1]}'
euro_mogilev = f'🇪🇺      *1 EUR:* покупка {clear_rate_mogilev[2]}, продажа {clear_rate_mogilev[3]}'
ros_rubel_mogilev = f'🇷🇺 *100 RUB:* покупка {clear_rate_mogilev[4]}, продажа {clear_rate_mogilev[5]}'
zl_mogilev = f'🇵🇱   *10 PLN:* покупка {clear_rate_mogilev[6]}, продажа {clear_rate_mogilev[7]}'

dollar_minsk = f'🇺🇸      *1 USD:* покупка {clear_rate_minsk[0]}, продажа {clear_rate_minsk[1]}'
euro_minsk = f'🇪🇺      *1 EUR:* покупка {clear_rate_minsk[2]}, продажа {clear_rate_minsk[3]}'
ros_rubel_minsk = f'🇷🇺 *100 RUB:* покупка {clear_rate_minsk[4]}, продажа {clear_rate_minsk[5]}'
zl_minsk = f'🇵🇱   *10 PLN:* покупка {clear_rate_minsk[6]}, продажа {clear_rate_minsk[7]}'

dollar_NB = f'🇺🇸      *1 USD*   {clear_rate_NB[0]}'
euro_NB = f'🇪🇺      *1 EUR*   {clear_rate_NB[1]}'
ros_rubel_NB = f'🇷🇺 *100 RUB*   {clear_rate_NB[2]}'
zl_NB = f'🇵🇱    *10 PLN*   {clear_rate_NB[3]}'

markup1 = types.InlineKeyboardMarkup(row_width=1)
item_rate = types.InlineKeyboardButton("Узнать курсы валют в моем городе", callback_data="rate")
item_NB = types.InlineKeyboardButton("Узнать курсы Нацбанка РБ", callback_data="NB")
markup1.add(item_rate, item_NB)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который расскажет о курсах валют в РБ 🇧🇾", reply_markup=markup1)

markup3= types.InlineKeyboardMarkup()
item_back = types.InlineKeyboardButton("Вернуться назад", callback_data="back")
markup3.add(item_back)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == "rate":
            markup2 = types.InlineKeyboardMarkup()
            item_brest = types.InlineKeyboardButton("Брест", callback_data="brest")
            item_grodno = types.InlineKeyboardButton("Гродно", callback_data="grodno")
            item_vitebsk = types.InlineKeyboardButton("Витебск", callback_data="vitebsk")
            item_gomel = types.InlineKeyboardButton("Гомель", callback_data="gomel")
            item_mogilev = types.InlineKeyboardButton("Могилев", callback_data="mogilev")
            item_minsk = types.InlineKeyboardButton("Минск", callback_data="minsk")
            item_back = types.InlineKeyboardButton("Вернуться назад", callback_data="back")
            markup2.add(item_brest,item_vitebsk,item_gomel, item_grodno, item_minsk, item_mogilev)
            bot.send_message(call.message.chat.id, "Выберите Ваш город", reply_markup=markup2)
        elif call.data == "brest":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Бресте на сегодня:* \n \n {dollar_brest} \n {euro_brest} \n {ros_rubel_brest} \n {zl_brest}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "grodno":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Гродно на сегодня:* \n \n {dollar_grodno} \n {euro_grodno} \n {ros_rubel_grodno} \n {zl_grodno}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "vitebsk":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Витебске на сегодня:* \n \n {dollar_vitebsk} \n {euro_vitebsk} \n {ros_rubel_vitebsk} \n {zl_vitebsk}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "gomel":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Гомеле на сегодня:* \n \n {dollar_gomel} \n {euro_gomel} \n {ros_rubel_gomel} \n {zl_gomel}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "mogilev":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Могилеве на сегодня:* \n \n {dollar_mogilev} \n {euro_mogilev} \n {ros_rubel_mogilev} \n {zl_mogilev}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "minsk":
                bot.send_message(call.message.chat.id, f'*Курсы валют в Минске на сегодня:* \n \n {dollar_minsk} \n {euro_minsk} \n {ros_rubel_minsk} \n {zl_minsk}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "NB":
                bot.send_message(call.message.chat.id, f'*Курсы валют Нацбанка РБ на сегодня:* \n \n {dollar_NB} \n {euro_NB} \n {ros_rubel_NB} \n {zl_NB}', reply_markup=markup3, parse_mode="Markdown")
        elif call.data == "back":
                bot.send_message(call.message.chat.id, "Привет! Я бот, который расскажет о курсах валют в РБ 🇧🇾", reply_markup=markup1)


bot.polling(none_stop=True)