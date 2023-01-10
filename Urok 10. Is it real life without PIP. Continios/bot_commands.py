import requests
from bs4 import BeautifulSoup as bs
import logging
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater, CallbackQueryHandler
import datetime
from spy_log import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Приветствие от бота
async def hi_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# Вывод списка доступных команд
async def help_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/sum\n/choise\n/help')

# Вывод текущего времени
async def time_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

# Суммирование двух чисел через пробел
async def sum_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

# Создание меню
async def build_menu(buttons, n_cols,
                     header_buttons=None,
                     footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

    button_list = [InlineKeyboardButton('ххххх', callback_data='1'), InlineKeyboardButton('yyyyyy', callback_data='2')]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    await bot.send_message(chat_id=chat_id, text='Меню из двух столбцов', reply_markup=reply_markup)

# парсер для кнопок
# url = 'https://anekdoty.ru/'
# response = requests.get(url).text
# soup = bs(response, 'html.parser')
# anekdot = soup.find('div', class_='holder-body')
# print(anekdot.text)






# Вывод кнопок выбора запрашиваемых пользователем данных
# async def choise_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     log(update, context)
#     Keyboard = [InlineKeyboardButton('ххххх', callback_data='1'), InlineKeyboardButton('yyyyyy', callback_data='2')]
#     await update.message.reply_text('Какие данные вы желаете получить?', reply_markup=InlineKeyboardMarkup(Keyboard))

# Программируем кнопки
# async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     log(update, context)
#     query = update.callback_query
#     query.answer()
#     if query.data == '1':
#         await context.bot.send_message(update.effective_chat.id, 'ххххх')
#     elif query.data == '2':
#         await context.bot.send_message(update.effective_chat.id, 'yyyyyy')




