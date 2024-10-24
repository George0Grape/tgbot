import telebot
import math
from googletrans import Translator
from telebot import types
import random
import requests
bot=telebot.TeleBot('insert token here')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("+")
    btn2 = types.KeyboardButton('-')
    btn3 = types.KeyboardButton("*")
    btn4 = types.KeyboardButton('/')
    btn5=types.KeyboardButton('solve a quadratic equation')
    btn6=types.KeyboardButton('Translate a word or text')
    btn7=types.KeyboardButton('play rock-paper-scissors')
    btn8=types.KeyboardButton('find out the weather of the entered city')
    btn9=types.KeyboardButton('convert a number from decimal number system to another number system')
    markup.add(btn1, btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
    bot.send_message(message.from_user.id, "PLEASE CHOOSE AN OPERATION BEFORE ENTERING NUMBERS", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text in ['+','-','*','/']:
        msg = bot.send_message(message.from_user.id, "Enter 2 numbers separated by space", reply_markup=markup)
        if message.text=='-':
            bot.register_next_step_handler(msg,sub)
        if message.text=='+':
            bot.register_next_step_handler(msg,add)
        if message.text=='*':
            bot.register_next_step_handler(msg,mul)
        if message.text=='/':
            bot.register_next_step_handler(msg,div)
    elif message.text=='solve a quadratic equation':
        msg = bot.send_message(message.from_user.id, "enter coefficients", reply_markup=markup)
        bot.register_next_step_handler(msg,sol)
    elif message.text=='Translate a word or text':
        msg = bot.send_message(message.from_user.id, "enter text and code of language you want to transalte text into ", reply_markup=markup)
        bot.register_next_step_handler(msg,tr)
    elif message.text=='play rock-paper-scissors':
        msg = bot.send_message(message.from_user.id, "Your turn,enter it using lowercase letters", reply_markup=markup)
        bot.register_next_step_handler(msg,tr2)
    elif message.text=='find out the weather of the entered city':
        msg = bot.send_message(message.from_user.id, "enter city", reply_markup=markup)
        bot.register_next_step_handler(msg,weat)
    elif message.text=='convert a number from decimal number system to another number system':
        msg = bot.send_message(message.from_user.id, "enter number and required number system separated by spaces,number must be decimal , required number system must be less than 37", reply_markup=markup)
        bot.register_next_step_handler(msg,conv)
def sub(message):
    a,b=list(map(int,message.text.split()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id,{a-b}, reply_markup=markup)
    bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
def add(message):
    a,b=list(map(int,message.text.split()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id,{a+b}, reply_markup=markup)
    bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
def mul(message):
    a,b=list(map(int,message.text.split()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id,{a*b}, reply_markup=markup)
    bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
def div(message):
    a,b=list(map(int,message.text.split()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if a%b==0:
        n=a//b
    else:
        n=a/b
    bot.send_message(message.from_user.id,{n}, reply_markup=markup)
    bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
def sol(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if len(message.text.split())<3:
        bot.send_message(message.from_user.id,'you need to enter 3 coefficients', reply_markup=markup)
        bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
        return
    a,b,c=list(map(int,message.text.split()))
    if a==0:
        bot.send_message(message.from_user.id,'equation is not quadratic', reply_markup=markup)
        bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
    else:
        d=b**2-4*a*c
        if d==0:
            bot.send_message(message.from_user.id,f'x={-b/(2*a)}', reply_markup=markup)
        elif d>0:
            bot.send_message(message.from_user.id,f'x1={(-b+math.sqrt(d))/(2*a)} x2={(-b-math.sqrt(d))/(2*a)}', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id,'equation has no solutions in real numbers', reply_markup=markup)
    bot.send_message(message.from_user.id,'choose an operation', reply_markup=markup)
def tr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    translator=Translator()
    a=message.text[:-3]
    initial_lang=translator.detect(a).lang
    ans=translator.translate(a,src=initial_lang,dest=message.text[-2:])
    bot.send_message(message.from_user.id,ans.text, reply_markup=markup)
def tr2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    answer=random.choice(['rock','paper','scissors'])
    w={'rock':'scissors','paper':'rock','scissors':'paper'}
    if message.text in ['rock','paper','scissors']:
        if w[answer]==message.text:
            bot.send_message(message.from_user.id,answer, reply_markup=markup)
            bot.send_message(message.from_user.id,'I won', reply_markup=markup)
            bot.send_message(message.from_user.id,'Game over', reply_markup=markup)
        elif w[message.text]==answer:
            bot.send_message(message.from_user.id,answer, reply_markup=markup)
            bot.send_message(message.from_user.id,'You won', reply_markup=markup)
            bot.send_message(message.from_user.id,'Game over', reply_markup=markup)
        else:
            bot.send_message(message.from_user.id,answer, reply_markup=markup)
            bot.send_message(message.from_user.id,'tie', reply_markup=markup)
            bot.send_message(message.from_user.id,'Game over', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id,'You need to enter rock,paper or scissors using only lowercase letters', reply_markup=markup)
        bot.send_message(message.from_user.id,'Game over', reply_markup=markup)
def weat(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    city=message.text
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    bot.send_message(message.from_user.id,f'It is {str(temperature)}°C in {city}  now', reply_markup=markup)
    bot.send_message(message.from_user.id,f'Feels like {str(temperature_feels)} °C', reply_markup=markup)
def conv(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a,b=message.text.split()
    a=int(a)
    b=int(b)
    s=''
    alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while a>0:
        s+=alphabet[a%b]
        a//=b
    s=s[::-1]
    bot.send_message(message.from_user.id,s, reply_markup=markup)
bot.polling(none_stop=True)
