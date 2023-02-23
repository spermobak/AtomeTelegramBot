from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_LOGIN = InlineKeyboardButton('Зарегистрироваться', callback_data='login')
BTN_SOCIAL_MEDIA = InlineKeyboardButton('Связаться с нами', callback_data='social_media')
BTN_FAQ = InlineKeyboardButton('Часто задаваемые вопросы', callback_data='faq')

BTN_INSTAGRAM = InlineKeyboardButton('Instagram', url='https://open.spotify.com/track/1wTopxO5eQBpxrBXPSbsUn?si=94b14ecffde5427e')
BTN_OK = InlineKeyboardButton('OK.ru', url='https://open.spotify.com/track/5bknBRjKJZ643DAN2w8Yoy?si=de2e819e60be4322')
BTN_GEM4ME = InlineKeyboardButton('Gem4me', url='https://open.spotify.com/track/3LVveFLGPaumoHbk7Xpzkf?si=d6ada89e341d4f42')

BTN_HELP = InlineKeyboardButton('Помощь', callback_data='help')

MENU = InlineKeyboardMarkup().add(BTN_LOGIN).add(BTN_SOCIAL_MEDIA).add(BTN_FAQ)
LOGIN = InlineKeyboardMarkup().add(BTN_SOCIAL_MEDIA).add(BTN_FAQ)
SOCIAL_MEDIA = InlineKeyboardMarkup().add(BTN_INSTAGRAM).add(BTN_OK).add(BTN_GEM4ME).add(BTN_HELP)
FAQ = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA)
HELP = InlineKeyboardMarkup().add(BTN_LOGIN, BTN_SOCIAL_MEDIA).add(BTN_FAQ)
