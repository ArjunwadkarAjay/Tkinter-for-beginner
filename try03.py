from tkinter import *
root=Tk()#blank widow
label_1=Label(root,text="USER_NAME")
label_2=Label(root,text="PASSWORD")
#entry of the text 
entry_1=Entry(root)
entry_2=Entry(root)
#grid  positions and sticky
label_1.grid(row=0,sticky=E)
label_2.grid(row=1,sticky=E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
#checkbox
c=Checkbutton(root,text="Keep Me Logged IN")
c.grid(columnspan=2)#to consume column




root.mainloop()#window constantly display

