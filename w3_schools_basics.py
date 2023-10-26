print("COMMENTS")
print("To add a comment on a singel line use a hashtag.")
# Comments are formatted with a hash
print("Multi-line comments start and end with \"\"\"")
"""
This is a comment
written in
more than just one line
"""

print()
print("------------------------------------------------------------------------------------------------------------")
print()
print("PRINT")
print("To print on the terminal use print(\"Hello you!\").")
print("Hello you!")
print()
print("------------------------------------------------------------------------------------------------------------")
print()
print("INDENTATION")
print("Python uses indentation to indicate a block of code.")
print("The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.")
print("You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:")

if 5 > 2:
    print("Five is greater than two!")

print()
print("------------------------------------------------------------------------------------------------------------")
print()
print("VARIABLES")

print("In Python, variables are created when you assign a value to it:")
name = "Rezana"
city = "Londres"

print("Comment tu't appelle?")
print("Je m'appelle " + name)
print("Où habites-tu?")
print("J'habite a " + city)

print()
print("A variable name must start with a letter or the underscore character")
print("A variable name cannot start with a number")
print("A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)")
print("Variable names are case-sensitive (age, Age and AGE are three different variables")
print("A variable name cannot be any of the Python keywords.")
print()

AGE = 30
age = 35
print("age != AGE")
print(age, AGE)
print()
print("Python allows you to assign values to multiple variables in one line:")
print("x, y, z = \"Orange\", \"Banana\", \"Cherry\"")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print()
print("And you can assign the same value to multiple variables in one line")
print("x = y = z = \"Orange\"")
x = y = z = "Strawberry"
print(x)
print(y)
print(z)

print()
print("------------------------------------------------------------------------------------------------------------")
print()

print("CASTING")
print("If you want to specify the data type of a variable, this can be done with casting. int(), str(), float()")
name_string = str("Rezana")
likes_integer = int(1000000)
money_float = float(999999.96)

print()
print("You can get the data type of a variable with the type() function.")

print(name_string, type(name_string))
print(likes_integer, type(likes_integer))
print(money_float, type(money_float))

print()
print("------------------------------------------------------------------------------------------------------------")
print()

print("GLOBAL VARABLES")
print("Variables that are created outside of a function (as in all of the examples above) are known as global "
      "variables.")
print("Global variables can be used by everyone, both inside of functions and outside.")

x = "set the first global, globally"


def my_function():
    global y
    y = "set the second global variable, in my_function()"
    print(x)


my_function()
print(y)

print()
print("------------------------------------------------------------------------------------------------------------")
print()

print("DATA TYPES")

print("Python has the following data types built-in by default, in these categories:\n" +
      "Text Type:	str \n" +
      "Numeric Types:	int, float, complex \n" +
      "Sequence Types:	list, tuple, range \n" +
      "Mapping Type:	dict \n" +
      "Set Types:	set, frozenset \n" +
      "Boolean Type:	bool \n" +
      "Binary Types:	bytes, bytearray, memoryview  \n" +
      "None Type:	NoneType \n")

print()
print("You can get the data type of any object by using the type() function")

x = 5
print(type(x))

print("If you want to specify the data type, you can use str(), int(), float(), list(), tuple(), dict(), set(), "
      "bytes(), bytearray()")

surname = str("dowra")
bond = float(9013340.89)
age = int(18)
data = bytes([65, 66, 67])

# with open("preds.png", "rb") as image:
#     f = image.read()
#     b = bytearray(f)
#     print(b[4])


print()
print("------------------------------------------------------------------------------------------------------------")
print()
import random

print("NUMBERS")

print(random.randrange(1, 10, 1))

print("Casting in python is done using constructor functions")
w = float("4.2")
print(w)
print("w = float(\"4.2\") # w will be 4.2")

print()
print("------------------------------------------------------------------------------------------------------------")
print()

print("STRINGS")

print("Strings in python are surrounded by either single quotation marks, or double quotation marks.")
print('Single Quotation(\')')
print("Double Quotation(\")")

hello = "hello"[0]
print(hello)

print("You can assign a multiline string to a variable by using three quotes:")
long_comment = """     This is often used as
     a format to write long comments 
"""
print(long_comment)

print("Like many other popular programming languages, strings in Python are arrays of bytes representing unicode "
      "characters. "
      "However, Python does not have a character data type, a single character is simply a string with a length of 1.")

print("Since strings are arrays, we can loop through the characters in a string, with a for loop.")

string = "abc"
for character in string:
    print(character)

print()

print("To get the length of a string, use the len() function.")

print(len(string))

print()

print("To check if a certain phrase or character is present in a string, we can use the keyword in.")

print("a" in string)

print()

print("Check if something is NOT in a string with not in")

print("d" not in string)

print()

print("You can return a range of characters by using the slice syntax.")
print("Specify the start index and the end index, separated by a colon, to return a part of the string.")

print(string[2:4])

print("By leaving out the start index, the range will start at the first character")
print(string[:2])

print("By leaving out the end index, the range will go to the end:")
print(string[2:])

print()

print("The upper() method returns the string in upper case")
print(string.upper())
print("The lower() method returns the string in lower case")
print(string.lower())
print("The strip() method removes any whitespace from the beginning or the end.")
a = " Hello, World! "
print(a.strip())
print("The replace() method replaces a string with another string.")
print(a.replace("H", "J"))
print("The split() method splits the string into substrings if it finds instances of the separator")
a = "test,this,comma,thing"
print(a.split(',', maxsplit=1))
print()
print("To concatenate, or combine, two strings you can use the + operator.")
name = "Rezana"
surname = "Dowra"
print(name + " " + surname)
print("To format we can use the f-string method f\'{}\' to replace variables")
print(f"My name is {name}")
print("You can also use {} in the string and use the format(variable_name,..) method")
print("My name is {}. My surname is {}".format(name, surname))

print()
print("------------------------------------------------------------------------------------------------------------")
print()

print("BOOLEANS")
print("When you compare two values, the expression is evaluated and Python returns the Boolean answer.")

value_x = 9
value_y = 20

if value_x > value_y:
    print("It's not my birthday")
else:
    print("It's my birthday!")

print()
print("Almost any value is evaluated to True if it has some sort of content. \n "
      "Any string is True, except empty strings.\n  Any number is True, except 0. \n"
      "Any list, tuple, set, and dictionary are True, except empty ones.")
print()
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print()
print(bool(""))
print(bool())
print(bool([]))


print()
print("------------------------------------------------------------------------------------------------------------")
print()


print("OPERATORS")
print("https://www.w3schools.com/python/python_operators.asp")