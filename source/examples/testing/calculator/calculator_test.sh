#!/bin/bash

test1="2 + 3"
test2="2 - 3"

echo -n $test1 "= "
./calculator.py $test1
echo -n $test2 "= "
./calculator.py $test2
