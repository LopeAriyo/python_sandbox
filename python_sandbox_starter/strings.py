# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Yemoja"
age = 2

# String Formatting
print("Hello, my name is {name} and I am {age} years old".format(
    name=name, age=age))


name2 = input("What's your name?: ")
age2 = input("Hello {name}, How old are you? ".format(name=name2))

# F-Strings
print(f"Wow {name2}! You look so young for {age2}")

# String Methods

greeting = "Hello, World!"


print(greeting.capitalize())  # Capitalize, only the first letter
print(greeting.upper())
print(greeting.lower())
print(greeting.swapcase())
print(len(greeting))
# case sensitive, does not modify greeting
print(greeting.replace("World", "Lope"))
print(greeting.count("o"))
print(greeting.startswith("Hi"))
print(greeting.endswith("World!"))
print(greeting.split(" "))


# References: https://www.w3schools.com/python/python_ref_string.asp
