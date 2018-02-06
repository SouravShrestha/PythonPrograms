str = raw_input("Enter A Sting : ")
count = {}
for letter in str:
	count[letter] = 0
for letter in str:
	count[letter] += 1
print count
a = count.items()
for k,c in a:
	print "Frequecy Of",k,"Is",c