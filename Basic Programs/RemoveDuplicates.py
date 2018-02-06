str = raw_input("Enter A Sentence ")
words = str.split(" ")
removedList = set(words)
newStr = ""
for w in removedList:
	newStr = newStr + w + " "
print newStr