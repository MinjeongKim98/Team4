num = int(input())
knum = int(input())

def factRF(n):
    return 1 if n == 1 else n * factRF(n - 1)

def factWF(n):
    i = 0
    fact = 1
    while (i < n):
        fact = fact * (i+1)
        i = i + 1
    return fact

print(factRF(num))
print(factWF(num))

def CombiRF(n, k):
    if k == 0 or n == k:
        return 1
    elif n < k:
        print("불가능합니다.")
    else:
        return int(CombiRF(n-1, k-1)+CombiRF(n-1, k))

def CombiWF(n, k):
    return int(factWF(n)/(factWF(k) * factWF(n-k)))

print(CombiWF(num, knum))
print(CombiRF(num, knum))