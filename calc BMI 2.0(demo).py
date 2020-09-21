def getDict():
    r={}
    while (True):
        print('Enter key (empty enter - exit)')
        k=input()
        if k=='':
            break
        print('Enter value')
        v=input()
        r[k]=v
    return r

d=getDict()
print(d)