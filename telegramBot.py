import telegram.ext
import pandas_datareader as web

TOKEN = '6243944410:AAEBeLkqU4HrnefHqJWl_sTvksk8GiGv5HY'

def start(update, context):
    update.message.reply_text("Hello! Welcome to AlfredBot")

def help(update, context):
    update.message.reply_text("""
    The Following Commands Are Available:
    
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About Alfred's Content
    /contact -> Information About Contact
    """)

def content (update, context):
        update.message.reply_text("My full name is Ogunbayo Alfred, this was made with python.")

def contact(update, context):
        update.message.reply_text("You can contact AlfredBot on telegram")

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The Current Price of {ticker} is {price:.2f}$!")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")

updater = telegram.ext.Updater(TOKEN, use_context= True)
disp = updater.dispatcher
 
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()


