import os
from flask import Flask, request
import telebot

# التوكن الخاص بالبوت
TOKEN = "8971500769:AAG6phF5pWlKR6o8_IFwu2gZrYTcpQtgz7g"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# الصفحة الرئيسية للتحقق من عمل السيرفر
@app.route('/')
def index():
    return "Ichancy Swaida Bot is running!", 200

# مسار الـ Webhook الأساسي الذي يحل مشكلة 404
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Forbidden", 403

# رد تجريبي عند إرسال /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! تم ربط البوت وتشغيله بنجاح على مدار 24 ساعة.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
