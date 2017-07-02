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
    gp_fullname = message.chat.title
  
  # Send message
  text = "`Your data:` \n- *Username:* @{0}\n- *Full name:* {1}\n- *UserID:* {2}".format(fu_username, fu_fullname, fu_userid)
  if rt_userid:
    text = text + "\n\n`Replied-to-message data:` \n- *It's username:* @{0}\n- *It's fullname:* {1}\n- *Its userID:* {2}".format(rt_username, rt_fullname, rt_userid)
  if rf_userid:
    text = text + "\n\n`Replied-to-forwarded-message data:` \n- *It's username:* @{0}\n- *It's fullname:* {1}\n- *Its userID:* {2}".format(rf_username, rf_fullname, rf_userid)
  if gp_groupid:
    text = text + "\n\n`Group data:` \n- *Group's title:* {0}\n- *Group's ID:* {1}".format(gp_groupid, gp_fullname)
  bot.send_message(message.chat.id, text, parse_mode="Markdown")

class plid:
  patterns=["^[/!]id(.*)$"]
