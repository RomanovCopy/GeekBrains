#Добавьте в Телеграмм-бот игру "Угадай число".
#Бот загадывает число от 1 до 1000.
#Когда игрок угадывает число выводится количество попыток.

import telebot
from random import randint

# создаем бота
bot = telebot.TeleBot('TOKEN')

# задаем диапазон чисел для угадывания
min_number = 1
max_number = 1000

# генерируем случайное число
number = randint(min_number, max_number)

## задаем количество попыток
#attempts = 0

# обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    global attempts  # объявляем переменную attempts как глобальную
    attempts = 0  # сбрасываем количество попыток при каждом запуске игры
    bot.send_message(message.chat.id, 'Привет! Я загадал число от {} до {}. Попробуй угадать!'.format(min_number, max_number))

# обработчик сообщений с числами
@bot.message_handler(content_types=['text'])
def check_number(message):
    global attempts  # объявляем переменную attempts как глобальную
    try:
        guess = int(message.text)
        if guess < min_number or guess > max_number:
            bot.send_message(message.chat.id, 'Число должно быть от {} до {}.'.format(min_number, max_number))
        elif guess < number:
            attempts += 1  # уменьшаем количество попыток при неверном ответе
            bot.send_message(message.chat.id, 'Загаданное число больше. Израсходовано попыток {}.'.format(attempts))
        elif guess > number:
            attempts += 1  # уменьшаем количество попыток при неверном ответе
            bot.send_message(message.chat.id, 'Загаданное число меньше. Израсходовано попыток {}.'.format(attempts))
        else:
            bot.send_message(message.chat.id, 'Поздравляю, ты угадал! Израсходовано попыток {}..'.format(attempts))
            bot.stop_polling()  # останавливаем бота
    except ValueError:
        bot.send_message(message.chat.id, 'Это не число.')

# запускаем бота
bot.polling()
