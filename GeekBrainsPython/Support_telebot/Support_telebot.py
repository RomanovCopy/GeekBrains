import telebot
import logging

# создаем бота
bot = telebot.TeleBot('TOKEN')

# настраиваем логирование
logging.basicConfig(filename='support.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Какой у вас вопрос или проблема?')

# обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # записываем обращение пользователя в файл
    logging.info('[{} {}] {}'.format(message.from_user.first_name, message.from_user.last_name, message.text))
    bot.send_message(message.chat.id, 'Ваше обращение принято. Мы постараемся ответить вам как можно скорее.')

# запускаем бота
bot.polling()
