def generator(start, stop):
    while True:
        if start > stop:
            raise StopIteration
        yield start
        start += 1


g = generator(0, 100)
for i in g:
    if i % 3 == 0:
        print('vasya')
    else:
        print(i)
