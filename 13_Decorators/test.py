def testing(x, *args,**kwargs):
    print(x)
    print(*args)
    print(f'{kwargs}')
    pass

testing(1, 2, 3, A=4,B=5,C=6)