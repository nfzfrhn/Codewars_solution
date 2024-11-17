"""
Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
Example(Input => Output):

35231 => [1,3,2,5,3]
0 => [0]

"""

# The Solution
def digitize(n):
    # map function will return a map object, so we need to convert returned value to list as the question required
    return list(map(int, str(n)[::-1]))

# My Solution
def digitize(n):
    b = [int(i) for i in str(n)]
    b.reverse()
    return b

ans = digitize(35231)
print(ans)