#!/bin/bash

export TIMEFORMAT=%R # to output the real time

# variables
NO_OF_TESTS=2
NO_OF_ERRORS=0
TOTAL_TIME=0
TIME_TAKEN=0
LONGEST=0
SHORTEST=0

touch temp.err # to get error
i=0
while [ $i -lt $NO_OF_TESTS ]
do
    # get the time taken to produce 1 random sudoku
    TIME_TAKEN=$(time(python3 sudoku_generator.py 2> temp.err) 2> /dev/stdout)
    printf "$(($i+1)): $TIME_TAKEN s\n"

    # check for errors
    if [ ! -z "$(cat temp.err)" ] # check if not empty
    then
        echo "Error at No. $(($i+1)) test!"
        NO_OF_ERRORS=$(($NO_OF_ERRORS+1))
        
        # clean the temporary text file
        rm temp.err
        touch temp.err
    fi
    i=$(($i+1))

    # add to total time
    TOTAL_TIME=$(echo "scale=5; $TIME_TAKEN + $TOTAL_TIME" | bc)

    # compare longest
    # compare shortest

done
rm temp.err # remove the temporary file

echo "No of Errors: $NO_OF_ERRORS out of $NO_OF_TESTS tests"
echo "Total Time Taken: $TOTAL_TIME s"
