
countS=0
count1=0
count0=0
countm=0

def func1(m):
    if m == 1 or m == 0:
        return 1
    if m < 0:
        return 0
    return m*func1(m-1)

def func2(m,n):
    if m == n:
        return 1
    if m < n:
        return 0 #입력 잘못 주면 0 리턴하게 
    if n == 1:
        return m
    if n == 0:
        return 1
    return func2(m-1,n)+func2(m-1,n-1)

def func3(m,n):
    return int(func1(m)/(func1(n)*func1(m-n)))
