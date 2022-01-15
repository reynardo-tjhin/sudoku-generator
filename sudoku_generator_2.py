from random import randint
from math import floor

def randomize() -> str:
    """
    Randomize the strings "horizontal", "vertical", "box" to indicate which number in the categories to find
    """
    type_to_randomize = [ "horizontal", "vertical", "box" ]
    n = randint(0, 2)
    return type_to_randomize[n]

def find_and_change(sudoku, no1, no2):
    """
    Search for the numbers, no1 and no2, to be swapped in the sudoku

    :param sudoku: a list of numbers
    :param no1: an integer that needs to be swapped
    :param no2: an integer that needs to be swapped 
    """
    i = 0
    while i < len(sudoku):

        j = 0
        while j < len(sudoku[i]):
            
            if (sudoku[i][j] == no1):
                sudoku[i][j] = no2
            elif (sudoku[i][j] == no2):
                sudoku[i][j] = no1

            j += 1
        
        i += 1

    return sudoku

# use random algorithm
def get_sudoku():
    """
    Generate a random sudoku using the idea of Fisher Yate's random algorithm
    """
    intial_sudoku = [
        [3, 7, 6, 4, 2, 8, 9, 1, 5],
        [1, 4, 5, 6, 9, 7, 2, 3, 8],
        [8, 9, 2, 1, 3, 5, 6, 4, 7],
        [2, 1, 7, 8, 4, 9, 5, 6, 3],
        [4, 3, 9, 2, 5, 6, 7, 8, 1],
        [6, 5, 8, 7, 1, 3, 4, 2, 9],
        [7, 8, 3, 9, 6, 4, 1, 5, 2],
        [5, 6, 1, 3, 7, 2, 8, 9, 4],
        [9, 2, 4, 5, 8, 1, 3, 7, 6]
    ]
    i = 0
    while i < 9:
        
        j = 0
        while j < 9:

            string = randomize()

            if (string.__eq__("horizontal")):
                # find a random coordinate along the horizontal axis
                x = i
                y = randint(j,8)
                
            elif (string.__eq__("vertical")):
                # find a random coordinate along the vertical axis
                x = randint(i,8)
                y = j

            else:
                # find a random coordinate within the box
                x = randint(i, 2 + floor(i / 3) * 3)
                y = randint(j, 2 + floor(j / 3) * 3)
            
            number = intial_sudoku[x][y]
            intial_sudoku = find_and_change(intial_sudoku, number, intial_sudoku[i][j])

            j += 1

        i += 1

    return intial_sudoku

if (__name__ == "__main__"):

    test = get_sudoku()
    string = ""
    i = 0
    while (i < 9):

        j = 0
        while (j < 9):

            if ( (j % 3 == 0) and (j != 0) ):
                string += "| "
            string += str(test[i][j]) + " "

            j += 1

        string += "\n"
        if ( ((i + 1) % 3 == 0) and (i != 8) ):
            string += "------+-------+-------\n"

        i += 1

    print()
    print(string)