from tkinter import *

import random


array = ["It is certain.","Without a doubt" "It is decidedly so","Yes - definitely","You may rely on it",\
         "As I see it, yes","Most likely yes","Yes","Signs point to yes","Reply hazy, try again","Ask again later",\
         "Better not tell you now","Cannot predict now","Concentrate and ask again","Do not count on it",\
         "My reply is no","My sources say no","Outlook not so good","Very doubtful","No","I am not your mom"]

window=Tk()
window.grid()
window.geometry('200x50')
btn=Button()
btn2=Button()    
def update():
    for i in range (20):
        choice = int (20 * random.random())
    btn2['text']="Answer: "+ str(array[choice])
    btn2.grid()
        
def widge():
    btn['text'] = "click me to get answer"
    btn['command'] = update
    #btn.pack(side=LEFT, expand=YES, fill=BOTH)
    btn.grid()
    btn2['text']="see answer here"
    btn2['command']=None
    btn2.grid()
    
widge()
window.mainloop()
    
