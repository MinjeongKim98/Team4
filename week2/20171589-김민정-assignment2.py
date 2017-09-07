def factorial(num):
    if num == 0: #number is 0 -> result=1
        return 1
    elif num < 0: #less than 0, it is not possible
        print('it is not possible')
    else:  #make a result
        su=1
        for i in range(1, num+1):
            su *= i
            i += 1
        return su

num = int(input())  #factorial 구할 값 입력받기 #int로 받으면 수 임의 변환-?>float
while num != -1: #-1이 아니면 계속 돌아가도록함
    result = factorial(num) #fuction
    print(result)
    num = int(input())
else:
    break

#while true -> input 한번만 받고 할 수 있음.











    
