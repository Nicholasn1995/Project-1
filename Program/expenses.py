def main():
	display_options()
	choice = int(input("Enter your choice: "))
	while choice != 0:
		if choice == 1:
			record_expense()
			display_options()
			choice = int(input("Enter your choice: "))
		elif choice == 2:
			display_expense()
			display_options()
			choice = int(input("Enter your choice: "))
		elif choice == 3:
			check_limit("expenses.txt")
			display_options()
			choice = int(input("Enter your choice: "))
		elif choice == 0:
			exit()

def display_options():
	print("\nWhat would you like to do? \n")
	print("1. Record an Expense")
	print("2. View Expenses")
	print("3. Check Limit")
	print("0. Exit \n")

def record_expense():
	expense_file = open("expenses.txt", 'a')
	amount = int(input("How much is your expense?"))
	category = input("What type of expense is this?")
	expense_file.write("\n" +str(amount) + "," + category)
	
	
def display_expense():
	expense_file = open("expenses.txt", 'r')
	print("Price \t\t Category")
	for line in expense_file:
		line = line.split(',')
		print(line[0].rjust(3) + "\t\t" + line[1].rjust(7), end= "")

def check_limit(file):
	limit = 50
	total = 0
	for line in open(file, 'r'):
		line = line.split(',')
		total += float(line[0])
	if total > limit:
		print("Limit exceeded!")


main()