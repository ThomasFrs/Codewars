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

code = Codewars()