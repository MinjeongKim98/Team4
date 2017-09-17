num = 0

def fact(n):
    return_value = 1
    if n == 0: return 1
    while n > 0:
        return_value = return_value * n
        n = n - 1
    return return_value

while (num != -1) :
    try:
        num = int(input("Enter a number: "))
        if (num == -1) : break
        print(fact(num))
    except ValueError:
        print("0또는 1이상의 자연수를 입력해주세요")