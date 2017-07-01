def calculator(m):
  userid = m.from_user.id
  if len(m.text.replace("✒️ Calculate", "", 1).split()) < 2:
    bot.reply_to(m, language[userlang]["CALC_NEA_MSG"], parse_mode="Markdown")
    return
  text = m.text.replace("/calc ","")
  res = urllib.urlopen("http://api.mathjs.org/v1/?expr={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "_{}_ = `{}`".format(text,res), parse_mode="Markdown", disable_web_page_preview=True)
