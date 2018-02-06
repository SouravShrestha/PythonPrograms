
# Print Hello World
print "Hello World"

#Variables
a = 15
b = 15
x = "This is a String"
print a + b
print x


# If Else
if a > b:
	print "%d Is Greater" %a
elif b > a:
	print "%d Is Greater" %b
else:
	print "%d And %s are same" %(a,b)


# While Loop
count = 0
while count < 2:
	n = raw_input("Enter A Number : ")
	print "You Entered ",n
	count = count + 1

print "Loop Ended, count = %d" %count


#For Loop
for letter in 'Sourav':
	print letter

names = ['Sourav','Ram','Andrew','Harry']
for name in names:
	print name

#For Loop Using Range 
for index in range(len(names)):
	print names[index]

