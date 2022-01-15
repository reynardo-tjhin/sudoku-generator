#!/bin/bash

# to output the real time
export TIMEFORMAT=%R

# variables
NO_OF_TESTS=100
NO_OF_ERRORS=0
TOTAL_TIME=0
TIME_TAKEN=0
LONGEST=-10
SHORTEST=10

# to get error
touch temp.err

i=0
while [ $i -lt $NO_OF_TESTS ]
do
    # get the time taken to produce 1 random sudoku
    TIME_TAKEN=$(time(python3 sudoku_generator_2.py 2> temp.err 1> /dev/null) 2> /dev/stdout)
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
    if [ 1 -eq $(echo "$LONGEST < $TIME_TAKEN" | bc) ]
    then
        LONGEST=$TIME_TAKEN
    fi

    # compare shortest
    if [ 1 -eq $(echo "$SHORTEST > $TIME_TAKEN" | bc) ]
    then
        SHORTEST=$TIME_TAKEN
    fi
done

# remove the temporary file
rm temp.err

# output
echo "No of Errors:     $NO_OF_ERRORS out of $NO_OF_TESTS tests"
echo "Total Time Taken: $(echo $TOTAL_TIME)s"
echo "Longest Time:     $(echo $LONGEST)s"
echo "Shortest Time:    $(echo $SHORTEST)s"
echo "Average Time:     $(echo "scale=5; $TOTAL_TIME / $i" | bc | awk '{printf "%f", $0}')s"