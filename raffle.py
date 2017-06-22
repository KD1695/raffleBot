from telegram.ext import Updater
updater = Updater(token='396866495:AAF0epwzj-a8DrOlayFft5atAizNv7UWdWs')
dispatcher = updater.dispatcher
def start(bot, update):
		bot.send_message(chat_id=update.message.chat_id, text="HI! I will generate tickets for you!")

		
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

from random import randint
ticketlist = []
tickets = []

def ticket(bot, update, args):
	nameP = ' '.join(args)
	b = randint(1, 1000)
	while b in ticketlist:
		b = randint(1, 1000)
	st = "Number: " + str(b) + " for " + nameP
	ticketlist.append(b)
	tickets.append([nameP, b])
	bot.send_message(chat_id=update.message.chat_id, text=st)

	
tick_handler = CommandHandler('ticket', ticket, pass_args=True)
dispatcher.add_handler(tick_handler)