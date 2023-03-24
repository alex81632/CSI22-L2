def q2(l):
    result = [0 for i in range(len(l))]
    for i in l:
        sum = 0
        for j in i:
            sum += j
        result[l.index(i)] = sum/2
    return tuple(result)

print(q2(((2,3,4),(3,4,5,6),(2,4),(4,8,9))))