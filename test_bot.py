import telebot
import random

bot = telebot.TeleBot('1693428494:AAEZbN8QXsVjtS-FR82Ga7FQOEv5oVO5QQc');

file = open('citata.txt')

fraza = [line for line in file]

@bot.message_handler(commands=['citata'])
def start_message(message):
            mssg = random.choice(fraza)
            bot.send_message(message.chat.id, mssg)

bot.polling(none_stop=True, interval=0)