def iterfibo(num, result):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num < 0:
        return "cannot be calculated"
    else:
        result.append(0)
        result.append(1)
        for i in range(num-1):
            last = result[0] + result[1]
            result.append(last)
            result.pop(0)
        return result[1]

result = []
num = int(input())
print(iterfibo(num, result))
