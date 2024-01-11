age = input("What is your current age?\n")


current_age = 90 - int(age)

days = 365 * current_age
weeks = 52 * current_age
months = 12 * current_age

print(f"You have {days} days, {weeks} weeks, {months} months left.")