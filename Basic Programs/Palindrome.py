while(1):
	str = raw_input("Enter String : ")
	newStr = ""
	for letter in str:
		newStr = letter + newStr
	if(str == newStr):
		print "Palidrome"
	else:
		print "Not Palidrome";
	ch = raw_input("Continue ? (Y/N)").lower()
	if(ch == "n"):
		break;