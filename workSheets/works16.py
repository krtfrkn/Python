x=50
y=50

def work1():
    x=100

def work2():
    global y
    y = 200
    return y

work1()
print(x)
work2()
print(y)

