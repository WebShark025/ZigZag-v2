def id(message):
  # Define empty variables
  fu_userid = False
  rt_userid = False
  rf_userid = False
  gp_groupid = False
  # the 'From User' data
  fu_username = message.from_user.username
  fu_userid = message.from_user.id
  fu_fullname = message.from_user.first_name.encode("utf-8")
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
      rf_username = message.reply_to_message.forward_from.username
  if "group" in message.chat.type:
    # the 'Group' data
    gp_groupid = message.chat.id
    gp_fullname = message.chat.title.encode("utf-8")
  
  # Send message
  text = "<code>Your data:</code> \n- <b>Username:</b> @{0}\n- <b>Full name:</b> {1}\n- <b>UserID:</b> {2}".format(fu_username, fu_fullname, fu_userid)
  if rt_userid:
    text = text + "\n\n<code>Replied-to-message data:</code> \n- <b>It's username:</b> @{0}\n- <b>It's fullname:</b> {1}\n- <b>Its userID:</b> {2}".format(rt_username, rt_fullname, rt_userid)
  if rf_userid:
    text = text + "\n\n<code>Replied-to-forwarded-message data:</code> \n- <b>It's username:</b> @{0}\n- <b>It's fullname:</b> {1}\n- <b>Its userID:</b> {2}".format(rf_username, rf_fullname, rf_userid)
  if gp_groupid:
    text = text + "\n\n<code>Group data:</code> \n- <b>Group's title:</b> {1}\n- <b>Group's ID:</b> {0}".format(gp_groupid, gp_fullname)
  bot.send_message(message.chat.id, text, parse_mode="HTML")

class plid:
  patterns=["^[/!]id(.*)$"]
