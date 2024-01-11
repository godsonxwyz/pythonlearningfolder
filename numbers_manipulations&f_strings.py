

### What to note about symbols
# Addition + , Subtraction - , multiplication * , Division / (it'll always print result in float in python no matter what, so it doesn't matter), 
# exponent sign raise to the power of **, == equal to, != not equal to, > greater than, less < than, etc
#  // divides completely, round() can be used to round off a floating number into a whole number number, or we can precise how many places lke
#  round(0.2333333, 2) or another way to round off is by ":.2f".format()

# Calculation follows PEMDAS-LR (left to right) rule here  which is Parathensis, Exponential, Multiplication, Division, Addition, Subtraction 
#  numbers can be attached or added to previous code score, this is important for writing scores in games

score = 30
score += 3
score *= 100
score /= score
print(score)