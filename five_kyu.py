from xml import dom


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

code = Codewars()