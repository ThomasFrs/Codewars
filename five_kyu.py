import re

class Codewars:
  def __init__(self):
    print("Welcome to Codewars 5kyu file")
    
  def make_readable(self, seconds):
    """
    seconds: number of seconds to translate into hours, minutes and second
    return: seconds into hours, minutes and seconds in a digital clock format
    """
    second = 0
    minute = 0
    hour = 0
    if seconds <= 359999:
      for i in range(seconds):
          second += 1
          if second >= 60:
            second -= 60
            minute += 1
            if minute >= 60:
              minute -= 60
              hour += 1
      if second < 10:
        second = "0"+str(second)
      if minute < 10:
        minute = "0"+str(minute)
      if hour < 10:
        hour = "0"+str(hour)
      return str("{}:{}:{}".format(hour, minute, second))

  def domain_name(self, url):
    """
    url: url of a website to split from "/" and "."
    return: domain name from the url
    """
    domain_list = ([elt.split(".") for elt in url.split("/")])
    for elt in domain_list:
      name = ([elt[i] for i in range(len(elt)) if elt[i] != "www" and elt[i] != "http:" and elt[i] != "https:" and elt[i] != ""])
      if name != []:
        return name[0]

  def regex_password_validation(self):
    """
    ^              # begin word
    (?=.*[a-z])   # at least one lowercase letter
    (?=.*[A-Z])   # at least one uppercase letter
    (?=.*\d)   # at least one number
    [A-Za-z\d]     # only alphanumeric
    {6,}           # at least 6 characters long
    $              # end word
    """
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"

  def rgb(self, *args):
    """
    args: r, g, b as decimals
    return: r, g, b values converted into hexidecimals
    """
    hex_list = []
    for elt in args:
      if elt < 0:
        elt = "00"
      elif elt > 255:
        elt = "FF"
      elif elt < 10:
        elt = "0" + (hex(elt).split("0x"))[1]
      else:
        elt = (hex(elt).split("0x"))[1]
      hex_list.append(elt.upper())
    return "".join(hex_list)

code = Codewars()