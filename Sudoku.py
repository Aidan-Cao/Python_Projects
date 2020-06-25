from turtle import *
speed(0)
pensize(6)
pu()
goto(-324,-322)
pd()
ht()
for i in range(4):
    fd (648)
    lt(90)

def med_square():
    for i in range(4):
        fd(216)
        lt(90)

def arrange_square():
    for i in range(4):
        med_square()
        fd(216)
        med_square()
        fd(432)
        lt(90)
arrange_square()

def small_square():
    pensize(2)
    for i in range(4):
        fd(72)
        lt(90)

def arrange_small_square():
    for i in range(4):
        small_square()
        fd(72)
        small_square()
        fd(144)
        lt(90)

for i in range(4):
    arrange_small_square()
    fd(216)
    arrange_small_square()
    fd(432)
    lt(90)
fd(432)
lt(90)
fd(216)
arrange_small_square()
