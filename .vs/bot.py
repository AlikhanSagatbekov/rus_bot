from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработчик команды /start
def start(update, context):
    update.message.reply_text(
        'Привет! Я бот.',
        reply_markup=ReplyKeyboardMarkup([['Достопримечательности'], ['Топ 10 достопримечательностей'], ['Советы по безопасности и путешествиям']]))
        
# Обработчик нажатий на кнопки меню
def menu_button(update, context):
    text = update.message.text
    if text == 'Достопримечательности':
        update.message.reply_text('Здесь будут перечислены достопримечательности.')
    elif text == 'Топ 10 достопримечательностей':
        update.message.reply_text('Здесь будет список топ 10 достопримечательностей.')
    elif text == 'Советы по безопасности и путешествиям':
        update.message.reply_text('Здесь будут советы по безопасности и путешествиям.')

def main():
    # Токен вашего бота
    token = '6991834091:AAGSERCH4qFfMR18fa2GAIcCxRH9I31rPUQ'
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))
    
    # Добавляем обработчик сообщений с кнопками меню
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, menu_button))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
