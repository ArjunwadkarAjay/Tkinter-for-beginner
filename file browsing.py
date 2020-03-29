from  tkinter import filedialog
from tkinter import *

root = Tk()
root.directory = filedialog.askopenfilename(initialdir="/",title="Select file",filetype=(("jpeg files","*.jpg"),("All Files","*.*")))
print (root.directory)
