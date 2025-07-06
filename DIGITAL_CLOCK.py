from tkinter import *

from time import *



def Time():
    time_string=strftime('%H:%M:%S %p')
    label_1.config(text= time_string)
    label_1.after(100,Time)

tm =Tk()
tm.title('Tick Tock Tkinter')

tm.attributes('-alpha', 0.5)


heading=Label(text="CodeCraft", font=(30),bg= 'black', fg ='cyan')
heading.pack(fill=X)


label_1=Label(tm,font=('ds-digital',100), bg= 'black', fg ='orange')

label_1.pack()
Time()
tm.mainloop()