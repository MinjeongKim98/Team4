num = 0
test = 0

while True:
        try:
                fnum = float(input('input number:'))
                if fnum % 1 != 0: continue
                if fnum < 0:
                        if fnum == -1: break
                        else: continue
                hi = 1
                num = int(fnum)
                for i in range(1,num+1):
                        hi *= i
                print(hi)
        except ValueError:
                print('숫자 아냐')
