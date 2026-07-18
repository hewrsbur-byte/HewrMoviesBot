from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text(!سڵاو! من بۆتەکەم کاردەککات.')

def main():
    # لێرە تۆکێنەکەت دادەنێین
    updater = Updater("8989364985:AAEwBkvkNjYmxl_GsEXlZPOkuQM50OFagwQ", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

