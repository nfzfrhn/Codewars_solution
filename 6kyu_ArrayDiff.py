"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

"""

# My Solution
def array_diff(z,y):
    sol = []
    for i in z:
        if i not in y:
            sol.append(i)
    return sol

# Refactor
def array_diff(z,y):
    return [i for i in z if i not in y]

# Best Practice
def array_diff1(a, b):
    return [x for x in a if x not in b]

a = [1,2,2,2,3]
b = [2]
c = array_diff(a,b)
d = array_diff1(a,b)
print(c)