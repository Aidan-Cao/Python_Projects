
from tkinter import * # Button, Tk, Entry, StringVar
  
# globally variable 
expression = "" 
  
# combine key inputs into expression then set to String Variable named equation. ref ln61/62
def press(num): 
    # re-define the global variable 
    global expression 
  
    # concatenate strings
    expression = expression + str(num) 
  
    # update equation/expression using set method 
    equation.set(expression) #no upfront String Variable definition needed for equation instance
    
# evaluate final expression 
def equalpress(): 
    # handling errors like zero 
    # division etc. 
    # Put code inside try block 
    # which may generate the error
    
    try: 
        global expression 
  
        # evaluate the expression (real calcultion here)
        # and put in string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze expression variable
        expression = "" #clean the carrying basket:)
  
    # error handle/clear expression 
    # by the except block 
    except: 
        equation.set(" error ") 
        expression = "" 
  
# clear text entry box and equation content 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") #clean Entry Field
  
# Create gedgets 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set GUI background color, .. 
    gui.configure(background="light green") 
    gui.title("Simple Calculator") 
    #gui.geometry("330x150") 
  
    # StringVar() is a variable class 
    # equation is an instance of the class 
    equation = StringVar() 
  
    # create text entry box for showing the expression.
    expression_field = Entry(gui, textvariable = equation) 
  
    # grid method used for placing 
    # the widgets at respective positions 
    expression_field.grid(columnspan=4, ipadx=70) 
  
    equation.set('enter your expression') 
  
    # create Buttons
    button1 = Button(gui, text=' 1 ', fg='black', bg='light blue', 
                     command=lambda: press(1), height=1, width=10) 
    button1.grid(row=2, column=0) sdfassasf
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='light blue', 
                     command=lambda: press(2), height=1, width=10) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='light blue', 
                     command=lambda: press(3), height=1, width=10) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='light blue', 
                     command=lambda: press(4), height=1, width=10) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='light blue', 
                     command=lambda: press(5), height=1, width=10) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='light blue', 
                     command=lambda: press(6), height=1, width=10) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='light blue', 
                     command=lambda: press(7), height=1, width=10) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='light blue', 
                     command=lambda: press(8), height=1, width=10) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='light blue', 
                     command=lambda: press(9), height=1, width=10) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='light blue', 
                     command=lambda: press(0), height=1, width=10) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui, text=' + ', fg='black', bg='light blue', 
                  command=lambda: press("+"), height=1, width=10) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui, text=' - ', fg='black', bg='light blue', 
                   command=lambda: press("-"), height=1, width=10) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui, text=' x ', fg='black', bg='light blue', 
                      command=lambda: press("*"), height=1, width=10) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui, text=' / ', fg='black', bg='light blue', 
                    command=lambda: press("/"), height=1, width=10) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui, text=' = ', fg='black', bg='light blue', 
                   command=equalpress, height=1, width=10) 
    equal.grid(row=5, column=2) 
  
    clear = Button(gui, text='Clear', fg='black', bg='light blue', 
                   command=clear, height=1, width=10) 
    clear.grid(row=5, column='1') 
  
    Decimal= Button(gui, text='.', fg='black', bg='light blue', 
                    command=lambda: press('.'), height=1, width=10) 
    Decimal.grid(row=6, column=0) 
    # start the GUI 
    gui.mainloop()
