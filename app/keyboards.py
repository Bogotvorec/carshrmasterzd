from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardButton , InlineKeyboardMarkup



main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Взяти тачку').add('Сдати тачку').add('Передати показники').add('Інформація')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True) #Переменная админ панели (с подстройкой под экран)
main_admin.add('Функції').add('Взяти тачку').add('Сдати тачку').add('Політика').add('Адмін-панель') # перечесление кнопок адмін пан

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('').add('Взяти тачку').add('Сдати звіт').add('Додати користувача').add('Відправити на Бронь')


# = InlineKeyboardMarkup(row_width=2) #інлайн меню
#catalog_list.add(InlineKeyboardButton(text= 'Політика використання', url='https://www.google.com/'),
#                 InlineKeyboardButton(text='Інструкції ',url='https://www.google.com/'),
#                 InlineKeyboardButton(text='Заграбастати тачілу', callback_data='sneakers'))

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', callback_data='t-shirt'),
                 InlineKeyboardButton(text='Шорты', callback_data='shorts'),
                 InlineKeyboardButton(text='Кроссовки', callback_data='sneakers'))