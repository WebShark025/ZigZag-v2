def broadcast(message):
  if message.from_user.id not in config["sudo"]:
    return
  allmembers = list(redisserver.smembers('zigzag:members'))
  if message.text.split()[0] == "/bc":
    if len(message.text.split()) < 2:
      bot.reply_to(message, "What should I broadcast?")
      return
    bcmsg = message.text.replace("/bc ","")
    bcusers = 0
    for userid in allmembers:
      try:
        bot.send_message(userid, bcmsg, parse_mode="HTML")
        bcusers = bcusers + 1
        blocklist = redisserver.sismember('zigzag:blocked', '{}'.format(userid))
        if blocklist:
          redisserver.srem('zigzag:blocked', userid)
      except:
        redisserver.sadd('zigzag:blocked',userid)
    bot.reply_to(message, "Successfully broadcasted to " + str(bcusers) + " users!")
    return
  elif message.text == "/fwdall":
    if not message.reply_to_message:
      bot.reply_to(message, "Please reply to a message.")
      return
    messgid = message.message_id
    messgchatid = message.chat.id
    bcusers = 0
    for userid in allmembers:
      try:
        bot.forward_message(userid, from_chat_id=messgchatid, message_id=messgid)
        bcusers = bcusers + 1
        blocklist = redisserver.sismember('zigzag:blocked', userid)
        if blocklist:
          redisserver.srem('zigzag:blocked', userid)
      except:
        redisserver.sadd('zigzag:blocked', userid)
    bot.reply_to(message, "Successfully forwarded to " + str(bcusers) + " users!")

class plbroadcast:
  patterns = ["^[/!]bc (.*)$", "^[/!]fwdall(.*)$"]
