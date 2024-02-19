'''
Author: Rahul Bhattachan
KUID: 3050953
Date: 9/5/2022
Lab: lab 1
Last modified: 9/5/22
Purpose: The purpose of the boardgame class is to create the variables that  
the Executive class will use.
It also creates the format that we will be using/displaying for the user.
           
'''

class Boardgame():
    #defines the objects parameters
    def __init__(self, name, G_rating, P_rating, year, min_players, playtime):
        self.name = name
        self.year = year
        self.G_rating = G_rating
        self.P_rating = P_rating
        self.min_players = min_players
        self.playtime = playtime
   # returns the year
    def get_year(self):
        return(self.year)
   # sets the year
    def set_year(self, yearNum):
        self.year = yearNum
   # prints out the class in question
    def __str__(self):
        return(f"{self.name} ({self.year}) [GR={self.G_rating}, PR={self.P_rating}, MP={self.min_players},MT={self.playtime}]")
