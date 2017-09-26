def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif int(num) < 0:
        print("that is not possible")
    else:
        return num * factorial(num - 1)

def combination(n,m):
    if n > m:
        x = n-m
        n = factorial(n)
        m = factorial(m)
        x = factorial(x)
        result = n/(x*m)
        return result
    elif n == m:
        return 1
    else:
        print("cannot be calculated")

n = int(input())
m = int(input())
print(combination(n,m))

#print(combination(n, m))