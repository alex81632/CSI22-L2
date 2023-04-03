from math import sqrt
def q7():
    i = 0
    while True:
        i+=1
        # se i for primo, yield i
        if i == 2:
            yield i
        elif i > 2:
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    break
            else:
                yield i
        
ret = q7()
for i in range(10):
    print(ret.__next__())