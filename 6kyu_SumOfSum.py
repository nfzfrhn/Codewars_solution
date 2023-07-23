"""
Let's define two functions:

S(N) — sum of all positive numbers not more than N
S(N) = 1 + 2 + 3 + ... + N

Z(N) — sum of all S(i), where 1 <= i <= N
Z(N) = S(1) + S(2) + S(3) + ... + S(N)

You will be given an integer N as input; your task is to return the value of S(Z(N)).

For example, let N = 3:

Z(3) = 1 + 3 + 6 = 10
S(Z(3)) = S(10) = 55

The input range is 1 <= N <= 10^9 and there are 80 ( 40 in LC ) test cases, of which most are random.

This is my first kata and I hope you'll enjoy it :).
Best of luck!

"""

import math as m

# Solution 1: O(n^2) because of the nested for loop plus the O(n) for the last for loop
def sum_of_sums1(n):
    sum1 = 0
    sum2 = 0
    sumsum = 0
    for i in range(1,n+1):
        sum2 = 0
        for j in range(1,i+1):
            sum2 += j
        sum1 += sum2
        #print(i)
    for k in range(1,sum1+1):
        sumsum +=k
    return sumsum

# Solution 2: There are 2 for loops. The solution works fine for small n but fail the test when n = 1x10^9. 
# This is the foundation for the next solution
def sum_of_sums(n):
    sum1 = 0
    sum2 = 0
    sumsum = 0
    for i in range(1,n+1):
        sum1 += i*n
        n -= 1
    print(f"sum1 is {sum1}")
    for k in range(1,sum1+1):
        sumsum +=k
    return sumsum

# Solution 3: There are 1 for loops but still fail the test when n = 1x10^9. The last for loop is O(1)
def sum_of_sums2(n):
    sum1 = 0
    sumsum = 0
    for i in range(1,n+1):
        sum1 += i*n
        n -= 1
    sumsum = sum1*(sum1+1)/2
    return sumsum

# The Solution: O(1)
def sum_of_sums3(n):
    sum = n*(n+1)*(n+2)//6          # This is the sum of the first  n triangular numbers
    sumsum = sum*(sum+1)//2         # This is the sum of the first sum triangular numbers. Which is basically triangular number
    return sumsum


N = 2 
a = sum_of_sums2(N)
b = sum_of_sums(N)
c = sum_of_sums3(N)
print(f"a is {a}")
print(f"b is {b}")
print(f"c is {c}")