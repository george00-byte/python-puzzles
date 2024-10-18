from tkinter import *
from PIL import ImageTk,Image

window=Tk()
window.title("kong is good")
window.iconbitmap('c:/image/rockstar.ico')

my_img=ImageTk.PhotoImage(Image.open("c:/image/mailchimp.ico"))
my_label=Label(image=my_img)
my_label.pack()


button_pack = Button(window,text="EXIT",command=window.quit)
button_pack =button_pack.pack()






window.mainloop()
