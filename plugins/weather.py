def weather(message):
  userid = message.from_user.id
  if len(message.text.replace("/weather", "").split()) < 2:
    m = bot.send_message(message.chat.id, "Please enter the city you want to get weather of, in your next message.")
    zigzag.nextstep(m, "weathercity")
    return
  city = message.text.replace("/weather ","").replace(" ", "%20")
  try:
    url = json.load(urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2def4a0a0455314526b0f455f98ec0f&units=metric".format(city)))
  except Exception as e:
    zigzag.error("Exception occured: " + str(e))
    return
  bot.send_message(message.chat.id, "💢 Current status of *" + str(url["name"]) + "*: \n\n🌍 Country: `" + str(url["sys"]["country"]) + "` \n☀️ Temperature: `" + str(url["main"]["temp"]) + "°C` \n" + "🌤 Weather: `" + str(url["weather"][0]["main"]) + "` \n💨 Wind: `" + str(url["wind"]["speed"]) + "m/s` \n💧 Humidity: `" + str(url["main"]["humidity"]) + "%`", parse_mode="Markdown")

def weathercity(message):
  userid = message.from_user.id
  city = message.text.replace("/weather ","").replace(" ", "%20")
  try:
    url = json.load(urllib.urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=d2def4a0a0455314526b0f455f98ec0f&units=metric".format(city)))
  except Exception as e:
    zigzag.error("Exception occured: " + str(e))

class plweather:
  patterns = ["^[/!]weather(.*)$"]
