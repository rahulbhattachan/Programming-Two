'''
Rahul Bhattachan
KU ID: 3050953
Date: 9/28/22
Lab 4
Purpose: This program keeps track of the amount of people infected each
day with the flu by using recursion and prints how many are
infected on a certain day, based on what day the user chooses.
'''



# Main (function)
# The purpose of main is to get a valid input from the user.

def main():
    print("\nOUTBREAK!")
    
    passed = False
    while not passed:
        try:
            day = int(input("What day do you want a sick count for?: "))
            passed = True
        except:
            print("Invalid Day\n")

    if day > 0:
        current = count(day)
        print("Total people with the flu: " + str(current) + "\n")
    else:
        print("Invalid Day\n")


# Count (function)
# If there are three or more days, the function keeps recursing until it gets 
# the value of the past three days. Then it adds the past three days to get the
# value of the current day.

def count(day):
    current = 0

    if day == 1:
        current = 6

    elif day == 2:
        current = 20

    elif day == 3:
        current = 75

    elif day > 3:
        for i in range(3):
            current += count(day-(i+1))

    return current

main()
