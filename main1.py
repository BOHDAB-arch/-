
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8544024388:AAHOmOa_SzJpr2rpeRb4c3bi7MpGpVa-XsI"
APP_URL = "https://t.me/DropStarsrobot?startapp"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "🎮 Привіт!\n\n"
        "🔥 Заходь, грай з нами та веселись!\n"
        "🚀 На тебе чекають ігри та круті емоції!\n\n"
        "👇 Натискай кнопку нижче та починай!"
    )

    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="🎮 Грати в апці",
            url=APP_URL
        )
    )

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=keyboard
    )

print("Бот запущений!")

bot.infinity_polling()
