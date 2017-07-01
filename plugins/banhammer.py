def banhammer(message):
  if message.from_user.id not in sudo:
    return
  if len(message.text.split()) < 2:
    bot.reply_to(message, "Who should I ban?")
    return
  userid = message.text.split()[1].replace(" ", "")
  if message.text.split()[0] == "/ban":
    zigzag.ban(userid)
  elif message.text.split()[0] == "/unban":
    zigzag.unban(userid)

class plbanhammer:
  patterns = ["^[!/]unban (.*)$", "^[!/]ban (.*)$"]
