# WIE Python Beginners Tutorial, Introduction to if statements 
# Daniel McCormick - November 8, 2017

# When coding you sometimes want your code to do things conditionally
# One way to check this conditions is with an if statement

logicStatement = True

if(logicStatement == True):
	print ("This statement is true, since logicStatement is true\n")

# It's important to know the difference between the use of "=" and "==".
# When you give the a value to something you use =;
# However, when you want to compare compare the value of two things you use == 

# For example 
average = 50
# Sets the variable average to 50 and then
if (average == 50): 
	print ("This statement is true if average is equal to 50")
# compares average to 50
# something worth noting is you can use ">" and "<" in if statements, to compare relative to a number
if (average > 60):
	print ("This statement won't print, because average is not greater than 60")
if (average < 60): 
	print ("This statement will print, because average is less than 60\n")



# The second thing that is important to note is the fact that the secon	d line 
# is indented. Unlike other languages, spaces in python matter ... a lot. 
# the if statement ends when the indentation ends


if(logicStatement == False):
	print ("This will not print")
print("This statement will, since it's not in an if statement")

# however, you can also check to see if things are not equal using "!="
if (logicStatement == False) :
	print ("This won't print because it isn't false")
if (logicStatement != False) :
	print ("This statement will print, because logicStatement is NOT false \n")

# you can also combine evaluatoins to have more complex concepts
# "and" will only be true if the statement on the left side and right side are true
if (logicStatement == False and average == 50): 
	print("This will not print, because logicStatement is true")
if (logicStatement == True and average == 50):
	print("This will print, since both conditions are true")
# If you only need one condition to be true, you can use "or" to be true if any statement is true

if (logicStatement == False or average == 50):
	print("This will print since at least one statement is true")
if (logicStatement == True or average == 50): 
	print("The statement will still print if more than one statement is true\n")
# In addition to the if statement there is an else if. Which checks the first statement,
# and if it's not true, it'll check the elsif

if(average == 90):
	print ("This will not print")
elif(average == 52):
	print ("This won't print either")
elif(average == 50):
	print ("However, this one will print")

# You can also use an else statment, which will excute if no if statement was found to be true

if(logicStatement == False):
	print ("This will not print")
else:
	print ("This statement will print if logicStatement does not")
	
# You can use else and else if together and are not limited to the number of 
# checks you have. The only rule is you need to start with an if and if you have 
# and else it must be the last check 

## CHALLENGES FOR THE USER
# Given a number, you want to check to see if it's within a valid range (say, 1-100)

from random import randrange, uniform
number = randrange(-200, 200) #generates a number between -200 and 200
print ("THE NUMBER IS " + str(number))
# put your IF statement here
	print("The number is valid\n")
else:
	print("The number is not valid\n")

# Now, we want you to check only if a number is outside the valid range (say, outside of 1-100)
#
secondNumber = randrange(-200, 200)
print ("THE SECOND NUMBER IS" + str(secondNumber))
#put your IF statement here
	print("This number is valid\n")
else: 
	print("This number is not valid\n)
#
#