import telebot

API_TOKEN = '5366935243:AAF-kbdlkr-8bl08eazYFlWTh-SDjCwdXe8'

bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Speech Converter.
I'm here to convert your speech into text. Just record an audio for me!\
""")

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open('new_file.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)

bot.infinity_polling()


