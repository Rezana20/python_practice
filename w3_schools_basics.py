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

print("stopped at https://www.w3schools.com/python/python_datatypes.asp")