from tkinter import *
window=Tk()
window.title("SPEED CALCULATOR")
enter=Entry(window,font=('arial',10, 'bold'),width=40,bg='powder blue',fg='black',borderwidth=7,bd=20,insertwidth=4,justify='right')
enter.grid(row=0,column=0,columnspan=3)

#defining function
def myfunction(number):  #number
     current=enter.get()
     enter.delete(0,END)
     enter.insert(0,str(current)+str(number))
#DEFINING CLEAR FUNCTION
def clear():
    enter.delete(0,END)
#ADD
def add():
    first_number=enter.get()
    global f_num
    global math
    math="add"
    f_num=int(first_number)
    enter.delete(0,END)
#multiply
def multiply():
    first_number=enter.get()            
    global f_num
    global math
    math="multiply"
    f_num=float(first_number)
    enter.delete(0,END)
#divide
def divide():
    first_number=enter.get()
    global f_num
    global math
    math="devide"                                      #f_num is the first number
    f_num=float(first_number)
    enter.delete(0,END)
#subtract
def subtract():
    first_number=enter.get()
    global f_num
    global math
    math="subtract"
    f_num=int(first_number)
    enter.delete(0,END)
#DEFINE EQUAL
def equal():
    second_number=enter.get()
    enter.delete(0,END)

    if math=="add":
        enter.insert(0, f_num+int(second_number))
    if  math=="multiply":
        enter.insert(0, f_num*int(second_number))
    if  math=="devide":
        enter.insert(0, f_num/int(second_number))
    if  math=="subtract":
        enter.insert(0, f_num-int(second_number))



    
#LISTING BUTTONS 
butt7=Button(window,text='7',padx=40,pady=20,command=lambda:myfunction(7))
butt8=Button(window,text='8',padx=40,pady=20,command=lambda:myfunction(8))
butt9=Button(window,text='9',padx=40,pady=20,command=lambda:myfunction(9))
butt4=Button(window,text='6',padx=40,pady=20,command=lambda:myfunction(6))
butt5=Button(window,text='5',padx=40,pady=20,command=lambda:myfunction(5))
butt6=Button(window,text='4',padx=40,pady=20,command=lambda:myfunction(4))
butt1=Button(window,text='3',padx=40,pady=20,command=lambda:myfunction(3))
butt2=Button(window,text='2',padx=40,pady=20,command=lambda:myfunction(2))
butt3=Button(window,text='1',padx=40,pady=20,command=lambda:myfunction(1))
butt0=Button(window,text='0',padx=40,pady=20,command=lambda:myfunction(0))
butt_add=Button(window,text='+',padx=40,pady=20,command=add)
butt_CL=Button(window,text='CL',padx=40,pady=20,command=clear)
butt_equal=Button(window,text='=',padx=40,pady=20,command=equal)
butt_multiply=Button(window,text='*',padx=40,pady=20,command=multiply)
butt_devide=Button(window,text='/',padx=40,pady=20,command=divide)
butt_subtract=Button(window,text='-',padx=130,pady=30,command=subtract)
#ALIGNING BUTTONS
butt7.grid(row=1,column=0)
butt8.grid(row=1,column=1)
butt9.grid(row=1,column=2)
butt4.grid(row=2,column=0)
butt5.grid(row=2,column=1)
butt6.grid(row=2,column=2)
butt1.grid(row=3,column=0)
butt2.grid(row=3,column=1)
butt3.grid(row=3,column=2)
butt0.grid(row=4,column=0)
butt_add.grid(row=4,column=1)
butt_CL.grid(row=4,column=2)
butt_equal.grid(row=5,column=0)
butt_multiply.grid(row=5,column=1)
butt_devide.grid(row=5,column=2)
butt_subtract.grid(row=6,column=0,columnspan=3)
    

    
window.mainloop()
