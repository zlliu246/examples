from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher

# Telegram bot token goes here
# IMPORTANT - remmeber to use .env files if you're committing to a public repository on github
TOKEN="1728636860:abcdefghijklmnop"

def route(update, context):
    text = update.message.text
    update.message.reply_text(text)

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
updater.start_polling()

print("telegram bot is running!")

updater.idle()

