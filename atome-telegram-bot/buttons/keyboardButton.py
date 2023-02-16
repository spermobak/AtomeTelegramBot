from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

BTN_LOGIN = KeyboardButton('Зарегистрироваться', callbackcallback_data='login')
BTN_SOCIAL_NETWORK = KeyboardButton('Связаться с нами', callback_data='social_network')
BTN_FAQ = KeyboardButton('Часто задаваемые вопросы', callback_data='faq')


START = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        BTN_SOCIAL_NETWORK, BTN_FAQ).add(BTN_LOGIN)
