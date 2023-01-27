
'''
    HDLC - Python Internship
    Mini - Project
    Name - Mohit Jaiswal
    Problem - Develop a desktop application - Basic arithmetic calculator which performs addition, subtraction, multiplication, division and mod operation using GUI.
'''

import tkinter
from tkinter import *

root =Tk()
root.title("Calculator by Mohit Jaiswal")
root.geometry("400x580+100+200")
root.resizable(False, False)
root.configure(bg="#000000")

equation =""

def show(value):
    global equation                                                  #For Showing on Screen
    equation+=value
    Screen.config(text=equation)

def clear():
    global equation
    equation=""                                                     #For Clearing the Screen
    Screen.config(text=equation)

def calculate():
    global equation
    result=""
    
    if equation!="":
        try:
            result=eval(equation)                                  #For Performing the Operations by using eval() functions
        except:
            result="error!"
            equation=""

    Screen.config(text=result)


#For Display
Screen = Label(root, width=25, height=4, font=("Arial", 30), bd=5,fg="#ffffff", bg="#000000")
Screen.pack()


#For Buttons
Button(root, text="AC", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: clear()).place(x=10, y=205)
Button(root, text="+/-", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("")).place(x=107, y=205)
Button(root, text="%", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("%")).place(x=207, y=205)
Button(root, text="÷", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#ffffff", bg="#f69906", command= lambda: show("/")).place(x=305, y=205)

Button(root, text="7", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("7")).place(x=10, y=280)
Button(root, text="8", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("8")).place(x=107, y=280)
Button(root, text="9", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("9")).place(x=207, y=280)
Button(root, text="x", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#ffffff", bg="#f69906", command= lambda: show("*")).place(x=305, y=280)


Button(root, text="4", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("4")).place(x=10, y=355)
Button(root, text="5", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("5")).place(x=107, y=355)
Button(root, text="6", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("6")).place(x=207, y=355)
Button(root, text="-", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#ffffff", bg="#f69906", command= lambda: show("-")).place(x=305, y=355)


Button(root, text="1", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("1")).place(x=10, y=430)
Button(root, text="2", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("2")).place(x=107, y=430)
Button(root, text="3", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("3")).place(x=207, y=430)
Button(root, text="+", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#ffffff", bg="#f69906", command= lambda: show("+")).place(x=305, y=430)


Button(root, text="0", width=9, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show("0")).place(x=10, y=505)
Button(root, text=".", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#000000", bg="#9f9f9f", command= lambda: show(".")).place(x=207, y=505)
Button(root, text="=", width=4, height=1,font=("arial", 25, "bold"), bd=1, fg="#ffffff", bg="#f69906", command= lambda: calculate()).place(x=305, y=505)


root.mainloop()