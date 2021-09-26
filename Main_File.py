


from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
aio = Client('Him01','aio_tWXf30872svwYycj3ylJFzNxN5ZW')
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
bot_token = '2010824411:AAHk9YCY3J9k0qXKaN3sPfy_jqipJsbao4s'
u = Updater(bot_token,use_context = True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
