#регистраци€ пользовател€
import telebot
import requests
import time

bot = telebot.TeleBot("6119292896:AAEZvqy8hW6fx42SKaWBr5_9qyI7NopYdaE") 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

@bot.message_handler(content_types=['text'])
def text_message(message):
	#print(message)
	if message.text == 'регистраци€':
		data = open('registred_users.txt', mode='r', encoding='utf-8')
		id_list = data.readlines()
		data.close()
		print(id_list)
		id_list = list(el[:-1] for el in id_list)
		print(id_list)
		if str(message.from_user.id) not in id_list:
			data = open('registred_users.txt', mode='a', encoding='utf-8')
			data.write(f'{message.from_user.id}\n')
			data.close()
			bot.reply_to(message, '–егистраци€ прошла успешно!')
		else:
			bot.reply_to(message, '¬ы уже зарегистрированы!')
	

bot.polling()
