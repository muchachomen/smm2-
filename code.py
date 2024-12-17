import telebot
from telebot import types


TOKEN = '7903869154:AAGdvwKEAQh1Kq8tQ76TYosrrdbLYfelcXs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\ud83d\udcbc Создать новый заказ", callback_data='create_order'))
    markup.add(types.InlineKeyboardButton("\ud83d\udcc4 Мои заказы", callback_data='my_orders'))
    markup.add(types.InlineKeyboardButton("\ud83d\udcb3 Мой баланс", callback_data='my_balance'))
    markup.add(types.InlineKeyboardButton("\ud83d\ude80 Заработать", callback_data='earn'))
    markup.add(types.InlineKeyboardButton("\ud83d\udcd6 Помощь", callback_data='help'))
    markup.add(types.InlineKeyboardButton("FAQ", callback_data='faq'))
    markup.add(types.InlineKeyboardButton("\ud83d\udcc5 Чеки", callback_data='receipts'))
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_menu(call):
    if call.data == 'create_order':
        show_create_order_menu(call.message)
    elif call.data == 'my_orders':
        show_my_orders(call.message)
    elif call.data == 'my_balance':
        show_balance(call.message)
    elif call.data == 'earn':
        show_earn_menu(call.message)
    elif call.data == 'help':
        show_help(call.message)
    elif call.data == 'faq':
        show_faq(call.message)
    elif call.data == 'receipts':
        show_receipts(call.message)



def show_create_order_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Создание нового заказа пока в разработке.", message.chat.id, message.message_id, reply_markup=markup)

def show_my_orders(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Ваши заказы пока недоступны.", message.chat.id, message.message_id, reply_markup=markup)

def show_balance(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Ваш текущий баланс: 0 руб.", message.chat.id, message.message_id, reply_markup=markup)

def show_earn_menu(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Раздел заработка пока в разработке.", message.chat.id, message.message_id, reply_markup=markup)

def show_help(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Помощь:\n1. Для создания заказа выберите соответствующий пункт.", message.chat.id, message.message_id, reply_markup=markup)

def show_faq(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("FAQ:\nЧасто задаваемые вопросы будут здесь.", message.chat.id, message.message_id, reply_markup=markup)

def show_receipts(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("\u2b05\ufe0f Назад", callback_data='back_to_main'))
    bot.edit_message_text("Ваши чеки пока недоступны.", message.chat.id, message.message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'back_to_main')
def back_to_main_menu(call):
    main_menu(call.message)


bot.polling(none_stop=True)
