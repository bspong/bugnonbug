def readFile2():
    for x in range(5):
        yield x


for i in readFile2():
    print (i)