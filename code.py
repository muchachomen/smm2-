import telebot
from telebot import types


TOKEN = '7903869154:AAGdvwKEAQh1Kq8tQ76TYosrrdbLYfelcXs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk = types.KeyboardButton("Создать новый заказ")
    mrk1 = types.KeyboardButton("Мои заказы")
    mrk2 = types.KeyboardButton("Мой баланс")
    mrk3 = types.KeyboardButton("Заработать")
    mrk4 = types.KeyboardButton("Помощь")
    mrk5 = types.KeyboardButton("FAQ")
    mrk6 = types.KeyboardButton("Чеки")
    # markup.add(types.InlineKeyboardButton("\ud83d\udcc4 Мои заказы", callback_data='my_orders'))
    # markup.add(types.InlineKeyboardButton("\ud83d\udcb3 Мой баланс", callback_data='my_balance'))
    # markup.add(types.InlineKeyboardButton("\ud83d\ude80 Заработать", callback_data='earn'))
    # markup.add(types.InlineKeyboardButton("\ud83d\udcd6 Помощь", callback_data='help'))
    # markup.add(types.InlineKeyboardButton("FAQ", callback_data='faq'))
    # markup.add(types.InlineKeyboardButton("\ud83d\udcc5 Чеки", callback_data='receipts'))
    markup.add(mrk,mrk1, mrk2, mrk3, mrk4, mrk5, mrk6)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def handle_menu(call):
#     if call.data == 'create_order':
#         show_create_order_menu(call.message)
#     elif call.data == 'my_orders':
#         show_my_orders(call.message)
#     elif call.data == 'my_balance':
#         show_balance(call.message)
#     elif call.data == 'earn':
#         show_earn_menu(call.message)
#     elif call.data == 'help':
#         show_help(call.message)
#     elif call.data == 'faq':
#         show_faq(call.message)
#     elif call.data == 'receipts':
#         show_receipts(call.message)



# Функция для показа меню создания заказа
# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def start_text(message):
    if message.text == "Создать новый заказ":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)
def show_my_orders(message):
    if message.text == "Мои заказы":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Корзина")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)
def show_balance(message):
    if message.text == "Мой баланс":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)

def show_earn_menu(message):
    if message.text == "Заработать":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)

def show_help(message):
    if message.text == "Помощь":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)

def show_faq(message):
    if message.text == "FAQ":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)

def show_receipts(message):
    if message.text == "Чеки":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Одежда")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)
    elif message.text == "Назад в меню":
        main_menu(message)






bot.polling(none_stop=True)
