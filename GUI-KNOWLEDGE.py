from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk()
GUI.title('programe')
GUI.geometry('500x400')
"""
b1= ttk.Button(GUI,text='input')
b1.pack(ipadx=20,ipady=10)
"""
l1=Label(GUI,text='first time',font=('Times New Roman',30),fg='blue')
l1.place(x=30,y=20)

##########
def Button2():
    text = 111
    messagebox.showinfo('i hate you',text) #showarning,showerror

fb1 = LabelFrame(GUI,text='code',fg='red')
fb1.place(x=30,y=80)
b2= ttk.Button(fb1,text='input2',command=Button2)
#b2.pack()
b2.pack(ipadx=20,ipady=20,padx=30,pady=30)
#######





GUI.mainloop()
