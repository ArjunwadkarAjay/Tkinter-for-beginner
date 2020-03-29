from tkinter import *
root=Tk()#blank widow
def printName(event):
    print ("My name is Ajay Arjunwadkar")

button1=Button(root,text="Print my Name")
## command binding a function to widget
button1.bind("<Button-1>",printName)
#event ,function to call
button1.pack()



root.mainloop()#window constantly display


