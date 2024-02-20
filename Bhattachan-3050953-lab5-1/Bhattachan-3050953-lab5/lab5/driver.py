'''
Author: Rahul Bhattahan
KUID: 3050953
Date: 10/17/22
Lab: lab 5
Purpose:Gives the amount of items eaten by blob depending input file
'''

itemsEaten = 0

def main():
    try:
        sewerLocations = {}
        global itemsEaten

        inputName = str(input("File Name: "))
        inputFile = open(inputName)
        outputFile = open("output.txt", "w")

        numRows, numCols = inputFile.readline().split()
        blobStartRow, blobStartCol = inputFile.readline().split()

        row = 0
        itemsEaten = 0
        for line in inputFile:
            letter = 0
            for char in line:
                if char == "@":
                    sewerLocations[row] = letter
                letter += 1
            outputFile.write(line)
            row += 1

        outputFile.close()

        isValidMove(int(blobStartRow), int(blobStartCol))
        run(int(numRows), int(numCols), int(blobStartRow), int(blobStartCol), sewerLocations)

        outputFile = open("output.txt", "a")
        outputFile.write("\nTotal Eaten: " + str(itemsEaten))
        outputFile.close()

        outputFile = open("output.txt")

        for line in outputFile:
            print(line.replace("\n", ""))
        outputFile.close()


        main() #Uses recursion to repeat the main
        
    except:
        raise RuntimeError
    


def sewerCount(sewerLocations, numRows, numCols): #If the blob hits a sewer, it finds every other sewer location
    for row, col in sewerLocations.items():
        run(numRows, numCols, row, col, sewerLocations, False)

def isValidMove(row, col): #Returns 1 if the blob can go on current row and column, returns 2 if there is a sewer there, returns False for anything else
    outputFile = open("output.txt")
    global itemsEaten

    char = outputFile.readlines()[row][col]
    outputFile.close()

    if char == "P":
        itemsEaten += 1
        return 1
    elif char == "S":
        return 1
    elif char == "@":
        return 2
    return False

def run(numRows, numCols, row, col, sewerLocations, markChar = True): #Marks the row and column and checks if the surrounding spots can be marked
    if markChar:
        mark(row, col)

    if col + 1 <= numCols - 1:
        if isValidMove(row, col +1 ) == 1:
            run(numRows, numCols, row, col + 1, sewerLocations)
        elif isValidMove(row, col +1 ) == 2:
            sewerCount(sewerLocations, numRows, numCols)
    if col - 1 >= 0:
        if isValidMove(row, col -1 ) == 1:
            run(numRows, numCols, row, col - 1, sewerLocations)
        elif isValidMove(row, col - 1) == 2:
            sewerCount(sewerLocations, numRows, numCols)
    if row + 1 <= numRows - 1:
        if isValidMove(row + 1, col) == 1:
            run(numRows, numCols, row+1, col, sewerLocations)
        elif isValidMove(row+1, col) == 2:
            sewerCount(sewerLocations, numRows, numCols)
    if row - 1 >= 0:
        if isValidMove(row - 1, col) == 1:
            run(numRows, numCols, row - 1, col, sewerLocations)
        elif isValidMove(row - 1, col) == 2:
            sewerCount(sewerLocations, numRows, numCols)
    
def mark(row, col): #Puts a B in the output file at the row and column
    outputFile = open("output.txt")

    newData = ""
    numRow = 0
    for line in outputFile:
        newLine = ""
        if (numRow == row):
            for char in range(len(line)):
                if char == col:
                    newLine += "B"
                else:
                    newLine += line[char]
        else:
            newLine = line
        newData += newLine
        numRow += 1

    outputFile.close()

    outputFile = open("output.txt", "w")
    outputFile.write(newData)
    outputFile.close()

main()
