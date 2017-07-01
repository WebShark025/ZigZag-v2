mp3taginfo = {}

def mp3tag(message):
  userid = message.from_user.id
  if message.text == "/mp3tag":
    m = bot.send_message(message.chat.id, "Please send the title to be set on the audiofile")
    zigzag.nextstep(m, mp3tagsendtitle)

def mp3tagsendtitle(message):
  userid = message.from_user.id
  title = message.text
  m = bot.send_message(message.chat.id, "Title set: {}. Please send the ArtistName to be set.".format(title))
  mp3taginfo.update({userid : title})
  zigzag.nextstep(m, mp3tagsendartist)

def mp3tagsendartist(message):
  userid = message.from_user.id
  artist = message.text
  m = bot.send_message(message.chat.id, "Artist set: {}. Please send the audio file now.".format(artist))
  mp3taginfo[userid] = {"title" : mp3taginfo[userid], "artist" : artist}
  zigzag.nextstep(m, mp3tagsendaudio)

def mp3tagsendaudio(message):
  if not message.audio:
    m = bot.send_message(message.chat.id, "Please send an AUDIO file, nothing else. To stop: /cancel")
    zigzag.nextstep(m, mp3tagsendaudio)
    return
  fileid = message.audio.file_id
  fileinfo = bot.get_file(fileid)
  filename = fileinfo.filepath.replace("music/", "")
  file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(config['token'], file_info.file_path), 'data/mp3tag/{}'.format(filename))
  bot.send_audio(message.chat.id, open('data/mp3tag/{}'.format(filename), 'rb'), duration=message.audio.duration, performer=mp3taginfo[userid][artist], title=mp3taginfo[userid][title])
  del mp3taginfo[userid]
  os.remove(filename)
