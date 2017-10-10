n = int(input("숫자를 입력하시오 : "))

num_list = [0, 1]

for i in range(1, n-1):
    num_list.append(num_list[i - 1] + num_list[i])

print(num_list)
