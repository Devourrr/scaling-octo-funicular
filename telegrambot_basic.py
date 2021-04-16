import telebot  # pip install pyTelegramBotAPI
import requests
from bs4 import BeautifulSoup  # pip install bs4
from urllib import parse

BOT_TOKEN = 'TOKEN'

bot = telebot.TeleBot(BOT_TOKEN)


def weather(loc):
    weather_text = ''   # 텍스트 내용을 모두 담아 한번에 반환
    return weather_text


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, 'Hi there.')


@bot.message_handler(commands=['날씨'])
def send_weather(message):
    try:
        args = message.text.split()
        query = args[1]
        res = weather(query)
    except Exception as e:
        bot.reply_to(message, e)
    
    bot.reply_to(message, res)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
