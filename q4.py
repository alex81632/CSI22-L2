def q4(a, b):
    todos = set(a)
    for char in todos:
        if char not in b:
            return False
    return True

print(q4('abcz', 'abracadabra'))
print(q4('abc', 'abracadab'))
