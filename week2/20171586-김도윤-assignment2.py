while (1):

    answer = 1
    inputStr = input()

    try:
        inputNum = float(inputStr)

        if(inputNum == -1):
            break

    except ValueError:

        inputStr = str(inputStr)
        inputNum = -1
        print(inputStr, " is not a number")

    if (inputNum == 0):

        print(answer)

    elif (inputNum < -1 or not inputNum - int(inputNum) == 0):

        print("we can't do it")

    else:

        while (inputNum > 0):
            answer = inputNum * answer
            inputNum = inputNum - 1

        print(int(answer))