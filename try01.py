from tkinter import *
root=Tk()#blank widow
#frame dividing page
topFrame=Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
#button
button2=Button(topFrame,text="button1",fg="yellow")
button3=Button(topFrame,text="button2",fg="orange")
button4=Button(topFrame,text="button3",fg="green")
button5=Button(bottomFrame,text="button4",fg="blue")
button1=Button(bottomFrame,text="button5",fg="red")
#button dispaly
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=BOTTOM)




root.mainloop()#window constantly display

