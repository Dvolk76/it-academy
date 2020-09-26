def generator(start=0):
    x = start
    while True:
        yield x
        x += 1


for x in generator(1):
    if x % 3 == 0:
        print('vasya')
    else:
        print(x)
