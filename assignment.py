def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:
# 3, 4 is printed. 
# When the number is 1, the condition becomes false, so nothing happens
# When the number is 2, since its greater than 1, it passes 2 to add_one, which calculate 2+1 and returns 3
# When the number is 3, since its greater than 1, it passes 3 to add_one, which calculate 3+1 and returns 4


# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
# add_one(2) returns the value 3.
# return passes a value back to the program from inside a function. It allows the program to store, calculate, or use that result elsewhere
# print displays the text for user to see
