from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Привет! Я бот.')

def main():
    # Токен вашего бота
    token = '6991834091:AAGSERCH4qFfMR18fa2GAIcCxRH9I31rPUQ'
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
