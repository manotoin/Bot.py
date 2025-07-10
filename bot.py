from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

TOKEN = os.environ.get("TOKEN")  # توکن از متغیر محیطی میاد

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام از Railway! 🚄")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
print("ربات فعال شد!")
