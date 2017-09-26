def combination(n, m):
    if n>m:
        if m == 0:
            return 1
        else:
            return combination(n-1, m) + combination(n-1, m-1)
    elif n == m :
        return 1
    else:
        return "not possible"


n = int(input())
m = int(input())
print(combination(n, m))