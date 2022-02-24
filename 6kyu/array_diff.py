# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b
# keeping their order.

def array_diff(a, b):
    """
    a: array of integers
    b: array of integers to substract to a
    return: the substract of a elements that are present in b
    """
    return ([elt for elt in a if elt not in b])

assert array_diff([1,2,3], [1, 2, 3]) == [], "array_diff([1,2,3], [1, 2, 3]), []"
assert array_diff([1,2,3], [1, 2]) == [3], "array_diff([1,2,3], [1, 2]), [3]"