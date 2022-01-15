import sudoku_generator as sg
import sudoku_generator_2 as sg2
import sys

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

if (__name__ == "__main__"):

    try:
        version = sys.argv[1]
        if (version == "1"):
            print(check_sud(sg.get_sudoku()))

        elif (version == "2"):
            print(check_sud(sg2.get_sudoku()))
    
    except:
        print("python3 check_sudoku.py [1/2]\n[1/2] refers to the version.")