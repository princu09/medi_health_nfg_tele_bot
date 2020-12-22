from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot

updater = Updater("1493323704:AAHuLjTwMhY-KYm0mvQWoM6PUq9mR5VB7Zk", use_context=True)

dispatcher: Dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    bot: Bot = context.bot
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    bot.send_message(chat_id=update.effective_chat.id,text=f"Hello {first_name} {last_name} !! Welcome To Medi Health NFG")

def sendPhoto(update: Update , context: CallbackContext):
    photo = open('logo.png' , 'rb')
    send_caption = '<b>About NFG ℹ️ : \n\nThis is a bot built by Python developer of Northfox Group and this bot is for sending every bill and new information to every customer of Medi Health NFG. \n\nIf you also want this software, you can contact us directly.\n\n<a href="mailto:northfoxgroup@hotmail.com">Mail Us</a> +91 9106693088 </b>'

    bot:Bot = context.bot
    bot.send_photo(chat_id=update.effective_chat.id,photo=photo , caption=send_caption , parse_mode='html')

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("about", sendPhoto))

updater.start_polling()