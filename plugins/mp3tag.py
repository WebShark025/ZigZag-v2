from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error


mp3taginfo = {}
mp3coverinfo = {}

def mp3tag(message):
  userid = message.from_user.id
  if message.text == "/mp3tag":
    m = bot.send_message(message.chat.id, "Please send the title to be set on the audiofile")
    zigzag.nextstep(m, mp3tagsendtitle)
  elif message.text == "/mp3cover":
    m = bot.send_message(message.chat.id, "Please send the cover you want to be set on your audio.")
    zigzag.nextstep(m, mp3cvrsendcover)

def mp3cvrsendcover(message):
  userid = message.from_user.id
  if not message.photo:
    bot.send_message(userid, "Send a PHOTO, or say /cancel to cancel.")
    zigzag.nextstep(m, mp3cvrsendcover)
    return
  phtoid = message.photo[0].file_id
  photoinf = bot.get_file(phtoid)
  photodl = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(config['token'], photoinf.file_path), '{0}.png'.format(phtoid))
  mp3coverinfo.update({userid: phtoid})
  m = bot.send_message(message.chat.id, "Please send the audio file now.")
  zigzag.nextstep(m, mp3cvrsendaudio)

def mp3cvrsendaudio(message):
  userid = message.from_user.id
  if not message.audio:
    bot.send_message(userid, "Please send an AUDIO, or enter /cancel to abort")
    return
  else:
    photoid = mp3coverinfo[userid]
    fileid = message.audio.file_id
    file_info = bot.get_file(fileid)
    filename = file_info.file_path.replace("music/", "")
    file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(config['token'], file_info.file_path), 'data/mp3tag/{}'.format(filename))
    audio = MP3("data/mp3tag/{}".format(filename), ID3=ID3)
    # add ID3 tag if it doesn't exist
    try:
      audio.add_tags()
    except error as e:
#      print(e)
      pass
    audio.tags.add(
      APIC(
        encoding=3, # 3 is for utf-8
        mime='image/png', # image/jpeg or image/png
        type=3, # 3 is for the cover image
        desc=u'Cover',
        data=open('{0}.png'.format(photoid)).read()
      )
    )
    audio.save()
    bot.send_audio(message.chat.id, open('data/mp3tag/{}'.format(filename), 'rb'), duration=message.audio.duration, title=message.audio.title, performer=message.audio.performer)
    del mp3coverinfo[userid]
    os.remove(photoid + ".png")

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
  userid = message.from_user.id
  if not message.audio:
    m = bot.send_message(message.chat.id, "Please send an AUDIO file, nothing else. To stop: /cancel")
    zigzag.nextstep(m, mp3tagsendaudio)
    return
  fileid = message.audio.file_id
  file_info = bot.get_file(fileid)
  filename = file_info.file_path.replace("music/", "")
  file = urllib.urlretrieve('https://api.telegram.org/file/bot{0}/{1}'.format(config['token'], file_info.file_path), 'data/mp3tag/{}'.format(filename))
  bot.send_audio(message.chat.id, open('data/mp3tag/{}'.format(filename), 'rb'), duration=message.audio.duration, performer=" " + mp3taginfo[userid]["artist"], title=mp3taginfo[userid]["title"])
  del mp3taginfo[userid]
  os.remove("data/mp3tag/" + filename)


class plmp3tag:
  patterns = ["^[/!]mp3tag(.*)$", "^[/!]mp3cover(.*)$"]
