#You need to write regex that will validate a password to make sure it
# meets the following criteria:
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

from re import search

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

assert bool(search(regex, 'fjd3IR9')) == True, "bool(search(regex, 'fjd3IR9')), True"
assert bool(search(regex, 'DHSJdhjsU')) == False, "bool(search(regex, 'DHSJdhjsU')), False"