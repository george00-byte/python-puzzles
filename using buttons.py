from tkinter import *
window=Tk()
def myfunction():
    myfunction=Label(window,text= 3+2)
    myfunction.pack()
Mybutton=Button(window,text="0", padx='2',pady='4',command=myfunction)
Mybutton.pack()
window.mainloop()
