def q8(lis):
    lis = filter(lambda x: x % 2 == 0, lis)
    return list(lis)

print(q8([1,2,3,4,5,6,7,8,9,10]))