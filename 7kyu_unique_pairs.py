"""
Specifications

Create the function projectPartners with the parameter n representing the number of students in Mrs. Frizzle's class. The function should return the total number of unique pairs she can make with n students.

projectPartners(2)
  --> returns 1
  
projectPartners(4)
  --> returns 6

Remarks

    your solution should not contain any arrays or objects that are used similar to an array. Note that Haskell will use rather large numbers, such as 10^40, so any list-based solution will autmatically fail the test.

    your function will only recieve a single number that is greater than or equal to 2 -- you do not need to worry about input validation.

"""
# This is basically just a combination in which from n samples we want to create 2 unique combination independent from its order
# The formula is n!/(2!*(n-2)!)

import math

# My Solution
def projectPartners(n):
    return math.factorial(n)/(2*math.factorial(n-2))

# Best Practice
def projectPartners1(n):
    return n*(n-1)/2

a = 4
c = projectPartners(a)
print(c)