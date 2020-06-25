from tkinter import * # Button, btn=Button(), btn.grid();rt=TK(), rt.title, rt.geometry

class Aidan_TK(Frame):

    def __init__(self, master):
        super(Aidan_TK, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def restart (self): 
        self.bttn_clicks = 0
        self.bttn['text'] = "Total Clicks: " + str(self.bttn_clicks)
        print ("Total Clicks: " + str(self.bttn_clicks))

    def create_widget(self):
        self.bttn = Button(self)
        self.bttn['text'] = "Total Clicks: 0"

        self.bttn['command'] = self.update_count
        self.bttn.grid()

        self.bttn2 = Button(self)
        self.bttn2['text'] = "Restart"
        self.bttn2['command'] = self.restart
        self.bttn2.grid()

    def update_count(self):
        self.bttn_clicks += 1
        self.bttn['text'] = "Total Clicks: " + str(self.bttn_clicks)
        print("Number of Button clicks is:", self.bttn_clicks)

root = Tk()
root.title("Click Counter")
root.geometry('200x100')

app = Aidan_TK(root)

#root.mainloop()    
