from random import randint
from math import floor
from time import time

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
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
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

def check_sud(sudoku):
    """
    Check whether the sudoku is correct

    :param sudoku: a list of list of 9 different integers
    :return true if it is a correct sudoku otherwise false
    """
    # check horizontal
    for i in range(0, 9):
        check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(0, 9):
            if (check[ int(sudoku[i][j]) - 1 ] == 1):
                return False
            check[ int(sudoku[i][j])- 1 ] = 1
    
    # check vertical
    for i in range(0, 9):
        check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(0, 9):
            if (check[ int(sudoku[j][i]) - 1] == 1):
                return False
            check[ int(sudoku[j][i]) - 1 ] = 1
    
    # check box
    i = 0
    while i < 9:
        
        check = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if (i >= 0 and i <= 2):
            j = 0
        elif (i >= 3 and i <= 5):
            j = 3
        else:
            j = 6
        for l in range(0, 3):

            if (i % 3 == 0):
                k = 0
            elif (i % 3 == 1):
                k = 3
            else:
                k = 6
            for m in range(0, 3):

                if (check[ int(sudoku[j][k]) - 1] == 1):
                    return False
                check[ int(sudoku[j][k]) - 1 ] = 1
                k += 1

            j += 1

        i += 1

    return True

def df(string):
    """
    Returns the correct sudoku as well as an incomplete sudoku with the number of empty numbers
    depends on the string given

    :param string: string to determine the level of difficulty ("e"/"m"/"h")
    """
    sudoku = get_sudoku()
    incomplete_sudoku = []
    for i in range(0, 9):
        incomplete_sudoku.append([])
        for j in range(0, 9):
            incomplete_sudoku[i].append(sudoku[i][j])

    number_of_empty = 0
    if (string.__eq__("e")):
        number_of_empty = randint(36, 42)
    elif (string.__eq__("m")):
        number_of_empty = randint(42, 59)
    else: # "h"
        number_of_empty = randint(59, 63)

    for i in range(0, number_of_empty):

        is_not_empty = True
        while (is_not_empty):
            j = randint(0, 8)
            k = randint(0, 8)
            if ( str(incomplete_sudoku[j][k]) != "" ):
                incomplete_sudoku[j][k] = ""
                is_not_empty = False

    return (incomplete_sudoku, sudoku)

# Testing and timing
if (__name__ == "__main__"):

    # past_time1 = time()
    # i = 0
    # while i < 100:
    #     past_time = time()
    #     get_sudoku() 
    #     current_time = time()
    #     print("{}. Time: {:.5f}s".format(i + 1, current_time - past_time))
    #     i += 1
    
    # current_time1 = time()
    # print("Total time taken: {:.5f}s".format(current_time1 - past_time1))

    print()
    past_time = time()
    test = get_sudoku()
    current_time = time()
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

    print(string)
    print("Time: {:.5f}s".format(current_time - past_time))
    print("Check: " + str(check_sud(test)))
    print("Success!")



"""
!!!FAILED METHODS!!!
def find_horizontal(sudoku, i, number):
    'Find the number and return the coordinates in the list'

    j_temp = 0
    while j_temp < 9:
        if (sudoku[i][j_temp] == number):
            return (i, j_temp)
        j_temp += 1

def find_vertical(sudoku, j, number):
    'Find the number and return the coordinates in the list'

    i_temp = 0
    while i_temp < 9:
        if (sudoku[i_temp][j] == number):
            return (i_temp, j)
        i_temp += 1

def find_box(sudoku, i, j, number):

    x = i % 3
    y = j % 3
    i_temp = i - x
    maxi = i_temp + 3
    while (i_temp < (maxi)):

        j_temp = j - y
        maxj = j_temp + 3
        
        # print(str(i_temp) + " " + str(j_temp))
        string = ""
        while (j_temp < (maxj)):

            string = "i_temp: " + str(i_temp) + " " + "j_temp: " + str(j_temp)
            print(string)

            if (sudoku[i_temp][j_temp] == number):
                return (i_temp, j_temp)

            j_temp += 1

        i_temp += 1

def sudoku_sample():

    intial_sudoku = [

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]

    ]
    return intial_sudoku
"""