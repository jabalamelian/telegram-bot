import telebot

TOKEN = "8058278858:AAHLcScvnAdkjovjPyo9xK8q3mN956siAd8"
bot = telebot.TeleBot(TOKEN)

# دیکشنری مقدار ابجد برای هر حرف فارسی
abjad_dict = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ی': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
    'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

# تابع محاسبه ابجد
def calculate_abjad(text):
    total = 0
    for char in text:
        if char in abjad_dict:
            total += abjad_dict[char]
    return total

# پیام خوش‌آمدگویی
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! یک جمله وارد کن تا مقدار ابجد آن را محاسبه کنم.")

# پردازش پیام کاربر
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.replace(" ", "")  # حذف فاصله‌ها
    abjad_value = calculate_abjad(text)
    bot.reply_to(message, f"مقدار ابجد جمله‌ی شما: {abjad_value}")

bot.polling(none_stop=True)
