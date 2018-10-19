#importing from TKinter class so can use it now
from tkinter import* 
#define functions
def checkIsInteger(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

def checkTitleNoInt(x):
	testString = str(x)
	for i in x:
		if i.isdigit() == True:
			return False
			break
	else:
		i+=1

def record_expense():
	expense_file = open("expenses.txt", 'a')
	nameOnList = nameItem_value.get()
	priceOnList = price_value.get()
	expense_file.write(str(nameOnList) + "," + str(priceOnList) + "\n")

def display_expense():
	expense_file = open("expenses.txt", 'r')
	print("Price \t\t Category")
	for line in expense_file:
		line = line.split(',')
		print(line[0].rjust(3) + "\t\t" + line[1].rjust(7), end= "")

def saveValues():
	print("Name of the item: ", nameItem_value.get())
	print("Price of the item: ", price_value.get())

#don't need this function, but just incase we want to create a window, here is a good reference
def createNewWindow():
	recordExpense = Toplevel()
	recordExpense.geometry("500x500")
	Label(recordExpense, text = "Name of Item: ").grid(row = 0)
	Label(recordExpense, text = "Price of item: ").grid(row = 1)
	#when you create the textbox, you need to define the variable to link it to in order to retrieve it
	nameItem = Entry(recordExpense, textvariable = nameItem_value)
	price = Entry(recordExpense, textvariable = price_value)

	nameItem.grid(row = 0, column = 1)
	price.grid(row = 1, column = 1)

	saveButton = Button(recordExpense, text = "Job's Done", fg = "Blue", bg = "Grey", command = checkIsInteger(str(price_value.get())) and recordExpense)
	saveButton.grid(row = 2, column = 1)
	
	recordExpense.mainloop()

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
appTitle = Label(text = "Expense Calculator", bg = "Grey", fg = "White")
#when you don't care where the object is placed, but you just want it display in window
appTitle.pack(fill = BOTH, expand = True)
#creating containers to place windows or widgets or objects in seperate areas of the entire screen	
topFrame = Frame(mainWindow)
topFrame.pack(side = TOP)

bottomFrame = Frame(mainWindow)
bottomFrame.pack(side = BOTTOM)

#defining variables
nameItem_value = StringVar()
price_value = StringVar()

#creation of button: Button(location, text, fg = (text color)) or bg = background color
quitButton = Button(text = "Quit", fg = "blue", bg = "Grey", command = quit)
recordButton = Button(text = "Record Expenses", fg = "red",bg= "Grey", command = createNewWindow)
displayButton = Button(text = "Display Expenses", fg = "red",bg= "Grey", command = display_expense)
#by default, pack stacks objects on top of one another. 
#define side = to specify where on window you want

recordButton.pack(in_ = topFrame, side = LEFT)
quitButton.pack(in_ = topFrame, side = RIGHT)
displayButton.pack(in_ = topFrame, side = LEFT)

#place window in infinite loop, keeps it displayed, until you press close
mainWindow.mainloop()