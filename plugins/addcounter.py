def addcounter(message):
  userid = message.from_user.id
  m = bot.send_message(message.chat.id, "Please send your message so it will get add-countererd")
  zigzag.nextstep(m, adcstep2)


class pladdcounter:
  patterns = ["^[!/]addcounter(.*)$"]
  # At the 'inlines' variable, you can use DEFAULTQUERY to get when there is no queries entered

def adcstep2(message):
  messgid = message.message_id
  messgchatid = message.chat.id
  fw = bot.forward_message("@ZigZagPrivZZZZZ", from_chat_id=messgchatid, message_id=messgid)
  bot.forward_message(message.chat.id, from_chat_id=fw.chat.id, message_id=fw.message_id)
