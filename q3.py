def q3(l):
    for i in l:
        # se tiver algum caractere que não seja um alfanumérico remova
        if not i.isalnum():
            l.remove(i)
    return l

print(q3(['ajfu3928jdnu2@448#', 'ksjjcndji', '@&#&@#', 'tunvnms', '1299382hghdn', 'ghdjsjsksk@#', '0']))