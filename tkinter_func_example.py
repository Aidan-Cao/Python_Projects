from tkinter import * # Button, btn=Button(), btn.grid();rt=TK(), rt.title, rt.geometry

root = Tk()
root.grid()
bttn_clicks = 0
root.title("Click Counter")
root.geometry('200x200')
bttn = Button()
bttn2 = Button()

def create_widget():
    bttn['text'] = "Total Clicks: 0"
    bttn['command'] = update_count
    bttn.grid()

    bttn2['text'] = "Restart"
    bttn2['command'] = restart
    bttn2.grid()

def update_count():
    global bttn_clicks
    bttn_clicks += 1
    bttn['text'] = "Total Clicks: " + str(bttn_clicks)
    print("Total Clicks: ", bttn_clicks)

def restart (): 
    global bttn_clicks
    bttn_clicks = 0
    bttn['text'] = "Total Clicks: 0" + str(bttn_clicks)
    print("Total Clicks: 0")

create_widget()

root.mainloop()    
