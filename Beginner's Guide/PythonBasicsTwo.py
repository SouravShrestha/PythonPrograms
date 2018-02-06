#Strings
var1 = "Sourav Shrestha"
var2 = "Python"
print var2[0] #P
print var1[0:9] #Sourav Sh
print var2[0:56] #Python
print var1,"And",var2 #Sourav Shrestha And Python
print var2[0:3] + "Rest" #PytRest


#Lists
list1 = [19,29,39,49,59,69,79,89,99]
print list1[2:4] #[39,49] (2nd to 4-1th index)
print list1[8] #99
list1[2] = 22 
print list1 #[19,29,22,49,59,69,79,89,99]
del list1[0] 
print list1 #[29,22,49,59,69,79,89,99]
print len(list1) #8
print list1 + [7,8] #[29,22,49,59,69,79,89,99,7,8]
print list1 * 2 #[29,22,49,59,69,79,89,99,29,22,49,59,69,79,89,99]
print 22 in list1 #True
list1.append('Hello')
print list1 #[29,22,49,59,69,79,89,99,'Hello']
freq = list1.count(99)
print freq #1


#Tuples (CANNOT BE CHANGED)
tup = (9,8,56)
print tup #(9,88,56)
del tup
tup1 = (9,)
print tup1[0] #9

#Dictionary
dic = {'Name':'Sourav','Age':20}
print dic['Name'] #Sourav
print dic #{'Name':'Sourav','Age':20}