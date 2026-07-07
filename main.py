import module # This is how we import a module.

print('Hello world') # This is a comment.

# The most common data types we typically store in variables are: text, integers and decimals, booleans, lists or arrays, as well as maps, objects, or dictionaries.

# Variables
book = "The Pragmatic Programmer." # This is a string variable.

integer = 26 # This is an integer variable.
decimal = 1.95485 # This is a decimal variable.

authorized = True # This is a boolean variable.
selected = False # This is a boolean variable.


# Data structures: Lists -> They allow us to store many types of data in an organized way.
numbers = [23, 45, 16, 37, 3, 99, 22] # This is a list variable.
print(numbers[0])

# Text list
animals = ["dog", "cat", "bird", "fish"] # This is a list of animals.
mixedData = ["text", 69, True, ["List within another list"]]

# We also have maps, objects, or dictionaries. -> These allow us to access a property very quickly using just a key.
players = {
    10: "Lionel Messi",
    7: "Cristiano Ronaldo",
}
print(players[7]) # This will return "Cristiano Ronaldo".

# Constants
PI = 3.14159 # This is a constant. It is a good practice to use uppercase letters for constants.
DAYS_OF_THE_WEEK = 7
URL_API = "https://example.com"

# Although Python won't prevent you from modifying its value, the convention indicates to other programmers that it should not be changed.

# Operators

# Arithmetic
print(4 + 5) # This will return 9.
print(4 - 5) # This will return -1.
print(4 * 5) # This will return 20.
print(4 / 5) # This will return 0.8.
print(4 % 5) # This will return 4.
print(4 ** 5) # This will return 1024.
print(12382 * 777090)

# TRUE
print(4 == 4) # This will return True.
print(4 != 5) # This will return True.
print(4 > 3) # This will return True.
print(4 < 5) # This will return True.
print(4 >= 4) # This will return True.
print(4 <= 5) # This will return True.

# FALSE
print(4 == 5) # This will return False.
print(4 != 4) # This will return False.
print(4 == "4") # This will return False because the data types are different (integer vs string).

# Identity operator
integer = 100
print(integer is integer) # This will return True because the variable "integer" is equal to 100.

# Logical operators
print(True and True) # This will return True.
print(True and False) # This will return False.
print(False and True) # This will return False.
print(False and False) # This will return False.


print(True or True) # This will return True.
print(True or False) # This will return True.
print(False or True) # This will return False.
print(False or False) # This will return False.

# Conditionals
authorized = False # This is a boolean variable.
if authorized:
    print("You can log in.")
else:
    print("You cannot log in.")

# Another example
integer = 100
if integer == 99:
    print("Is 99")
elif integer == 100:
    print("Is 100")
else:
    print("Is not 99 or 100")

# Conditional Match
color = "yellow"
match color:
    case "green":
        print("Success!")
    case "yellow":
        print("Warning!")
    case _: # To capture additional situations, we use the underscore or low line.
        print("Error!")

# Functions
def add(first, second):
    return first + second
result = add(24, 76)
print(result)


def multiply(first, second):
    return first * second
result = multiply(24, 76)
print(result)

def printFirstElement(lst):
    print(lst[0])
printFirstElement([1, 2, 3, 4, 5]) # This will print 1.


def quicksort(lst):
    if len(lst) <= 1:
        return lst
    
    pivot = lst[0]
    left = []
    right = []
    for i in range(1, len(lst)):
        left.append(lst[i]) if lst[i] < pivot else right.append(lst[i])
    return quicksort(left) + [pivot] + quicksort(right)

numbers = [23, 45, 16, 37, 3, 99, 22]
listOrdered = quicksort(numbers)
print(listOrdered) # This will print the ordered list: [3, 16, 22, 23, 37, 45, 99].


# CYCLES OR LOOPS
animals = ["dog", "cat", "bird", "fish", "tiger"]
for animal in animals:
    print(animal) # This will print each animal in the list.



def multiply(first, second):
    return first * second
numbers = [23, 45, 16, 37, 3, 99, 22]
for number in numbers:
    result = multiply(number, 2) # This will multiply each number in the list by 2.
    print(result)

integer = 100
emergency = 911
# Cycle "While"
while integer < emergency:
    print(integer)
    integer += 1 # This will increment the value of "integer" by 1 in each iteration.


# OBJECT-ORIENTED PROGRAMMING (POO)
javascript = {
    'name': 'JavaScript',
    'year': 1995
}

# def description():
#     print("%s was created in %s." % (javascript['name'], javascript['year']))
# description() # This will print "JavaScript was created in 1995."

# Classes
class Language:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def description(self):
        print("%s was created in %s." % (self.name, self.year))

# Create an instance of the language class
javascript = Language("JavaScript", 1995)
javascript.description() # This will print "JavaScript was created in 1995."

html = Language("HTML", 1993)
html.description() # This will print "HTML was created in 1993."
css = Language("CSS", 1996)
css.description() # This will print "CSS was created in 1996."

# MODULES
# A module is a file that contains Python code. It can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use.
import module

module.subtract(10, 2)
# This is how "libraries" are created.
