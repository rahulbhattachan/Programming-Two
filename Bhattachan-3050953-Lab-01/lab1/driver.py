'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/5/2022
Lab: lab 1
Last modified: 9/5/22
Purpose: The purpose of the driver is to contain main() which
asks the user to input a file. Once the user inputs a file it then calls the
Executive class
 
'''
 
from executive import Executive
 
#Asks user for a file and if the file matches, and then gives control to Executive class
def main():
  file_name = input("Enter the name of the input file: ")
  my_exec = Executive(file_name)
  my_exec.run()
 
if __name__ == "__main__":
  main()

