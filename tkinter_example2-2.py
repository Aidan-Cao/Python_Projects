from tkinter import Button, Tk #btn=Button(), btn.grid();rt=TK(), rt.title, rt.geometry

root = Tk()
root.grid()
bttn_clicks = 0
#root.title("Click Counter")
#root.geometry('200x200')


def create_widget():
    bttn['text', 'command'] = ("Total Clicks: 0", update_count)
    #bttn['command'] = update_count
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

bttn = Button(root,text="Total Clicks:", command=update_count)
bttn2 = Button(root, text="Restart", command=restart)

create_widget()

root.mainloop()    
