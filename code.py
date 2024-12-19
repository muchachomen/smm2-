import sqlite3
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
    items = [1, 2, 3, 4]
    if message.text == "Создать новый заказ":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar = types.KeyboardButton("Товары")
        mar2 = types.KeyboardButton("Назад в меню")
        markup1.add(mar, mar2)
        bot.send_message(message.chat.id,"Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1)

    elif message.text == "Товары":
        bot.get_file(items)
    elif message.text == "Назад в меню":
        main_menu(message)
    elif message.text == "Мои заказы":
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1 = types.KeyboardButton("Корзина")
        mar3 = types.KeyboardButton("Назад в меню")
        markup2.add(mar1, mar3)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup2)
    elif message.text == "Назад в меню":
        main_menu()


    elif message.text == "Мой баланс":
        markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar0 = types.KeyboardButton("Одежда")
        mar23= types.KeyboardButton("Назад в меню")
        markup11.add(mar0, mar23)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup11)
    elif message.text == "Назад в меню":
        main_menu()

    elif message.text == "Заработать":
        markup1w = types.ReplyKeyboardMarkup(resize_keyboard=True)
        marw = types.KeyboardButton("Одежда")
        mar22 = types.KeyboardButton("Назад в меню")
        markup1w.add(marw, mar22)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1w)
    elif message.text == "Назад в меню":
        main_menu()

    elif message.text == "Помощь":
        markup1q = types.ReplyKeyboardMarkup(resize_keyboard=True)
        marq = types.KeyboardButton("Одежда")
        mar2q = types.KeyboardButton("Назад в меню")
        markup1q.add(marq, mar2q)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1q)
    elif message.text == "Назад в меню":
        main_menu()

    elif message.text == "FAQ":
        markup1r = types.ReplyKeyboardMarkup(resize_keyboard=True)
        marr = types.KeyboardButton("Одежда")
        mar2r = types.KeyboardButton("Назад в меню")
        markup1r.add(marr, mar2r)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1r)
    elif message.text == "Назад в меню":
        main_menu()

    elif message.text == "Чеки":
        markup1e = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mare = types.KeyboardButton("Одежда")
        mar2e = types.KeyboardButton("Назад в меню")
        markup1e.add(mare, mar2e)
        bot.send_message(message.chat.id,
                         "Выберите, что вам нужно, если хотите вернуться в меню просто нажмите кнопку 'Назад в меню'.",
                         reply_markup=markup1e)
    elif message.text == "Назад в меню":
        main_menu()






bot.polling(none_stop=True)
