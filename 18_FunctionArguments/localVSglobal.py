# local vs global variables
# state global otherwise will be local

def foo():
    global number
    x = number
    number = 3
    print('number inside function:', x)


number = 0
foo()