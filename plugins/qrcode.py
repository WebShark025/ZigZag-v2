# -*- coding: utf-8 -*-

def qrcode(message):
  userid = message.from_user.id
  m = bot.send_message(message.chat.id, "Please send the link/address/text/etc. you want to be converted to QR-Code")
  zigzag.nextstep(m, "qrnext")

def qrnext(message):
  args = message.text.replace("/qrcode ","").replace(" ", "%20")
  bot.reply_to(message, "Processing... Please wait !")
  urllib.urlretrieve("http://api.qrserver.com/v1/create-qr-code/?data={}&size=600x600".format(args), 'data/qr{}.png'.format(userid))
  bot.send_photo(message.chat.id, open('data/qr{}.png'.format(userid)), caption="QR Code by @TheZigZagBot")

class plqrcode:
  patterns = ["^[/!]qrcode(.*)$"]
