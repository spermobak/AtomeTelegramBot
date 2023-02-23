import logging

from aiogram import Bot, Dispatcher, executor, types

import inlineButton
import messages
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'menu'])
async def show_command(message: types.Message):
    await message.answer(text=messages.menu(),
                         reply_markup=inlineButton.MENU)


async def on_startup(dp: Dispatcher) -> None:
    await bot.set_my_commands([
        types.BotCommand('start', 'it is start command...'),
        types.BotCommand('help', 'it is help command...'),
        types.BotCommand('faq', 'it is faq command...'),
        types.BotCommand('login', 'it is login command...')
    ])


@dp.message_handler(commands='help')
async def show_help_message(message: types.Message):
    await message.answer(text=messages.help(),
                         reply_markup=inlineButton.HELP)


@dp.message_handler(commands='social_media')
async def show_social_media(message: types.Message):
    await message.answer(text=messages.social_media(), reply_markup=inlineButton.SOCIAL_MEDIA)


@dp.message_handler(commands='faq')
async def show_faq(message: types.Message):
    await message.answer(text=messages.faq(), reply_markup=inlineButton.FAQ)


@dp.callback_query_handler(text='menu')
async def process_callback_menu(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.menu(),
        reply_markup=inlineButton.MENU
    )


@dp.callback_query_handler(text='help')
async def process_callback_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.help(),
        reply_markup=inlineButton.HELP
    )


@dp.callback_query_handler(text='login')
async def process_callback_login(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.login(),
        reply_markup=inlineButton.LOGIN
    )


@dp.callback_query_handler(text='social_media')
async def process_callback_social_media(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.social_media(),
        reply_markup=inlineButton.SOCIAL_MEDIA
    )


@dp.callback_query_handler(text='faq')
async def process_callback_faq(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.faq(),
        reply_markup=inlineButton.FAQ
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
