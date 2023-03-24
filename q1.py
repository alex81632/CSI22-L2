def q1(l):
    for i in l:
        if len(i) == 0:
            l.remove(i)
    return l

print(q1([(1,0), (), (2,3), (4,5,6), (), (1,2,3,4,10)]))