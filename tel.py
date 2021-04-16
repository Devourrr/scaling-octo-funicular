import telebot
TOKEN = '1795391045:AAFsmAKo_ResztkMR96grDLq-Ftyf1luPmY'
# https://pypi.org/project/pyTelegramBotAPI/0.3.0/ 참고
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help']) #/start 또는 /help라는 채팅이 오면 실행
def send_welcome(message):
    print(message)
    bot.reply_to(message, 'Hi there.') # 봇이 응답하는 텍스트

@bot.message_handler(commands=['구구단']) #/구구단 2, /구구단 3
def send_gugudan(message):
    print(message.text)
    
    args = message.text.split(' ')
    dan = args[1]

    res = ''
    for i in range(1, 10):
        # print(f"{dan} x {i} = {dan * i}")
        res += f"{dan} x {i} = {int(dan) * i}\n"
    
    bot.reply_to(message, res)

@bot.message_handler(commands=['오늘의메뉴'])
def send_menu(message):
    print(message.text)
    import random

    args = message.text.split(' ')
    menu = ['김치찌개 ','백반', '삼계탕','돈까스']
    
    
   
    for i in range(len(menu)):
        i = random.randint(0,len(menu) -1)
    
    bot.reply_to(message,'추천 메뉴:' +  menu[i]) # 형식


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    

bot.polling() # 주인님의 명령을 기다림