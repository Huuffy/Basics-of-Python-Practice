from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
def submit():
    global nvar,stdvar,gvar,cvar,fvar,chvar,bvar,resulttxt
    resulttxt.delete(1.0,END)
    resulttxt.insert(INSERT,'Name :'+nvar.get())
    resulttxt.insert(INSERT,'\nStandard: '+stdvar.get())
    resulttxt.insert(INSERT,'\nGender: '+gvar.get())
    resulttxt.insert(INSERT,'\nSports: \n')
    if cvar.get():
        resulttxt.insert(INSERT,'      Cricket\n')
    if fvar.get():
        resulttxt.insert(INSERT,'      Football\n')
    if chvar.get():
        resulttxt.insert(INSERT,'      Chess\n')
    if bvar.get():
        resulttxt.insert(INSERT,'      Basketball\n')
    messagebox.showinfo('Victory','Data stored sucessfully')
    #window.destroy()
    return
window=Tk()
window.title('form')
window.geometry('600x600')

f=('Arial',15)
nlbl=Label(window,text='name',font=f)
nlbl.grid(row=0,column=0)
nvar=StringVar()
nentry=Entry(window,text=nvar,font=f)
nentry.grid(row=0,column=1,columnspan=2)

slbl=Label(window,text='std',font=f)
slbl.grid(row=1,column=0)
stdvar=StringVar()
stdcombo=Combobox(window,text=stdvar,font=f)
stdcombo.grid(row=1,column=1,columnspan=2)
stdcombo['values']=("1","2","3","4","5",'6','7','8','9','10')

glbl=Label(window,text='gender',font=f)
glbl.grid(row=2,column=0)
gvar=StringVar()
mbtn=Radiobutton(window,text='MALE',value="MALE",variable=gvar)
mbtn.grid(row=2,column=1)
fbtn=Radiobutton(window,text='FEMALE',value='FEMALE',variable=gvar)
fbtn.grid(row=2,column=2)



splbl=Label(window,text='sports',font=f)
splbl.grid(row=3,column=0)
cvar=StringVar()
fvar=StringVar()
chvar=StringVar()
bvar=StringVar()
cbtn=Checkbutton(window,text='cricket',onvalue='cricket',offvalue='',variable=cvar)
cbtn.grid(row=3,column=1)

fbtn=Checkbutton(window,text='football',onvalue='football',offvalue='',variable=fvar)
fbtn.grid(row=3,column=2)

chbtn=Checkbutton(window,text='chess',onvalue='chess',offvalue='',variable=chvar)
chbtn.grid(row=3,column=3)

bbtn=Checkbutton(window,text='basketball',onvalue='basketball',offvalue='',variable=bvar)
bbtn.grid(row=3,column=4)

submitbtn=Button(window,text='submit',command=submit)
submitbtn.grid(row=4,column=0)

resulttxt=Text(window,font=f,width=45)
resulttxt.grid(row=5,column=0,columnspan=7)

window.mainloop()
