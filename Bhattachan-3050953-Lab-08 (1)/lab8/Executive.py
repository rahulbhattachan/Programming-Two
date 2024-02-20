'''
Rahul Bhattachan
KU ID: 3050953
Purpose: Contains the main chunk of code that will be called by the driver.
Lab #8
Last Modified:11/07/22
'''
 
from BSTNode import BSTNode
from Data import Data
 
def copy(root):#returns copy of root
    if root is None:
        return None
    rootCopy = BSTNode(root.val, root.data)
    rootCopy.left = copy(root.left)
    rootCopy.right = copy(root.right)
    return rootCopy
 
 
def select():#presents option to user whether they want to pick og pokedex or the copy
    print("Which pokedex would you like to search from?")
    print("1) Original")
    print("2) Copy")
    return int(input("Choose 1 or 2: "))
   
class Executive:
 
    def main():# Opens text file and presents input options to user
       
        pokedex = open("pokedex.txt", "r")
 
        BST = BSTNode()
 
        for line in pokedex:
            value1, key, value2 = line.split()
            myData = Data(int(key), value1, value2)
            BST.insert(myData.index, myData)
 
        copied = False
       
        while True:
            print("\nWhat would you like to do?")
            print("1) Search from Pokedex")
            print("2) Add new entry")
            print("3) Print Pokedex")
            print("4) Copy Pokedex")
            print("5) Remove entry")
            print("6) Quit")
 
            choice = int(input("\nSelect a number: "))
            print()
 
           
            if choice == 1:
                if copied:
                    pokedexChoice = select()
                    if pokedexChoice == 1:
                        userID = int(input("Enter the id to search for a pokemon: "))
                        print()
                        print(BST.exists(userID))
                    elif pokedexChoice == 2:
                        userID = int(input("Enter the id to search for a pokemon: "))
                        print()
                        print(COPY.exists(userID))
                else:
                    userID = int(input("Enter the id to search for a pokemon: "))
                    print()
                    print(BST.exists(userID))
                       
 
            elif choice == 2:
                print("Add a new Pokemon!")
                if copied:
                    pokedexChoice = select()
                    englishName = str(input("Enter an english name: "))
                    japanName = str(input("Enter a Japanese name: "))
                    pokedexNum = int(input("Enter pokedex number: "))
                    myData1 = Data(int(pokedexNum), englishName, japanName)
                    if pokedexChoice == 1:
                        if BST.doExists(pokedexNum) == False:
                            BST.insert(myData1.index, myData1)
                            print("New entry inserted sucessfully in original.")
                        else:
                            print("Entry already exists.")
                    elif pokedexChoice == 2:
                        if COPY.doExists(pokedexNum) == False:
                            COPY.insert(myData1.index, myData1)
                            print("New entry inserted sucessfully in copy.")
                        else:
                            print("Entry already exists.")
                else:
                    englishName = str(input("Enter an english name: "))
                    japanName = str(input("Enter a Japanese name: "))
                    pokedexNum = int(input("Enter pokedex number: "))
                    myData1 = Data(int(pokedexNum), englishName, japanName)
                    if BST.doExists(pokedexNum) == False:
                        BST.insert(myData1.index, myData1)
                        print("New entry inserted sucessfully in original.")
                    else:
                        print("Entry already exists.")                
 
 
            elif choice == 3:
                print("Make another selection")
                print("1) Pre order")
                print("2) In order")
                print("3) Post order")
                choice = int(input("Choose a traversal order: "))
 
                if choice == 1:
                    print("\nPre order:")
                    if copied:
                        pokedexChoice = select()
                        if pokedexChoice == 1:
                            for line in BST.preorder([]):
                                print(line)
                        elif pokedexChoice == 2:
                            for line in COPY.preorder([]):
                                print(line)
                    else:
                        for line in BST.preorder([]):
                            print(line)
 
                elif choice == 2:
                    print("\nIn order:")
                    if copied:
                        pokedexChoice = select()
                        if pokedexChoice == 1:
                            for line in BST.inorder([]):
                                print(line)
                        elif pokedexChoice == 2:
                            for line in COPY.inorder([]):
                                print(line)
                    else:
                        for line in BST.inorder([]):
                            print(line)
 
                elif choice == 3:
                    print("\nPost order:")
                    if copied:
                        pokedexChoice = select()
                        if pokedexChoice == 1:
                            for line in BST.postorder([]):
                                print(line)
                        elif pokedexChoice == 2:
                            for line in COPY.postorder([]):
                                print(line)
                    else:
                        for line in BST.postorder([]):
                            print(line)
 
 
            elif choice == 4:
                if copied:
                    print("Copy already exists.")
                else:
                    COPY = copy(BST)
                    copied = True
                    print("BST copied!")
 
 
            elif choice == 5:
                print("Delete a Pokemon!")
                if copied:
                    pokedexChoice = select()
                    if pokedexChoice == 1:
                        pokedexNum = int(input("Enter pokedex number: "))
                        if BST.doExists(pokedexNum) == False:
                            print("Entry not found.")
                        else:
                            BST.delete(pokedexNum)
                            print("\nPokemon at index: " + str(pokedexNum) + " deleted sucessfully from original!")
                    elif pokedexChoice == 2:
                        pokedexNum = int(input("Enter pokedex number: "))
                        if COPY.doExists(pokedexNum) == False:
                            print("Entry not found.")
                        else:
                            COPY.delete(pokedexNum)
                            print("\nPokemon at index: " + str(pokedexNum) + " deleted sucessfully from copy!")
                else:
                    pokedexNum = int(input("Enter pokedex number: "))
                    if BST.doExists(pokedexNum) == False:
                        print("Entry not found.")
                    else:
                        BST.delete(pokedexNum)
                        print("\nPokemon at index: " + str(pokedexNum) + " deleted sucessfully from original!")
                   
                   
            elif choice == 6:
                print("Exiting...")
                break
 
 
            else:
                print("Please enter a number from 1 to 6.")
 
        pokedex.close()

