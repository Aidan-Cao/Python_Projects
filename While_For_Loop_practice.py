from turtle import *
speed(0)
pensize(3)
pu()
goto(170,0)
pd()
ht()
color('red')
for i in range(12):
    fd(120);rt(150)

pu()
lt(90);fd(70)
pd()
color('blue')
style = ('Courier', 30, 'italic')
write('For Loop Star', font=style, align='center')


rt(90)
x = 0
pu()
goto(-180,0)
pd()
pensize(5)

while x < 5:
    fd(150);rt(144)
    x = x + 1
pu()
lt(90);fd(70)
pd()
color('red')
style = ('Courier', 30, 'italic')
write('While Loop Star', font=style, align='center')
