from tkinter import *
window=Tk()
window.title("Gui")
Mywindow=Label(window,text="Hey man")
Mywindow2=Label(window,text="How are you doing")
Mywindow.grid(row=0,column=0)
Mywindow2.grid(row=1,column=1)
window.mainloop()
