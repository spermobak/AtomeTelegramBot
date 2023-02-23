import logging

from aiogram import Bot, Dispatcher, executor, types

import inlineButton
import messages
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'login'])
async def show_command(message: types.Message):
    await message.answer(text=messages.login(),
                         reply_markup=inlineButton.LOGIN)


async def on_startup(dp: Dispatcher) -> None:
    await bot.set_my_commands([
        types.BotCommand("start", "it is start command...")
    ])


@dp.message_handler(commands='help')
async def show_help_message(message: types.Message):
    await message.answer(text=f'This bot can get the current weather from your IP address.',
                         reply_markup=inlineButton.HELP)


@dp.message_handler(commands='social_media')
async def show_social_media(message: types.Message):
    await message.answer(text=messages.social_media(), reply_markup=inlineButton.SOCIAL_MEDIA)


@dp.message_handler(commands='faq')
async def show_faq(message: types.Message):
    await message.answer(text=messages.faq(), reply_markup=inlineButton.FAQ)


@dp.callback_query_handler(text='login')
async def process_callback_weather(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.login(),
        reply_markup=inlineButton.LOGIN
    )


@dp.callback_query_handler(text='social_media')
async def process_callback_wind(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.social_media(),
        reply_markup=inlineButton.SOCIAL_MEDIA
    )


@dp.callback_query_handler(text='faq')
async def process_callback_sun_time(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.faq(),
        reply_markup=inlineButton.FAQ
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
