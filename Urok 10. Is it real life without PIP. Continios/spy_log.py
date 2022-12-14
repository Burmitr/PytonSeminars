from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater, CallbackQueryHandler

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('db.csv', 'a') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, '
                   f'{update.message.date}\n')
