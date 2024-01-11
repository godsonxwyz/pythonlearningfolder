#V Variables can be used for many things, especially to receive and store info from a prompt. 
#Here, I used a variable, assigned to save info from a prompt and print a welcome message of a customer signing on a webpage or whatever
#Or see it as a tool to collect data through prompts and save 


Customer_Name = input("What's your name? ")
print("Welcome, " + Customer_Name + "!")


# There are two variables, a and b from input (solution is to use a third variable for switching, a = gin b = ger c = third variable to store info)
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

c = a 
a = b
b = c


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

