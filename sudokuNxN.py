#!/usr/bin/python
import itertools
import os
import sys

class element:
	def __init__(self, row, column, digit, index, value):
		self.row = row
		self.col = column
		self.digit = digit
		self.index = index
		self.value = value

#getInput
def getInput(numberN):
	tempList = []
	strList = []
	for x in xrange(1,numberN):
		strList.append(str(x))

	for i in range(1,numberN):
		inputString = raw_input()
		j = 1
		for item in inputString.split(','):
			if(item in strList):
				tempObject = element(i, j, int(item), -1, True)
				tempList.append(tempObject)
				j += 1
			elif(item == '_'):
				tempObject = element(i, j, 0, -1, False)
				tempList.append(tempObject)
				j += 1
			elif(item == ''):
				pass
			else:
				print('\nPlease input valid element!')
				return None
	return tempList

def getBlockElement(startRow, startCol, elementList, vBlockSize, hBlockSize):
	tempList = []
	for i in xrange(startRow,startRow + vBlockSize):
		for j in xrange(startCol,startCol + hBlockSize):
			for item in elementList:
				if item.row == i and item.col == j:
					tempList.append(item)
	return tempList

def initialization(numberN, vBlockSize, hBlockSize):
	elementList = []
	count = 1

	for i in xrange(1,numberN): 
		for j in xrange(1,numberN): 
			for k in xrange(1,numberN): 
				elementList.append(element(i, j, k, count, False))
				count += 1

	rowElementList = []
	for row in xrange(1,numberN):
		tempList = []
		for item in elementList:
			if (item.row == row):
				tempList.append(item)
		rowElementList.append(tempList)

	columnElementList = []
	for column in xrange(1,numberN):
		tempList = []
		for item in elementList:
			if (item.col == column):
				tempList.append(item)
		columnElementList.append(tempList)

	blockElementList = []

	for x in xrange(1, numberN, vBlockSize): 
		tempRow = []
		for y in xrange(1, numberN, hBlockSize):
			tempRow.append(getBlockElement(x, y, elementList, vBlockSize, hBlockSize))
		blockElementList.append(tempRow)

	blockElementList.append(tempRow)

	return elementList, rowElementList, columnElementList, blockElementList


def generateExactlyOnceClause(inputList):
	stringList = []
	tempString = ''
	for item in inputList:
		tempString += str(item.index)
		tempString += ' '
	tempString += '0'
	stringList.append(tempString)

	for item in itertools.combinations(inputList, 2):
		tempString = '-%d -%d 0' % (item[0].index, item[1].index)
		stringList.append(tempString)

	return stringList


#main
if __name__ == '__main__':

	try:
		numberN = int(sys.argv[1]) + 1
		vBlockSize = int(sys.argv[2])
		hBlockSize = int(sys.argv[3])
		print("\nParameters provided, using specified setting:\n Number: %dx%d\n Vertical Block Size: %d\n HorizontalBlockSize: %d" % (numberN - 1, numberN - 1, vBlockSize, hBlockSize))
	except:
		print("usage: %s <number N> <vertical block size> <horizontal block size>" % sys.argv[0])
		print('	e.g. for an 16x16 puzzle with block size 4x4, type %s 16 4 4' % sys.argv[0])
		print("\nNo parameters provided, using default setting:\n Number: 9x9\n Vertical Block Size: 3\n HorizontalBlockSize: 3")
		numberN = 10
		vBlockSize = 3
		hBlockSize = 3

	elementList, rowElementList, columnElementList, blockElementList = initialization(numberN, vBlockSize, hBlockSize)

	outputBuffer = []

	# exactly one digit appears in each cell
	i = 0
	while i < len(elementList):
		tempList = []
		for n in xrange(1,numberN):
			tempList.append(elementList[i])
			i += 1
		outputBuffer += generateExactlyOnceClause(tempList)

	# each digit appears exactly once in each row
	for d in xrange(1,numberN):
		for row in rowElementList:
			tempList = []
			for item in row:
				if item.digit == d:
					tempList.append(item)
			outputBuffer += generateExactlyOnceClause(tempList)

	# each digit appears exactly once in each column
	for d in xrange(1,numberN):
		for col in columnElementList:
			tempList = []
			for item in col:
				if item.digit == d:
					tempList.append(item)
			outputBuffer += generateExactlyOnceClause(tempList)

	# each digit appears exactly once in each block
	for d in xrange(1,numberN):
		for blockRows in blockElementList:
			for block in blockRows:
				tempList = []
				for item in block:
					if item.digit == d:
						tempList.append(item)
				outputBuffer += generateExactlyOnceClause(tempList)

	print("\nPlease enter a Sudoku problem\nUse '_' to represent an unknown number, use ',' to separate each terms in a row: \n") 
	breakFlag = True
	inputElementList = []
	while (True):
		inputElementList = getInput(numberN)
		if(inputElementList != None):
			break
	
	# include prefilled numbers
	for item in inputElementList:
		if(item.digit == 0):
			continue
		targetObject = None
		for curr in rowElementList[item.row - 1]:
			if curr.row == item.row and curr.col == item.col and curr.digit == item.digit:
				targetObject = curr
				break
		tempString = '%d 0' % targetObject.index
		outputBuffer.append(tempString)

	fileHandle = open('inputFile.txt', 'w')
	fileHandle.write('p cnf %d %d\n' % (len(elementList), len(outputBuffer)))
	for line in outputBuffer:
		fileHandle.write(line + '\n')

	fileHandle.close()

	os.system('minisat inputFile.txt outputFile.txt')

	fileHandle = open('outputFile.txt', 'r')
	lines = fileHandle.readlines()
	fileHandle.close()

	if lines[0].startswith('SAT') != True :
		print('\nNo solution. Program exit...')
		exit()

	print('\nThe solution to the given sudoku problem is: \n')
	numberArray = lines[1].split(' ')
	count = 0
	for number in numberArray:
		if(int(number) == 0):
			break
		actualNumber = int(number)
		if(actualNumber < 0):
			continue
		else:
			print(elementList[actualNumber - 1].digit),
			count += 1
			if(count == (numberN - 1)):
				print('\n'),
				count = 0



	
