# Python Beginners Tutorial, Introduction to loops
# Daniel McCormick - November 10, 2017 

# When coding you sometimes want to do an action a set amount of times
# for example if you wanted to output all numbers from 1 to 10 you could 
print (1)
print (2)
print (3)
print (4)
print (5)
print (6)
print (7)
print (8)
print (9)
print (10)
# or if you wanted to increase the numbers in a list by 1 you could 
shortList = [1,2,3,4]
shortList[0] = shortList[0] + 1;
shortList[1] = shortList[1] + 1;
shortList[2] = shortList[2] + 1;
shortList[3] = shortList[3] + 1;

# or you could simply use a loop. The idea behind a for loop is the computer will keep on 
# doing actions until a certain condition is met

for number in range(10):
	print (number)
	
# THe code above will loop until number is equal to or more then 10, 
# and increase the number by 1  each time it loops

for number in range(-1,10):
	print (number)

# What the above does is loops until number is equal to or more then 10, 
# and increase it by 1  each time it loops but it starts at -1

for number in range(-5,5,10):
	print (number)

# What the above does is loops until number is equal to or more then 10, 
# and increase it by 10  each time it loops but it starts at -5


# Instead of a number you can give the loop a List
classes = ['calulus',"programming","goosology","modern salt harvesting techniques"]
for anyNameYouWant in classes:
	print (anyNameYouWant)
	
# This is also valid
for index in range(len(classes)):
	print (classes[index])
	
# len() returns the length of a list, so we are simply giving it the length of the list
	
# Now if your turn! Print all the integers between 1 and 10!
#(Bonus points: use an if statement to print out if each number is even or odd)
	
# Sometimes you don't want to do things a set amount of times, you just want to do things while a condition is true
# In this case, a while loop may be more useful for what you want

listOfStuff = ["Cat", 3, "Innovation", 12j + 3, "Mr. Goose", -17]
stillMissing = True
index = 0
while (stillMissing == True) :
	if (listOfStuff[index] == "Mr. Goose"):
		print ("PRAISE MR GOOSE")
		stillMissing = False
	else:
		index = index + 1

#this will operate, until Mr. Goose is found.
#Be careful, because if the the loop never ends, you'll be stuck in your while loop indefinitely.
# the code below is an example
		
# alwaysTrue = (true) 
# while (alwaysTrue == true)
# 	print ("HELP I'M STUCK IN A LOOP")
##
# This will always be true since a tuple can't be changed, and nothing inside the loop is changing it, therefore it can never be false
# However, there is overlap between these loops, and they can be used similarly. For example
print ("This is from a for loop")
for number in range (1,11):
	print (number)
	
# this should print out all numbers from one to ten. However, you can achieve the same with a while loop;

print ("However, this is from a while loop")
counter = 1;
while (counter < 11) :
	print (counter)
	counter = counter+1
	
# this should do the same

#Now it's your turn again!
numbers = ["last",4,5,6,7,8,3,4,5,6,7,"first"]
# print this list backwards
# hint (there are 11 elements)
