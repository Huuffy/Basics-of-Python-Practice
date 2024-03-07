#no close key added this was a practice
from tkinter import *


def assignsymbol(btn):
    global symbol,rounds
    if btn['text']!='':
        return
        
    btn['text']=symbol#btn text gives access to what is n the text
    
    if symbol=="X":
        symbol="O"
        lbl.configure(text="This is O's")
    else:
        symbol="X"
        lbl.configure(text="This is X's")
    rounds+=1
    
        
         
g=('Arial',50)  
window=Tk()
window.title('Tic tac toe')
window.geometry('600x700')

symbol='X'
rounds=0
f=('Arial',16)

btn1=Button(window,text="",command=lambda:assignsymbol(btn1),font=g)
btn1.grid(row=0,column=0,sticky='nsew')

btn2=Button(window,text="",command=lambda:assignsymbol(btn2),font=g)
btn2.grid(row=0,column=1,sticky='nsew')

btn3=Button(window,text="",command=lambda:assignsymbol(btn3),font=g)
btn3.grid(row=0,column=2,sticky='nsew')

btn4=Button(window,text="",command=lambda:assignsymbol(btn4),font=g)
btn4.grid(row=1,column=0,sticky='nsew')

btn5=Button(window,text="",command=lambda:assignsymbol(btn5),font=g)
btn5.grid(row=1,column=1,sticky='nsew')

btn6=Button(window,text="",command=lambda:assignsymbol(btn6),font=g)
btn6.grid(row=1,column=2,sticky='nsew')

btn7=Button(window,text="",command=lambda:assignsymbol(btn7),font=g)
btn7.grid(row=2,column=0,sticky='nsew')

btn8=Button(window,text="",command=lambda:assignsymbol(btn8),font=g)
btn8.grid(row=2,column=1,sticky='nsew')

btn9=Button(window,text="",command=lambda:assignsymbol(btn9),font=g)
btn9.grid(row=2,column=2,sticky='nsew')

lbl=Label(window,text="This is X's",font=f)
lbl.grid(row=3,column=1)

window.rowconfigure(0,minsize=200)
window.rowconfigure(1,minsize=200)
window.rowconfigure(2,minsize=200)

window.columnconfigure(0,minsize=200)
window.columnconfigure(1,minsize=200)
window.columnconfigure(2,minsize=200)








