from aiogram import Bot, Dispatcher, executor, types
#from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup, InlineKeyboardButton
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)



async def on_startup(_):
    await db.db_start()
    print('Бот запущен!')


@dp.message_handler(commands=['start'])
async def cmd_stat(message: types.message):
    await message.answer_sticker('CAACAgIAAxkBAAMdZK6VIgzmTEVQzdkYOqLA91KY5tcAAhoAA8A2TxOC27C1PAZBVy8E')
    await message.answer (f'{message.from_user.first_name} Пиздуй отсюда',
                          reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Ви авторизувались як Аміністратор!', reply_markup=kb.main_admin)

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')
@dp.message_handler(text='Взяти тачку')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')

@dp.message_handler(text='Сдати тачку')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')

@dp.message_handler(text='Передати показник')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')


@dp.message_handler(text='Інформація')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте',reply_markup=kb.catalog_list)

@dp.message_handler(text='Адмін-панель')
async def takecar(massage: types.Message):
    if massage.from_user.id == int(os.getenv('ADMIN_ID')):
        await massage.answer(f'Ви увійшли в адмін панель!', reply_markup=kb.admin_panel)
    else:
        await massage.reply('воу-воу ти не Адмін')

#@dp.message_handler(content_types=['start'])
#async def chek_stiker(messege: types.Message):
#    await messege.answer_sticker('CAACAgIAAxkBAAMdZK6VIgzmTEVQzdkYOqLA91KY5tcAAhoAA8A2TxOC27C1PAZBVy8E')
#    await messege.answer(f'{messege.form_user.first_name}, Пиздуй отсюда ')

@dp.message_handler(content_types=['sticker'])
async def chek_stiker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id,message.chat.id)

@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id,message.message_id)

async def answer(message: types.Message):
    await message.reply('Ты втираешь мне дичь')


@dp.message_handler()
async  def callback_query_keyboadr(callback_query: types.CallbackQuery):
    if callback_query.data == 'sneakers':
        await bot.send_message(chat_id=callback_query.from_user.id, text='время хоперблок')






if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
