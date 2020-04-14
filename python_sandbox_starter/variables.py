# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1  # * This is an integer
y = 2.6  # * This is a float
name = "Lope"  # * This is a string
is_savage = True  # * This is a boolean, booleans in python start with a capital letter

# Multiple Assignments

a, b, surname, is_wizard = (5, 6.5, "Ariyo", False)

print(type(a))
print(type(b))
print(type(surname))
print(type(is_wizard))


# Casting
print(x, type(x))
x = str(x)  # change a integer to a string
print(x, type(x))
print(y, type(y))
y = int(y)  # change a float to an integer
print(y, type(y))

z = float(y)
print(z, type(z))
