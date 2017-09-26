def factorial(num):
    if num == 0:
        return 1
    elif int(num) < 0:
        print("that is not possible")
    else:
        fac_num = num * factorial(num-1)
        return fac_num


num = int(input())
print(factorial(num))