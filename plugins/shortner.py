def shortner(m):
  userid = m.from_user.id
  m = bot.send_message(m.chat.id, "Please send the link you want to be shortened in your next message")
  zigzag.nextstep(m, "shortsendlink")

def shortsendlink(m):
  text = m.text.replace("/short ","", 1).replace("Link shortner", "", 1)
  res = urllib.urlopen("http://r1z.ir/api.php?long={}".format(text).replace("+","%2B")).read()
  bot.send_message(m.chat.id, "Shorten link: `{}`".format(res), parse_mode="Markdown", disable_web_page_preview=True)

class plshortner:
  patterns = ["^[/!]short(.*)"]
