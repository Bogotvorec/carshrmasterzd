from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Взяти тачку').add('Сдати звіт').add('Передати показники').add('Політика')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Функції').add('Взяти тачку').add('Сдати звіт').add('Політика').add('Адмін-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('').add('Взяти тачку').add('Сдати звіт').add('Додати користувача').add('Відправити на Бронь')
@dp.message_handler(commands=['start'])
async def cmd_stat(message: types.message):
    await message.answer_sticker('CAACAgIAAxkBAAMdZK6VIgzmTEVQzdkYOqLA91KY5tcAAhoAA8A2TxOC27C1PAZBVy8E')
    await message.answer (f'{message.from_user.first_name} Пиздуй отсюда',
                          reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Ви авторизувались як Аміністратор!', reply_markup=main_admin)

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')
@dp.message_handler(text='Взяти тачку')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')

@dp.message_handler(text='Сдати звіт')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')

@dp.message_handler(text='Функції')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')


@dp.message_handler(text='Політика')
async def takecar(massage: types.Message):
    await massage.answer(f'Машину подано Cер! , ви можете взять ключи в оговоренном месте')

@dp.message_handler(text='Адмін-панель')
async def takecar(massage: types.Message):
    if massage.from_user.id == int(os.getenv('ADMIN_ID')):
        await massage.answer(f'Ви увійшли в адмін панель!', reply_markup=admin_panel)
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

if __name__ == '__main__':
    executor.start_polling(dp)