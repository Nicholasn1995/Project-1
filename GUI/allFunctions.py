def checkIsInteger(x):
	try:
		int(x)
		return True
	except ValueError:
		return False

def checkTitleNoInt(x):
	for i in x:
		if i.isdigit() == True:
			return False
			break
		else:
			pass
	return True