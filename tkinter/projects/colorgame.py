from tkinter import *
import random

score=0
timeleft=30

color=['White','Black','Green','Blue','Brown','Pink','Purple','Gray']

def startgame(event):
    if timeleft==30:
        countdown()
    nextcolor()
def nextcolor():
    global score
    global timeleft
    if timeleft>0:
        e.focus_set()
        if e.get().lower()==color[1].lower():
            score+=1
        e.delete(0,END)
        random.shuffle(color)
        label.config(fg=str(color[1]),text=str(color[0]))
        scorelabel.config(text="Score: "+str(score))
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        timelabel.config(text="Time Left: "+str(timeleft))
        timelabel.after(1000,countdown)
root=Tk()
root.title("Color Game")
root.geometry('375x200')
root.resizable(False,False)

scorelabel=Label(root,text="Press Enter To Start",font=('Tahoma',12))
scorelabel.pack()

timelabel=Label(root,text="Time Left: "+str(timeleft),font=('Tahoma',8))
timelabel.pack()

label=Label(root,font=('Tahoma',10))
label.pack()

e=Entry(root)
root.bind('<Return>',startgame)
e.focus_set()
e.pack()
root.mainloop()
