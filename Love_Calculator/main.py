

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n") # What is your name?
name2 = input("What is their name?\n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_name = name1 + name2
lower_case_name = combined_name.lower()

T = lower_case_name.count("t")
R = lower_case_name.count("r")
U = lower_case_name.count("u")
E = lower_case_name.count("e")

true = T + R + U + E

l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")

LOVE = l + o + v + e

love_score = int(str(true) + str(LOVE))

if love_score <= 10 or love_score >= 90:
    print(f"Your score is {love_score}, you go together like coke and fanta!")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


