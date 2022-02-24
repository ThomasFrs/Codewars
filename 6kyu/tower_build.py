# Build a pyramid-shaped tower given a positive integer number of floors.
# A tower block is represented with "*" character.

def tower_build(n_floors=1):
    """
    n_floors: number of floors for the tower
    return: tower consisting of "*" from top to bottom layed out as a pyramid
    """
    tower_list = ([" "*(n_floors-i) + "*"*(2*i-1) + " "*(n_floors-i) for i in range(1, n_floors+1)])
    return tower_list

assert tower_build(2) == [' * ', '***'], "tower_build(2), [' * ', '***']"
assert tower_build(3) == ['  *  ', ' *** ', '*****'], "tower_build(3), ['  *  ', ' *** ', '*****']"