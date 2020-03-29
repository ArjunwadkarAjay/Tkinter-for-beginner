from tkinter import *
root=Tk()#blank widow
def printName():
    print ("My name is Ajay Arjunwadkar")

button1=Button(root,text="Print my Name",command=printName)
## command binding a function to widget
button1.pack()



root.mainloop()#window constantly display


