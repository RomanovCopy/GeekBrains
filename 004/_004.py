#использование кнопок
import telebot
from telebot import types
import requests
import time

bot = telebot.TeleBot("token") 

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_reg = types.KeyboardButton('регистраци€')
btn_alarm = types.KeyboardButton('оповещение')
markup.add(btn_reg, btn_alarm)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, "ѕривет, € бот ѕитоша.", reply_markup=markup)
	

@bot.message_handler(content_types=['text'])
def text_message(message):
	#print(message)
	data = open('log.txt', mode='a', encoding='utf-8')
	text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
	data.write(text)
	data.close()
	if message.text == 'регистраци€':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		id_list = list(el[:-1] for el in id_list)
		if str(message.from_user.id) not in id_list:
			data = open('registred_users.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, '–егистраци€ прошла успешно!')
		else:
			bot.reply_to(message, '¬ы уже зарегистрированы!')
	elif message.text == 'оповещение':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.read().split('\n')
		data.close()
		id_list = id_list[:-1]
		for id in id_list:
			bot.send_message(id, 'совещание через 5 минут')
		
	
bot.polling()
