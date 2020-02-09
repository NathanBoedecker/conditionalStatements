'''
For this assignment you should read the task, then below the task do what it asks you to do.
'''

'''
#1) Create a Variable called grade and set it to an integer. Make an if statement that checks if the grade is a passing grade. grade must be above 65 to pass. print out "student is passing"
'''
x=1
if (x >= 65):
    print("student is passing")
'''
#2) Now make an if, else statement that checks if the student is passing but also print "student is failing", if the grade is less than 65
'''
if (x >= 65):
    print("student is passing")
elif(x >= 65):
    print("student is failing")
'''
#3)Create a variable called age. Make and if, else statement that checks if the age entered is old enough to vote. Remember the voting age is 18
'''
x = 17
if(x <= 18):
    print("person is too young to vote")
elif(x <= 18):
    print("person is old enough to vote")
'''
#4)Create a variable called weight. Make an if statement that checks the unit of the weight. If the weight is in kilograms, convert it to pounds 
'''
weightUnit = "kilograms"
weight = 120 
if(weightUnit == "kilograms"):
    weightUnit = "pounds"
    weight = x*2.20462
    print(weight)
'''
#5)Now modify the previous program to also convert from pounds to kilograms
'''
if(weightUnit == "kilograms"):
    weightUnit = "pounds"
    weight = x*2.20462
    print(weight)
elif(weightUnit == "kilograms"):
    weightUnit="kilograms"
    weight=x/2.20462
    print(weight)
    