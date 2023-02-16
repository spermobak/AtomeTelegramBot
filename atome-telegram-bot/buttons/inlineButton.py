from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_INSTA = InlineKeyboardButton('Instagram', callback_data='instagram')
BTN_VK = InlineKeyboardButton('Vk', callback_data='vk')
BTN_TELEGRAM = InlineKeyboardButton('Telegram', callback_data='telegram')

SOCIAL_MEDIA = InlineKeyboardMarkup().add(BTN_INSTA).add(BTN_VK).add(BTN_TELEGRAM)