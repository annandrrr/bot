import telebot
bot = telebot.TeleBot('1086164896:AAGgiW-HaBUnnRW__Qf8L-rHMv585yAWb7k')


@bot.message_handler(content_types=['text'])
def start(message):
    bot.send_message(message.chat.id, 'Люблю тебя')


bot.polling(none_stop=True)
