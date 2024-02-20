'''
Rahul Bhattachan
KU ID: 3050953
Date: 9/28/22
Lab 4
Purpose: This program keeps track of the numbers in the Fibonacci sequence
with the 2 starting numbers being 0 and 1. Then, based on what the
user chooses, it will use recursion to either print the ith Fibonacci
number at the user's number or will verify if a number is or is not
in the sequence.
'''


# Main (function)
# The purpose of main is to get a valid input from the user.
# It also checks what calculation the user wants to do.

def main():
    passed = False
    
    while not passed:
        try:
            mode, value = input("\nEnter mode and value: ").split() 
            value = int(value)
            if value > 0:
                passed = True
            else:
                print("Invalid input")
        except:
            print("Invalid input")
        

    if str(mode) == "-i":
        print(fibonacci(value))

    elif str(mode) == "-v":
        index = 0
        found = True
        
        while found:
            if (fibonacci(index) == value):
                print(f"{value} is in the sequence\n")
                found = False
            elif (fibonacci(index) > value):
                print(f"{value} is not in the sequence\n")
                found = False
            index += 1


# Recurssion function
# Recurses to find the "ith" fibonacci number.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


main()
