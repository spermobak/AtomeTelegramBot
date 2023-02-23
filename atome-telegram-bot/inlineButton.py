from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOGIN = InlineKeyboardButton('Зарегистрироваться', callback_data='login')
BTN_SOCIAL_MEDIA = InlineKeyboardButton('Связаться с нами', callback_data='social_media')
BTN_FAQ = InlineKeyboardButton('Часто задаваемые вопросы', callback_data='faq')

BTN_INSTAGRAM = InlineKeyboardButton('Instagram', callback_data='instagram')
BTN_OK = InlineKeyboardButton('OK.ru', callback_data='ok.ru')
BTN_GEM4ME = InlineKeyboardButton('Gem4me', callback_data='gem4me')

LOGIN = InlineKeyboardMarkup().add(BTN_SOCIAL_MEDIA, BTN_FAQ)
SOCIAL_MEDIA = InlineKeyboardMarkup().add(BTN_INSTAGRAM).add(BTN_OK).add(BTN_GEM4ME)
FAQ = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA)
HELP = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA).add(BTN_FAQ)
