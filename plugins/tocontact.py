tocontactargs = {}

def tocontact(message):
  m = bot.send_message(message.chat.id, "Please enter the number you want to be converted to a contact in your next message.")
  zigzag.nextstep(m, "tocontactsendnum")

def tocontactsendnum(message):
  rlnumber = re.compile(r'^\+(?:\+?)?[0-9]\d{9,13}')
  args = message.text.replace("/tocontact ","").replace(" ","")
  if rlnumber.search(args):
    m = bot.send_message(message.chat.id, "Phone number received: {}\nPlease send the contact name in your next message.".format(args))
    zigzag.nextstep(m, "tocontactsendname")
    tocontactargs.update({str(message.from_user.id) : args})
  else:
    bot.reply_to(message, "Error occured! Phone number is in an invalid format. For example, it should be like this: \n+98 912 1234567. \nPlease start over")
    return

def tocontactsendname(message):
  bot.send_contact(message.chat.id, tocontactargs[str(message.from_user.id)], message.text.replace("/tocontact ",""))
  del tocontactargs[str(message.from_user.id)]

class pltocontact:
  patterns = ["^[/!]tocontact(.*)$"]
