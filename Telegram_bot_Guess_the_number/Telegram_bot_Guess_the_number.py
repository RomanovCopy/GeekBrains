#Добавьте в Телеграмм-бот игру "Угадай число".
#Бот загадывает число от 1 до 1000.
#Когда игрок угадывает число выводится количество попыток.

import telebot
from random import randint

bot = telebot.TeleBot("TOKEN")
count=0
myNumber=randint(1,1000)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Поиграем в числа.\nЯ загадал целое число от 1 до 1000.\nПопробуй отгадать.")

@bot.message_handler(content_types=['text'])
def number_game(message):
	if message.text.isnumeric():
         number = int(message.text)
         if examination(myNumber,number,message):
             bot.reply_to(message, f"Победа!!! Я действительно загдал: {number}\nЧисло угадано за {count} попыток.")
         else:
             count+=1
    #else:
	   #  bot.reply_to(message, "Это не число")



def examination(myNumber, number, message):
    if myNumber>number:
        bot.reply_to(message, f"Мало... Попытка {count}" )
        return False
    elif myNumber<number:
        bot.reply_to(message, f"Много...  Попытка {count}")
        return False
    else:
        return True




bot.polling()


