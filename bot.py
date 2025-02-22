import telebot

TOKEN = "8058278858:AAEoojscH36V8bfyonK0qiKPMaEgVYayTH8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()