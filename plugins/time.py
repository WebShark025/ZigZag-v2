
def time(message):
  userid = message.from_user.id
  if len(message.text.split()) < 2:
    m = bot.send_message(message.chat.id, "Please send the city you want to get it's time in your next message.")
    zigzag.nextstep(m, "timecity")
    return
  city = city = message.text.split()[1]
  gettm = gettime(city)
  bot.send_chat_action(message.chat.id, "typing")
  if gettm == True:
    bot.send_message(message.chat.id, "Current time in *" + gettm["time"][0] + "*: \n" + gettm["time"][1], parse_mode="Markdown")

def timecity(message):
  city = message.text.replace("/time ", "")
  bot.send_chat_action(message.chat.id, "typing")
  gettm = gettime(city)

def gettime(city):
  try:
    tzd = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/geocode/json?address={}".format(city)))
    if str(tzd["status"]) == "OK":
      latlng = tzd["results"][0]["geometry"]["location"]
      lat = str(latlng["lat"])
      lng = str(latlng["lng"])
      tzl = json.load(urllib.urlopen("https://maps.googleapis.com/maps/api/timezone/json?location={}&timestamp=1331161200".format(lat + "," + lng)))
      timezone = tzl["timeZoneId"]
      time = json.load(urllib.urlopen("https://script.google.com/macros/s/AKfycbyd5AcbAnWi2Yn0xhFRbyzS4qMq1VucMVgVvhul5XqS9HkAyJY/exec?tz={}".format(timezone)))
      return {"time" : [timezone, time["fulldate"]]}
    else:
      bot.reply_to(message, "Timezone not found.")
      return False
  except:
    print("[Time] Exception occured")
    return False
