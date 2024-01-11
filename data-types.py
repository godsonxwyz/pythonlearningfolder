# Data Types

# There are different data types e.g strings which are letters(alphabets) and they look like this "Hello World"

# Integers which are numbers without no decimal places e.g. 342 13383

# Float are number with decimal places, it's also called floating point numbers e.g.  341.32

# Subscript [] fucntion can be used to print a position of a particular letter in a string... []

# print("Hello"[4])

# Note, counting starts from 0 in programming cos we're dealing with bytes

# Boolean, this is simply to confirm if a data is True or False and always start with cap
# True
# False

# Type() function gives information about the data type, maybe it's an integer, float or whatever
# str() converts whatever data to strings
# Float() converts data type to float
# int () can be used to convert data too

# name_char = len(input("What's your name?\n"))

# new_name_char = str(name_char)

# print("The number of letters in your name is " + new_name_char+"!")

# To add or convert integer to strings so it can be added to the output data, we can use the str() function and place our 
# string together with integer by doing type conversion

# a = 235.98
# print(type(a))

two_digits_number = input()

first_digit = int(two_digits_number[0])
second_digit = int(two_digits_number[1])

print(first_digit + second_digit)