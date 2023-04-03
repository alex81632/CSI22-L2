def q5(a, b):
    resp = []
    for i in range(len(a)):
        resp.append([])
        for j in range(len(b[0])):
            resp[i].append(0)
            for k in range(len(b)):
                resp[i][j] += a[i][k] * b[k][j]

    return resp

print(q5([[1,2,3],[4,5,6]], [[1,2],[3,4],[5,6]]))