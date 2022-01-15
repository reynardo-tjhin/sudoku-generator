import sudoku_generator as sg
import sudoku_generator_2 as sg2
from random import randint

def df(string, version):
    """
    Returns the correct sudoku as well as an incomplete sudoku with the number of empty numbers
    depends on the string given

    :param string: string to determine the level of difficulty ("e"/"m"/"h")
    :param version: [1/2]
    """
    if (version == 1):
        sudoku = sg.get_sudoku()
    elif (version == 2):
        sudoku = sg2.get_sudoku()
    else:
        print("Error: Input the generator version!")
        return
    
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

if (__name__ == "__main__"):

    incomplete_sudoku, sudoku = df("e", 2)
    
    string = ""
    i = 0
    while (i < 9):

        j = 0
        while (j < 9):

            if ( (j % 3 == 0) and (j != 0) ):
                string += "| "
            if (str(incomplete_sudoku[i][j]) == ""):
                string += " "
            string += str(incomplete_sudoku[i][j]) + " "

            j += 1

        string += "\n"
        if ( ((i + 1) % 3 == 0) and (i != 8) ):
            string += "------+-------+-------\n"

        i += 1

    print()
    print(string)