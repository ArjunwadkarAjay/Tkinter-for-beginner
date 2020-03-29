from tkinter import *
root=Tk()#blank widow
one=Label(root,text="ONE",bg="black",fg="white")
one.pack()
two=Label(root,text="TWO",bg="green",fg="white")
two.pack(fill=X)
three=Label(root,text="THREE",bg="blue",fg="white")
three.pack(side=LEFT,fill=Y)



root.mainloop()#window constantly display

