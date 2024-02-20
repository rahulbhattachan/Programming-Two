from BSTNode import BSTNode
from Data import Data
'''
Rahul Bhattachan
KU ID: 3050953
Purpose: Contains the main chunk of code that will be called by the driver.
Lab #7
Last Modified:10/31/22
'''
class Executive:

    def main(): # Opens text file and presents input options to user
        
        pokedex = open("pokedex.txt", "r")
        BST = BSTNode()

        for line in pokedex:
            value1, key, value2 = line.split()
            Info = Data(int(key), value1, value2)
            BST.insert(Info.index, Info)
        
        while True:
            print("\nWhat would you like to do?")
            print("1) Search from Pokedex")
            print("2) Add new entry")
            print("3) Print Pokedex")
            print("4) Quit")

            choice = int(input("\nSelect a number: "))
            print()
            
            if choice == 1:
                ID = int(input("Enter the id to search for a pokemon: "))
                print()
                print(BST.exists(ID))

            elif choice == 2:
                print("Add a new Pokemon!")
                ENG = str(input("Enter an english name: "))
                JAP = str(input("Enter a Japanese name: "))
                NUM = int(input("Enter pokedex number: ")) 
                Info = Data(int(NUM), ENG, JAP)

                if BST.doExists(NUM) == False:
                    BST.insert(Info.index, Info)
                else:
                    print("Entry already exists.")

            elif choice == 3:
                print("Select a traversal order")
                print("1) Pre order")
                print("2) In order")
                print("3) Post order")
                choice = int(input("\nSelect a number: "))

                if choice == 1:
                    print("\nPre order:")
                    for line in BST.preorder([]):
                        print(line)

                elif choice == 2:
                    print("\nIn order:")
                    for line in BST.inorder([]):
                        print(line)

                elif choice == 3:
                    print("\nPost order:")
                    for line in BST.postorder([]):
                        print(line)
                
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Please enter a number from 1 to 4.")

        pokedex.close()

    main()


