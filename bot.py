import telebot
from config import BOT_TOKEN
from database import create_tables, update_order_status
from utils import send_notification

bot = telebot.TeleBot(BOT_TOKEN)

# إضافة أوامر البوت
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أهلاً بك في ShahenX! اختر خدمة من القائمة.")

@bot.message_handler(commands=['track_order'])
def track_order(message):
    # من هنا يمكنك إضافة الكود لتتبع الأوردرات
    pass

# استلام إشعارات من المندوب عند تغيير حالة الأوردر
@bot.message_handler(func=lambda message: True)
def order_notification(message):
    # هنا تستخدم دالة إرسال الإشعار للمستخدم
    send_notification(message.text)

if __name__ == "__main__":
    create_tables()  # إنشاء الجداول في قاعدة البيانات
    bot.polling()
