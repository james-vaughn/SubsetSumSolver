# Subset Sum Solver

This is a basic project that solves the subset sum problem 
in parallel for each line of an input file that contains:

1. The target sum
2. The input number list

### Usage

These parameters can be used when running the script:
* `-f` to set the input file location
* `-o` to set the output file location
* `-p` to set the size of the process pool

Example usage: `python main.py -f input.txt -o output.txt -p 4`

### Input file
Each line of the file is a subset sum problem. 
The format is 'target sum, number 1, number 2, ...'
The solver will produce a file that contains solutions to 
each problem should one exist. It will only produce the first
solution it finds.
