import telebot

API_TOKEN = '5180015716:AAHEXPed8DWwCRabaLpbdJRqXCKepPYrxhI'

bot = telebot.TeleBot(API_TOKEN)


# TODO add voice
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Hi""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()