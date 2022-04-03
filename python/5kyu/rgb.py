# The rgb function is incomplete.
# Complete it so that passing in RGB decimal values will result in a
# hexadecimal representation being returned.
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that
# range must be rounded to the closest valid value.

def rgb(*args):
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

assert rgb(255,255,255) == "FFFFFF", "rgb(255,255,255) == 'FFFFFF'"
assert rgb(-20,275,125) == "00FF7D", "rgb(-20,275,125) == '00FF7D'"