def id(message):
  userlang = redisserver.get("settings:user:language:" + str(message.from_user.id))
  fu_username = message.from_user.username
  fu_userid = message.from_user.id
  fu_fullname = message.from_user.first_name.encode("utf-8")
  reply_msg = language[userlang]["ID_MSG"]
  gpid = message.chat.id
  if message.chat.type == "supergroup" or message.chat.type == "group": 
    reply_msg = reply_msg + language[userlang]["INGP_ID_MSG"]
  if message.reply_to_message:
    repliedid = message.reply_to_message.from_user.id
    reply_msg = reply_msg + language[userlang]["REPLIED_ID_MSG"].format(repliedid)
    if message.reply_to_message.forward_from:
      reply_msg = reply_msg + language[userlang]["FORWARDED_ID_MSG"].format(message.reply_to_message.forward_from.id)
      try:
        reply_msg = reply_msg + language[userlang]["CHATID_ID_MSG"].format(message.reply_to_message.forward_from_chat.id)
      except:
        pass
  bot.reply_to(message, reply_msg.format(username, userid, gpid), parse_mode="Markdown")
  
  
def id(message):
  # the 'From User' data
  fu_username = message.from_user.username
  fu_userid = message.from_user.id
  fu_fullname = message.from_user.firstname.encode("utf-8")
  # check for 'Replied to' message
  if message.reply_to_message:
    # the 'Replied To' data
    rt_userid = message.reply_to_message.from_user.id
    rt_fullname = message.reply_to_message.from_user.first_name.encode("utf-8")
    rt_username = message.reply_to_message.from_user.username
    if message.reply_to_message.forward_from:
      # the 'Replied to, Forwarded' data
      rf_userid = message.reply_to_message.forward_from.id
      rf_fullname = message.reply_to_message.forward_from.first_name.encode("utf-8")
      rf_username = message.reply_to_message.forward_from.from_user.username
  if message.
