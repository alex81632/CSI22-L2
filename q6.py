def q6(lis):
    for i in range(len(lis)-1, -1, -1):
        yield lis[i]

ret = q6([1,2,3,4,5])
print(ret.__next__())