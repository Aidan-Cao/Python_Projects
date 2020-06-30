
import tkinter as tk
import random
#import winsound #importing this gives the ability to play .wav sounds


class Magic8Ball(tk.Frame):

# The parameter tk.Frame is a Frame widget from the tkinter module.
    def __init__(self, master=None):

        tk.Frame.__init__(self,master)
        self.grid()
        self.master.title('Magic 8 Ball') # titles main window
        self.master.configure(bg = 'white') # makes background white
        self.master.geometry("330x490")   # sizes window
        self.master.resizable(0,0)        # makes window NOT resizable
        self.createHeading()
        self.createQuestion()
        self.createShakebutton()
        self.eightballpic()

    def createHeading(self):
        
        self.heading = tk.Label(self, text = "Ask Magic8Ball a Question.", font=('Times New Roman', 15))
        self.heading.config(bg = 'white', fg = 'blue')
        self.heading.grid(row = 1, column = 0, columnspan = 3, pady = 5, padx = 10)
        self.heading.focus_force()
           
            
    def createQuestion(self):

        self.question = tk.Entry(self, width = 35)
        self.question.grid(row = 2, column = 0, columnspan = 2, pady = 5, padx = 0)
        self.question.focus_force()  
        return self.question
        
        
    def createShakebutton(self):

        self.shake = tk.Button(self, text = "Click me to Shake the Magic 8 Ball!",font=('Times New Roman', 15))
        self.shake.configure(bg='black',fg='blue')
        self.shake.grid(row = 3,column = 0, pady = 5, padx = 5)
        self.shake["command"] = self.validate
        #'command' means wait for the user to click on the button
        self.master.bind("<Return>", self.validate2)
        #<Return> is the 'Enter' key
        
        
           
    def eightballpic(self):

        self.picture = tk.Label(self)
        self.picture.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 5)
        self.ball = tk.PhotoImage(file = "magic8ball.gif")
        self.picture["image"] = self.ball
        return self.picture
        
    def display(self,message):
        self.picture.grid_remove()
        #deletes the previous pic of the eightball
        
        self.picture = tk.Label(self)
        self.picture.grid(row = 4, column = 0, columnspan = 3, pady = 5, padx = 5)
        self.ball2 = tk.PhotoImage(file = "magic8ball2.gif")
        self.picture["image"] = self.ball2
        #puts in the new picture of the eightball
        
        answers = tk.Text(self, width = 17, height = 6, bg = 'blue', fg = 'white', wrap = 'word')
        answers.config(font ='bold')
        answers.grid(row = 4, column = 0, columnspan = 1)
        #sets up the answer box

        answers["state"] = "normal"
        answers.delete(0.0,'end')
        answers.insert(0.0,message)
        answers["state"] = "disabled"
        #puts the message in the answer box

        self.question.delete(0,'end')
        #this will delete the question you asked
           
    def validate(self):
        question = self.question.get()
        if question == '':
            message = "You didn't enter anything."
            self.display(message)
        elif question.isdigit():
            message = "I am not a calculator! Please enter a question in words."
            self.display(message)
        elif not question.endswith("?"):
            message = "Was that a question? You forgot the question mark."
            self.display(message)
        elif not " " in question:
            message = "No one-word questions please."
            self.display(message)
        else:
            # this creates the 'Shake' sound
            #winsound.PlaySound("shake_sound.wav", winsound.SND_ALIAS)
            self.submit_answer()
            

    def validate2(self,event):
        '''
gets the question from the question box and checks 
calls self.display to return the message if error otherwise self.submit_answer
is used
The self parameter is the Frame widget from tkinter
The event parameter is pushing 'Enter' on the keyboard
'''
        question = self.question.get()
        if question == '':
            message = "You didn't enter anything."
            self.display(message)
        elif question.isdigit():
            message = "I am not a calculator! Please enter a question in words."
            self.display(message)
        elif not question.endswith("?"):
            message = "Was that a question? You forgot the question mark."
            self.display(message)
        elif not " " in question:
            message = "No one-word questions please."
            self.display(message)
        else:
            # this creates the 'Shake' sound
            winsound.PlaySound("shake_sound.wav", winsound.SND_ALIAS)
            self.submit_answer()
            
    def submit_answer(self):

        responses = ["It is certain!",
             "It is decidedly so",
             "Without a doubt!",
             "Yes definitely!",
             "You may rely on it",
             "As I see it, yes.",
             "Most likely",
             "Outlook good",
             "Yes!",
             "Signs point to yes",
             "Reply hazy try again",
             "Ask again later",
             "Better not tell you now",
             "Cannot predict now",
             "Concentrate and ask again",
             "Don't count on it",
             "My reply is NO!",
             "My sources say no",
             "Outlook not so good",
             "Very doubtful",
             "Yes, in due time",
             "Definitely not",
             "You will have to wait",
             "I have my doubts",
             "Outlook so so",
             "Looks good to me",
             "Who knows?",
             "Looking good!",
             "Probably",
             "Are you kidding?",
             "Go for it!",
             "Don't bet on it",
             "Forget about it."]
        
        message = random.choice(responses)
        self.display(message)

win = Magic8Ball() # assigns win to the Main Frame Window
win.mainloop() # Puts the program in loop so it doesn't quit until the user
               # exits out


                      


