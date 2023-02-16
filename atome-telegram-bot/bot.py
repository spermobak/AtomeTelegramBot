import logging
import config
import messages

from aiogram import Bot, Dispatcher, executor, types
from buttons import keyboardButton, inlineButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("text", reply_markup=keyboardButton.START)


@dp.callback_query_handler(text='social_network')
async def process_callback_social_media(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=messages.social_media(),
        reply_markup=inlineButton.SOCIAL_MEDIA
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
