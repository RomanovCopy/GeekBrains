#Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.
import telebot
import logging


# создаем бота
bot = telebot.TeleBot('TOKEN')

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Какой у вас вопрос или проблема?')
