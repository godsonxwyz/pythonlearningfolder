# import random
#
# ########### This exercise is to pracise what I've just learned about random, and pylist
# #
# # names = "Bola, Wale, Jamiu, Tife, Yemi"
# #
# # print(names.split(", ")) to split strings into list
# #
# # another = ["Wale", "Jamiu", 5, "Ibeju", 7, "Lekki"]
# # print(another[4])
#
# import random
#
# names = input("Please enter your names separated by a comma and a space.\n").split(", ")
#
# print(random.choice(names) + " will pay the bill")
#
#
#


yeah_list = ["Bola", "Jamiu", "Ismail", "Anabelle", "notAmerica"]

yeah_list.extend(["Patrick", "Kewe"])

print(yeah_list[-2])