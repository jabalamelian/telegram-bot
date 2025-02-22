import telebot

TOKEN ="8058278858:AAHLcScvnAdkjovjPyo9xK8q3mN956siAd8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من ربات تلگرامی شما هستم.")

bot.polling(none_stop=True)  # این خط فقط وقتی باید اجرا بشه که Webhook فعال نباشه
