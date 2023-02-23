from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOGIN = InlineKeyboardButton('Зарегистрироваться', callback_data='login')
BTN_SOCIAL_MEDIA = InlineKeyboardButton('Связаться с нами', callback_data='social_media')
BTN_FAQ = InlineKeyboardButton('Часто задаваемые вопросы', callback_data='faq')

LOGIN = InlineKeyboardMarkup().add(BTN_SOCIAL_MEDIA, BTN_FAQ)
SOCIAL_MEDIA = InlineKeyboardMarkup().add(BTN_LOGIN).add(BTN_FAQ)
FAQ = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA)
HELP = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA).add(BTN_FAQ)
