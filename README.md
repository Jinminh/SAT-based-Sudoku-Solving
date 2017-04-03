
## Folder structure
-Project.zip
	|
	./README.txt: this file
	./sudokuNxN.py: encoder/decoder program
	./ourProgram.pl: Sudoku Solver in Prolog
	./Report.txt: the report file

## Usage
	./sudokuNxN.py <N> <verticalBlockSize> <horizontalBlockSize>
As an example, for 16x16 puzzle with block size 4x4:
	./sudokuNxN.py 16 4 4

## Note:
	This program needs minisat installed.
	It will call minisat automatically. 
	If the call failed, please use the inputFile.txt as the input of the minisat solver. 
	After the output from minisat is generated, please rename the output file to outputFile.txt, put it with the program 	and try again.


## Sample Problem For Testing:

### 9 x 9 Problem:
```
1,6,3,8,_,5,_,7,_
_,_,8,_,4,_,_,6,5
_,_,5,_,_,7,_,_,8
4,5,_,_,8,2,_,3,9
3,_,1,_,_,_,_,4,_
7,_,_,_,_,_,_,_,_
8,3,9,_,5,_,_,_,_
6,_,4,2,_,_,5,9,_
_,_,_,_,9,3,_,8,1
```

### 16x16 Problem:
```
_,6,_,_,_,_,_,8,11,_,_,15,14,_,_,16
15,11,_,_,_,16,14,_,_,_,12,_,_,6,_,_
13,_,9,12,_,_,_,_,3,16,14,_,15,11,10,_
2,_,16,_,11,_,15,10,1,_,_,_,_,_,_,_
_,15,11,10,_,_,16,2,13,8,9,12,_,_,_,_
12,13,_,_,4,1,5,6,2,3,_,_,_,_,11,10
5,_,6,1,12,_,9,_,15,11,10,7,16,_,_,3
_,2,_,_,_,10,_,11,6,_,5,_,_,13,_,9
10,7,15,11,16,_,_,_,12,13,_,_,_,_,_,6
9,_,_,_,_,_,1,_,_,2,_,16,10,_,_,11
1,_,4,6,9,13,_,_,7,_,11,_,3,16,_,_
16,14,_,_,7,_,10,15,4,6,1,_,_,_,13,8
11,10,_,15,_,_,_,16,9,12,13,_,_,1,5,4
_,_,12,_,1,4,6,_,16,_,_,_,11,10,_,_
_,_,5,_,8,12,13,_,10,_,_,11,2,_,_,14
3,16,_,_,10,_,_,7,_,_,_,6,_,_,_,12
```
