# Write a function, which takes a non-negative integer (seconds)
# as input and returns the time in a human-readable format (HH:MM:SS)

def make_readable(seconds):
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

assert make_readable(60) == "00:01:00", "make_readable(60), '00:01:00'"
assert make_readable(359999) == "99:59:59", "make_readable(359999), '99:59:59'"