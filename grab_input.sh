#!/bin/bash

DAY=$1

PADDED_DAY=$(printf "%02d" $DAY)

response=$(curl https://adventofcode.com/2021/day/$DAY/input --cookie "session=$AOC_SESSION")

echo $response

echo -n "main_input=\"\"\"$response\"\"\"" > inputs/input_$PADDED_DAY.py
