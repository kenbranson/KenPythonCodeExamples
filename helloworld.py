print("Hello, world")
print("Hello World\nThis is a message")

# with variables
x = 2
y = 3
print(x, ' ', y)

s="Hello, world!"
print(s[0])   # printing 1 letter in a string
print(s[:3])  # printing a range from the beginning up to, but not including, 3 (which is actually the 4th position)
print(s[3:])  # prints from 3 to end (including 3)

if "ello" in s:    # searching within a string
    print("Yes, found it")

#getting inputs
name = input("Enter a name: ")
xint = int(input("Give me an integer:"))
xfloat = float(input("Give me a non-integer number:"))

if x == 4:  #ends with :, then indent for code block
    print 'You guessed correctly!'
elif x > 4:
    print "You guessed too high."
else:
    print 'You guessed too low.'

# for loops:
for i in range(1, 11):   # range is a prebuilt generator
    print i

# while loop
while x != 5:
   x = int(input("Guess a number:"))

   if x != 5:
      print("Incorrect choice")
print("Correct!")

# example of defining a function that takes 2 inputs and returns a value
import math

def pythagoras(a,b):
    value = math.sqrt(a*a + b*b)
    return value


result = pythagoras(3,3)
print(result)

#Lists
myList = [1, 3, 5, 7, 9]
print(myList[0])  #accessing a specific item (note: lists are ordered)
print(myList[-1])  #last item in the list
print(len(myList))

#tuples = lists that cannot be modified
myTuple = (1,2,3)
print(myTuple[1])

#dictionary = very similar to a hashmap
myDict = {"Ken":43, "Will":9}
ken_age = myDict["Ken"]  #Reading a value from a dict
print(myDict["Ken"])
myDict["Cheryl"]=43   #adding to a dict
del myDict["Ken"]     #removing an item from the dict
print(myDict)


#reading files
#!/usr/bin/env python
filename = "readme.txt"
with open(filename) as fn:
    content = fn.readlines()
print(content)    #this is a list where each item is a line of text from the file

#writing a file
f = open("output.txt","w")
f.write("Pythonprogramminglanugage.com, \n")
f.write("Example program.")
f.close()


# regular expressions
import re

s = "123"
matcher = re.match('\d{3}\Z',s)   #looks for a match of the given pattern within the given string

if matcher:
    print("True")
else:
    print("False")