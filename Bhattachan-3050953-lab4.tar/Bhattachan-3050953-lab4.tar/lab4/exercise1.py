'''
Rahul Bhattachan
KU ID: 3050953
Date: 9/28/22
Lab 4
Purpose: The program asks the user for a base and power then uses
recursion to find and print an answer of base ** power.
'''



# Main (function)
# The purpose of main is to get a valid input from the user.

def main():
    base = 0
    power = 0
    passed = False

    while passed == False:
        try:
            base = int(input("\nEnter a base: "))
            passed = True
        except:
            print("Base must be a number")

    passed = False

    while passed == False:
        try:
            power = int(input("Enter a power: " ))
            if power >= 0:
                passed = True
            else:
                print("Sorry, your exponent must be zero or larger.\n")
        except:
            print("Power must be a number\n")

    answer = calculate(base, power)
    print("Answer: " + str(answer))

# Calculate (function)
# If the power isn't one, the function keeps recursing by multiplying 
# the base by itself until it reaches the desired power.

def calculate(base, power):
    if power == 1:
        return base
    else:
        return base * calculate(base, power - 1)


main()
