
def time(message):
  userid = message.from_user.id
  if len(message.text.split()) < 2:
    m = bot.send_message(message.chat.id, "Please send the city you want to get it's time in your next message.")
    zigzag.nextstep(m, "timecity")
    return
  
  bot.send_chat_action(message.chat.id, "typing")
  time = json.load(urllib.urlopen("https://script.google.com/macros/s/AKfycbyd5AcbAnWi2Yn0xhFRbyzS4qMq1VucMVgVvhul5XqS9HkAyJY/exec?tz={}".format(timezone)))
  bot.send_message(message.chat.id, "Current time in *" + timezone + "*: \n" + time["fulldate"], parse_mode="Markdown")

def timecity(message):
  

def gettime(city):
  try:
    tzd = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(city)))
    if str(tzd["status"]) == "OK":
      latlng = tzd["results"][0]["geometry"]["location"]
      lat = str(latlng["lat"])
      lng = str(latlng["lng"])
      tzl = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/timezone/json?location={}&timestamp=1331161200".format(lat + "," + lng)))
      timezone = tzl["timeZoneId"]
    else:
      bot.reply_to(message, "Timezone not found.")
      return
  except:
    print("[Time] Exception occured")
    return