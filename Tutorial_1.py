# WIE Python Beginners Tutorial, Introduction to variables 
# Daniel McCormick - November 9, 2017

# In python there are several types of variables
# A variable is a type of data


# One such type of data is Numbers
a = 10;    # Integers are numbers without decimal places 
b = 10.0;  # Floating point numbers are numbers with decimals
c = 3.14j  # Complex Numbers are numbers with imaginary components (ie the square roof of negative 1)

# Strings are another type of data
d = 'Hello World !'
e = "Hello World !"
# Note that the string d is equal to the string e

# Lists (A great things about python)
# List entries could all be the same type 
sameTypeList  = [1,2,3,4]
sameTypeList2 = ['one',"two",'three',"four"]

# List entries can also be anything
whyPythonIsSometimesBetterThenC = [1,"alpha",3.2j,"Pie","afro", switzerland]

# A speciall type of lists are called Tuples 
# Tuples are read-only
# A list is dynamic, it's size and content can change at any time
shortList = [1]
shortList[0] = 5

#You can't change the value of tuples
shortTuple = ("This", "Can't", "Be", "Changed")
# The line below is invaild 
# shortTuple[0] = 5

# The last type is a Dictionary, which is nothing more than a list whose index 
# could be anything 
exampleDictionary = {}
exampleDictionary['Pie'] = 'MorePie'
exampleDictionary[1] = 'LessPie'
exampleDictionary[10] = 'PiePiePie' 

# In order to only have one print statement we need to wrap our none string 
# variables # in str() which converts the variable into a string. Note we could've 
# and maybe # should've had 2 print statements and no str()
print ('a = ' + str(a))
print ('b = ' + str(b))
print ('c = ' + str(c))
print ('d = ' + d)
print ('e = ' + e)
print ('shortTuple = ' + str(shortTuple))
print ('sameTypeList = '+ str(sameTypeList))
print ('sameTypeList2 = ' + str(sameTypeList2))
print ('exampleDictionary = ' + str(exampleDictionary))
print ('whyPythonIsSometimesBetterThenC = ' + str(whyPythonIsSometimesBetterThenC))
print ("\nNow it's your turn:")
print ("What's your name?")
# Try it out for yourself! Print your name here!

print ("What's your favorite number?")
value
# assign your favorite number to the value
#print the number out!