from tkinter import *
window=Tk()
data = StringVar()
lbl=Label(window, text="Enter the string", fg='red', font=("Helvetica", 12))
lbl.place(x=60, y=50)
txtfld=Entry(window, textvariable = data, bd=5)
txtfld.place(x=80, y=80)

btn1=Button(window, text="Length", fg='blue')
btn1.place(x=80, y=120)

def __init__(self, window):
    self.lbl1(window, text = "Enter the string:")
    
   


    
btn2=Button(window, text="Uppercase", fg='blue')
btn2.place(x=80, y=150)

btn3=Button(window, text="Lowercase", fg='blue')
btn3.place(x=80, y=180)

lbl2=Label(window, text="Result", fg='red', font=("Helvetica", 12))
lbl2.place(x=80, y=220)
txtfld2=Entry(window, bd=5)
txtfld2.place(x=80, y=250)



window.title('Hello Python')
window.geometry("400x300+10+10")
window.mainloop()
