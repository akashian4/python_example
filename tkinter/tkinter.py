from tkinter import *

win=Tk()
win.title("My App")

#win.minsize(300,300)
#win.maxsize(750,750)

win.geometry('500x500')
#win.resizable(False,False)

#win.withdraw()
#win.wm_withdraw()
#print(win.state())
#win.deiconify()
#win.wm_deiconify()
#print(win.state())

#lbl=Label(win,text="Faradars",
#          font=("Tahoma",10,"bold"),fg="white",bg="black",cursor="target",
#          relief="flat",state="disabled")

def func1(event):
   print("Hello Faradars")
#btn=Button(win,state="normal",relief="ridge",
#           cursor="hand2",command=func1)
#btn.place(x=50,y=150)
#lbl.pack()


#text=Entry(win,width=20,bg="black",fg="white",bd=4,
#           font=("Tahoma",12),show="*")
#text.place(x=100,y=180)




lbl=Label(win,text="click me!")
lbl.bind("<Enter>",func1)
lbl.pack()
win.mainloop()
