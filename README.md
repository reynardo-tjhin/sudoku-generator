# Sudoku Random Generator
Creating a random 9x9 sudoku

Programs are purely created using Python Language.

1. First Version:  Using a bruteforce with exceptions approach
2. Second Version: Using Yate's Random Algorithm

Files:
- `test_sudoku_one.sh`: This file is used to calculate the time for the first sudoku generator "sudoku_generator.py" to generate one sudoku. It is run by writing "./test_sudoku_one.sh". The file will generate average time taken, total time taken, shortest time and longest time, and also the number of sudokus that are failed to be generated.
- `test_sudoku_two.sh`: Similar to `test_sudoku_one.sh`
- `sudoku_generator.py`: 1st version of the random sudoku generator
- `sudoku_generator_2.py`: 2nd version of the random sudoku generator
- `check_sudoku.py`: This file is to check the correctness of the random sudoku
- `get_difficulty.py`: This file generates an incomplete sudoku based on the difficulty level desired

First Version: Bruteforce

Second Version: Modified Fisher-Yates' Algorithm
- The algorithm is used to randomize the numbers within an array.
- The pseudo-code:
Algorithm is taken from University of Sydney Year 2021 Semester 1 COMP2123: Data Structure and Algorithms course Lecture 12: Randomization.
```
def FisherYates(A):
    # permute A in place
    n = length of array A

    for i in {0, 1, ..., n - 1} do
        # swap A[i] with random position
        j = random number in {i, ..., n - 1}
        A[i], A[j] = A[j], A[i]
    
    return A
```

- The second version of sudoku generator follows similarly to Fisher-Yates' Algorithm.
Firstly, we prepare a complete and randomized sudoku. <br />
We then iterate every position in the sudoku from the very first row to last row. The order in each row is from the first column to the last column. <br />
For every iteration, we choose which way to pick the number: within the 3x3 box, horizontal or vertical. <br />
We then pick a number from the (current index + 1) to the final number depending on the way we picked previously. <br />
For example, we have a snippet of a sudoku: <br />
1 3 4 | 2 5 6 | 7 9 8 <br />
5 8 7 | 9 1 3 | 2 4 6 <br />
2 6 9 | 4 7 8 | 1 3 5 <br />
Let's assume we are currently at (1, 4) where 1 refers to row, 4 refers to column. <br />
If we pick within the 3x3 box, <br />
we are looking at: <br />
2 5 6 <br />
9 1 3 <br />
4 7 8 <br />
Hence, since we are at (1, 4), this means we will swap 2 and a random number within the box. <br />
If we pick horizontally, <br />
we are looking at: <br />
1 3 4 | 2 5 6 | 7 9 8 <br />
Hence, we will swap 2 and a random number after 2. <br />
*The reason why we do not swap with numbers before 2 is because the previous numbers are already randomized, hence, there might be a possibility that we will swap the same number again and retain the same sudoku. <br />
If we pick vertically, <br />
we are looking at: <br />
2 <br />
9 <br />
4 <br />
... <br />
Hence, we will swap 2 and a random number below 2. <br />
After we pick 2 numbers, we will go through the entire sudoku and swap all the numbers. <br />
- The correctness of this algorithm

