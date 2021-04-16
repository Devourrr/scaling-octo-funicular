# pip install pyTelegramBotAPI

import telebot
TOKEN = '1795391045:AAFsmAKo_ResztkMR96grDLq-Ftyf1luPmY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help']) #/start 또는 /help라는 채팅이 오면 실행
def send_welcome(message):
    print(message)
    bot.reply_to(message, 'Hi there.') # 봇이 응답하는 텍스트

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.txt)
    
bot.polling # 주인님의 명령을 기다림
