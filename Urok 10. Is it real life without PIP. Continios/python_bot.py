from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, Updater, CallbackQueryHandler
from bot_commands import *
from credits import bot_token

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("hi", hi_commands))
app.add_handler(CommandHandler("time", time_commands))
app.add_handler(CommandHandler("help", help_commands))
app.add_handler(CommandHandler("sum", sum_commands))
# app.add_handler(CommandHandler("choise", choise_buttons))
app.add_handler(CallbackQueryHandler("menu", build_menu))
print('server started!')
app.run_polling()