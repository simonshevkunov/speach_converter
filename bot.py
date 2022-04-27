import telebot
import requests
import json

IAM_TOKEN = 't1.9euelZqLkpzHjs6Xy5OVmZuNy8vMjO3rnpWaz5jLl5COjcfOkZOSlZePj8jl8_d6D1ps-e96c3d7_t3z9zo-V2z573pzd3v-.JHMNrWcrzwXRI1OiaillN28x2F_JZyBmWvB9isyCePVmUy80MkYq19E6FTsuEyFy2yP21m7kn3JEwwqtTuyJDQ'
FOLDER_ID = 'b1gf0pjdr98nkrslcnba'



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

    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}"
    }
    with open('new_file.ogg', 'rb') as f:
        resp = requests.post(
            f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?folderId={FOLDER_ID}&lang=ru-RU",
            data=f.read(),
            headers=headers)
        res = json.loads(resp.content)

    print(res)
    bot.reply_to(message, res['result'])

bot.infinity_polling()