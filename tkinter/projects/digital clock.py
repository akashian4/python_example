from tkinter import *
from time import strftime

root=Tk()
root.title("Digital Clock")

def time():
    string=strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000,time)

lbl=Label(root,font=('calibri',40,'bold'),
          background='purple',
          foreground='white')
lbl.pack(anchor='center')

time()
root.mainloop()
