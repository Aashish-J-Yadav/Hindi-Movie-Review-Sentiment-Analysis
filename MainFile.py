from tkinter import *
from SentimentClassification import run_ans

window=Tk()
window.title("Movie Review System")

def from_kg():
    x=run_ans(e2_value.get())
    if x==0:
        x="Negative"
    else:
        x="Positive"
    t2.delete("1.0", END)
    t2.insert(END,x)

e1=Label(window,text="Input :")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b1=Button(window,text="Review",command=from_kg)
b1.grid(row=0,column=2)

t1=Label(window,text="Output :")
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)


window.mainloop()
