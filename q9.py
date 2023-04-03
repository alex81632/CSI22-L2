def q9(mat):
    resp = []
    for lin in mat:
        obj = list(map(lambda x: x+2, lin))
        resp.append(obj)
    return resp

print(q9([[1,2,3],[4,5,6],[7,8,9]]))