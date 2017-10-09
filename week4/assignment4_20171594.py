N = int(input("n :  "))
R = int(input("r :  "))
facto = int(input("num : "))

def fact_recursive(n):
    if n == 1:
            return 1
    elif n > 1:
        return n * fact_recursive(n-1)

num = 0
def fact(n):
    return_value = 1
    if n == 0: return 1
    while n > 0:
        return_value = return_value * n
        n = n - 1
    return return_value

def combi(n, r):
    if n == r or r == 0:
        return 1
    elif r > n:
        print("존재하지 않는 값입니다.")
    else:
        return (combi(n-1, r-1) + combi(n-1 ,r))


def combi_fact(n, r):
    return fact(n)/(fact(r) * fact(n - r))


print("재귀 함수를 이용한 팩토리얼 값 : " , fact_recursive(facto))
print("일반 함수를 이용한 팩토리얼 값 : " , fact(facto))
print("팩토리얼을 이용한 컴비네이션 값 : " , combi_fact(N, R))
print("재귀 함수를 이용한 컴비네이션 값 : " , combi(N, R))
