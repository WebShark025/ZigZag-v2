def lmgtfy(message):
  m = bot.send_message(message.chat.id, "Please send the query you want to be LMGTFY'ed")
  zigzag.nextstep(m, "lmgtfyquery")

def lmgtfyquery(message):
  textl = message.text.replace("/lmgtfy ","", 1).replace("/Lmgtfy ", "", 1).replace("+","%2B")
  rez = urllib.urlopen("http://r1z.ir/api.php?long=http://lmgtfy.com/?q={}".format(textl)).read()
  bot.send_message(message.chat.id, "Direct link: `{}`\n\nOr [Click on this]({})".format(rez,rez), parse_mode="Markdown", disable_web_page_preview=True)

def inlinelmgtfy(query):
  if query.query == "lmgtfy":
    r = types.InlineQueryResultArticle('1', "Please enter a query to lmgtfy it!", types.InputTextMessageContent('http://google.com'))
    bot.answer_inline_query(inline_query.id, [r])
    return
  text = query.query.replace("lmgtfy ", "")
  lmgtfyurl = urllib.urlopen("http://r1z.ir/api.php?long=http://lmgtfy.com/?q={}".format(text.replace(" ", "+"))).read()
  try:
    r3 = types.InlineQueryResultArticle('3', "Send inline lmgtfy message!, types.InputTextMessageContent("Direct link: `{}`\n\nOr click on [this :D]({})".format(lmgtfyurl, lmgtfyurl), parse_mode="Markdown", disable_web_page_preview=True))
    bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)
  except:
    r3 = types.InlineQueryResultArticle('3', 'Error occured.', types.InputTextMessageContent("Unexpected error occured."))
    bot.answer_inline_query(inline_query.id, [r3], cache_time=1, is_personal=True)

class pllmgtfy:
  patterns = ["^[/!]lmgtfy(.*)$"]
  inlines = ["lmgtfy(.*)"]
