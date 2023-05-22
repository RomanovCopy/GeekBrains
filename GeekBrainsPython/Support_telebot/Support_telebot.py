import datetime
import telebot

# создаем бота
bot = telebot.TeleBot('TOKEN')
#нумерация обращений
index = 0
# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Какой у вас вопрос или проблема?')
    #обнуляем нумерацию при старте бота
    global index
    index=0
# обработчик всех сообщений
@bot.message_handler(content_types=['text'])
def handle_message(message):
    global index
    # Получение текущей даты и времени
    now = datetime.datetime.now()
    # Форматирование даты и времени в нужный формат
    formatted_date = now.strftime('%d/%m/%Y/%H/%M/%S')
    # записываем обращение пользователя в файл
    index+=1
    text=f"{index}\n{message.chat.username}\n{formatted_date}\n{message.chat.id}\n{message.text}\n"
    file=open('support.log','a', encoding='utf-8')
    file.writelines(text)
    file.close()
    bot.send_message(message.chat.id, 'Ваше обращение принято. Мы постараемся ответить вам как можно скорее.')

# запускаем бота
bot.polling()
