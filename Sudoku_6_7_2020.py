from turtle import *
speed(0)
pensize(6)
pu()
goto(-324,-322)
pd()
ht()

def square():
    for i in range(4):
        fd(x);lt(90)
x = 648
square()
x = 216
def arrange_square():
    for i in range(4):
        square()
        fd(x)
        square()
        fd(2*x)
        lt(90)

arrange_square()
x = 72
pensize(2)

for i in range(4):
    arrange_square()
    fd(216)
    arrange_square()
    fd(432);lt(90)
fd(432);lt(90);fd(216)
arrange_square()
