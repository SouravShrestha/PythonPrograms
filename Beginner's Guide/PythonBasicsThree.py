# Functions
def display(s):
	print(s)
	#return;

display('Sourav')



def printInfo(age,name='Default Name'):
	print('Name :',name)
	print('Age :',age)
	return;

printInfo(50,'Sourav')
printInfo(90)
printInfo(age=90,name='Anything')


#(Always Pass By Reference i.e. Value Changes)
def funList(listMe):
	listMe.append('AppendedString') #[9,19,'AppendedString']
	print(listMe)
	return;

listMe1 = [9,19]
funList(listMe1)
print(listMe1) #[9,19,'AppendedString']