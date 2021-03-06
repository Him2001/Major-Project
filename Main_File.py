from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
import os


telegram_bot_token = os.getenv('telegram_bot_token')
adafruit_client = os.getenv('adafruit_client')
adafruit_token = os.getenv('adafruit_token')

aio = Client(adafruit_client,adafruit_token)
bot_token = telegram_bot_token 
 
def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Turning on Light')
def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Turning off Light')
def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Turning on Fan')
def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Turning off Fan')
def main(bot,update):
  a = bot.message.text 
  b = bot.message.text
  c = bot.message.text
  d = bot.message.text
  if a == "Turn on light":
   demo1(bot,update)
   aio.send('light-feed',1)
  if b == "Turn off light":
   demo2(bot,update) 
   aio.send('light-feed',0)
  if c == "Turn on fan":
   demo3(bot,update)
   aio.send('fan-feed',1)
  if d == "Turn off fan":
   demo4(bot,update)
   aio.send('fan-feed',0)


u = Updater(bot_token,use_context = True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
