from tkinter import *
from PIL import ImageTk,Image
window=Tk()
window.title("BLAZE")
window.iconbitmap('c:/image/backblaze.ico')
image=ImageTk.PhotoImage(Image.open('c:/image/justworks.ico'))
label=Label(image=image)
label.pack()







window.mainloop()
