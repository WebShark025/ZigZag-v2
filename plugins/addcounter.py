def addcounter(message):
  userid = message.from_user.id
  m = bot.send_message(message.chat.id, "Please send your message so it will get add-countererd")
  zigzag.nextstep(m, adcstep2)


class plecho:
  patterns = ["^[!/]addcounter(.*)$"]
  # At the 'inlines' variable, you can use DEFAULTQUERY to get when there is no queries entered
