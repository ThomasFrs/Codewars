# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.

def two_to_one(a1, a2):
  """
  a1, a2: string of unsorted letters
  return: sorted string of each letters of a1 and a2
  """
  return "".join(sorted(set(a1 + a2)))

assert two_to_one("aretheyhere", "yestheyarehere") == "aehrsty", "two_to_one('aretheyhere', 'yestheyarehere'), 'aehrsty'"
assert two_to_one("inmanylanguages", "theresapairoffunctions") == "acefghilmnoprstuy", "two_to_one('inmanylanguages', 'theresapairoffunctions'), 'acefghilmnoprstuy'"