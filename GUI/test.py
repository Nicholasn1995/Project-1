#importing from TKinter class so can use it now
from tkinter import* 

#define functions
def printSomething():
	print("This works!")
#creates a blank window
#every GUI has to have this and mainloop
mainWindow = Tk()
#sets size of window at start up
mainWindow.geometry("500x500")
#makes window unable to be resized by users
mainWindow.resizable(width = False, height = False)
#to populate the window with a label, create using Label(location, x)
#pack(fill =x) button will stretch however long window is stretched (left and right)
#replace above with y, will stretch height wise
#fill = BOTH, expand = True, will dynamically change both x and y
appTitle = Label(mainWindow, text = "Expense Calculator", bg = "black", fg = "White")
#when you don't care where the object is placed, but you just want it display in window
appTitle.pack(fill = BOTH, expand = True)
#creating containers to place windows or widgets or objects in seperate areas of the entire screen	
topFrame = Frame(mainWindow)
topFrame.pack()

bottomFrame = Frame(mainWindow)
bottomFrame.pack(side = BOTTOM)

#creation of button: Button(location, text, fg = (text color)) or bg = background color
button1 = Button(topFrame, text = "This works Top", fg = "blue", command = quit)
button2 = Button(bottomFrame, text = "This works bottom", fg = "red", command = printSomething)
#by default, pack stacks objects on top of one another. 
#define side = to specify where on window you want

button2.pack()
button1.pack()
#place window in infinite loop, keeps it displayed, until you press close
mainWindow.mainloop()