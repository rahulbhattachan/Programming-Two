'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/5/2022
Lab: lab 1
Last modified: 9/5/22
Purpose: The purpose of the executive class is to print the menu and handle all the
user interactions. It uses the boardgame class to format and print out stuff depending on what the
on what the user chooses.
 
'''
 
from boardgame import Boardgame
 
class Executive():
    #Initializes the object's attributes.
    def __init__(self, file):
        self.file = file
    #Handles the function
    def run(self):
        #prints the menu when called
        def printMenu(): 
            print("\nBoardGame.py")
            print("1) Print all games")
            print("2) Print all games from a year")
            print("3) Print based on play time")
            print("4) The People VS Dr. Gibbons")
            print("5) Print based on rating")
            print("6) Exit the program\n")
 
        gameFile = open(self.file, "r")
        gameList = []
        for line in gameFile:
            line = line.strip()
            line = line.split()
            gameList.append(line)
        gameFile.close()
 
        while True:
            printMenu()
            userInput = int(input("Enter a number: "))
 
            if userInput == 1:
                tempList = []
                for game in gameList:
                    GR = game[1]
                    info = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                    tempList.append(f"{game[1]}^{info.__str__()}")
                tempList.sort(reverse=True)
 
                orderedList = []
                for stuff in tempList:
                    orderedList.append(stuff.split("^")[1])
               
                print("All games ranked from highest to lowest by Gibbons:\n")
                for stuff in orderedList:
                    print(stuff)
       
            if userInput == 2:
                userYear = input("Enter a year: ")
                print("All games from " + userYear + ":\n")
                found = False
                for game in gameList:
                    if userYear == game[3]:
                        found = True
                        game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                        print(game.__str__())
                if not found:
                    print("No games found.")
 
            if userInput == 3:
                userPlaytime = int(input("Enter a play time: "))
                print("All games with a play time less than or equal to " + str(userPlaytime) + ":\n")
                for game in gameList:
                    playtime = int(game[5])
                    if userPlaytime >= playtime:
                        game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                        print(game.__str__())
 
            if userInput == 4:
                userNum = float(input("Enter a number to compare the people's rating and Gibbon's rating: "))
                print("All games that have a difference in rating by " + str(userNum) + ":\n")
                for game in gameList:
                    ratingDifference = abs(float(game[1]) - float(game[2]))
                    if ratingDifference >= userNum:
                        game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                        print(game.__str__())
 
            if userInput == 5:
                userRating = float(input("Enter a rating: "))
                print("All games that have a rating of " + str(userRating) + " or higher:\n")
                for game in gameList:
                    GRating = float(game[1])
                    if GRating >= userRating:
                        game = Boardgame(game[0], game[1], game[2], game[3], game[4], game[5])
                        print(game.__str__())
               
            if userInput == 6:
                print("Exiting...")
                break




