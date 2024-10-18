from tkinter import *
window=Tk()
def my7():
    mylabel7=Label(text=7)
    mylabel7.pack()
    

button=Button(window,text="7",command=my7,fg='Green',bg='yellow')
button.pack()


window.mainloop()
