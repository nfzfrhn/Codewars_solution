import math as m

# Inefficient
def isPP1(n):
    ans = []
    for i in range(2,n):
        for j in range(2,n):
            if i**j==n and ((i or j) not in ans):
                ans.extend([i,j])
    if not ans:
        ans = None
    return ans

# Answer1
def isPP2(n):
    ans = []
    count = 0
    m=n
    for i in range(2,n):
        m=n
        count = 0
        if (m%i==0):
            while(m>1):        
                m/=i
                count+=1
        if count!=0 and i**count==n:
            ans.extend([i,count])
        if i**i==n:
                ans.extend([i,i])                  
    if not ans:
        ans = None
    return ans

# Answer 2
def isPP3(n):
    ans = []
    count=0
    m=n
    i=2
    while(m>1):
        if n%i==0:
            m/=i
            count+=1
        else:
            i+=1
        if i**count==n:
            ans.append([i,count])
    if not ans:
        ans = None
    return ans

# My Solution
def isPP(n):
    ans = []
    for i in range(2,n):
        if n%i==0:
            a = m.log(n,i)
            if m.isclose(a,round(a),rel_tol=1e-9,abs_tol=1e-16):
                ans.extend([i,round(a)])
                break
    if not ans:
        ans = None
    return ans

# The Solution
def isPP(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i**j > n:
                break
            elif i**j == n:
                return [i, j]
    return None

k = isPP(19487171) 
print(k)