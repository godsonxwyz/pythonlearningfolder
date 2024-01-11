print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))

percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

splitting_bill = int(input("How many people to split the bill? "))

# Solution

tip = percentage_tip / 100
percentage_tip_amount = tip * bill
tip_plus_bill = percentage_tip_amount + bill

Each_person = tip_plus_bill / splitting_bill

# "{:.2f}".format() this is the code to round off to two decimal places if the round(), 2 function isn't working
# It's rather a format error rather than a mathematical error!

rounded_each_person = "{:.2f}".format(Each_person)
print(f"Each person should pay: ${rounded_each_person}")
