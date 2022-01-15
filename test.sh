#!/bin/bash

export TIMEFORMAT=%R

NEGATIVE_NO=0.438
echo "$NEGATIVE_NO > 0.613" | bc
if [ 1 -eq $(echo "$NEGATIVE_NO > 0.613" | bc) ]
then
    echo "-1 is greater than -8"
fi

touch temp.err
touch temp.txt

time(python3 test.py 2> temp.err) 2>> temp.txt

TIME=$(time(python3 test.py 2> temp.err) 2>/dev/stdout)
printf "$(echo $TIME)s\n"

if [ ! -z "$(cat temp.err)" ]
then
    echo "There is an error"
fi

rm temp.err

printf "FASTEST: $(sort temp.txt | head -n 1)s\n"
printf "SLOWEST: $(sort temp.txt | tail -n 1)s\n"

# Find Average
TOTAL=0
COUNT=0
for i in $(cat temp.txt)
do
    TOTAL=$(echo "$i + $TOTAL" | bc)
    COUNT=$(($COUNT+1))
done
printf "TOTAL: $(echo $TOTAL)s\n"
printf "COUNT: $(echo $COUNT)\n"
printf "AVERAGE: $(echo "scale=5; $TOTAL / $COUNT" | bc | awk '{printf "%f", $0}')s\n"

rm temp.txt