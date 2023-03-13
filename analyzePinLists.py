'''
	Analyze all *.txt files and create a csv file and an md file for all arduino variants.
	The .txt files should have been created with the sketch created in createPinAnalyzer.py
'''

import os

######################################

allDict = dict()			# ardu-variant => (pin-name => pin-number)
allPinNames = set()
allVariantNames = []
allLinesArray = []			# denotes one line in the csv file (pin-name, (pin-number per arduino variant)+)

def analyzePinList(fName):
	'''
		Analyze one *.txt file with the according pin numbers into Dictionary allDict.
		Also collect allPinNames and allVariantNames
	'''
	variant = fName[17:-4]
	print(variant)
	newDict = dict()
	with open(fName, 'r') as inFile:
		allVariantNames.append(variant)
		while True:
			
			line = inFile.readline()
			if not line:
				break
			line = line.strip()
			#if line.find('----') >= 0:
			#	continue
			
			idx = line.find(':')
			if idx < 0:
				continue
			name = line[0:idx]
			value = line[idx+2:]
			while value.startswith("\t"):
				value = value[1:]
			print(name + ' => ' + value)
			newDict[name] = value
			allPinNames.add(name)
		allDict[variant] = newDict


def writeCsv(fName):
	'''
		Write the table in csv syntax
	'''
	string = '';
	for lineArr in allLinesArray:
		string += ','.join(lineArr) + "\n"
	with open(fName, 'w') as inFile:
		inFile.write(string)
		
	print(string)
	
	
def writeMd(fName):
	'''
		Write the table in markdown syntax
	'''
	string = ''
	# show the headline row:
	lineArr = allLinesArray[0]					
	string += '|' + '|'.join(lineArr) + "|\n"

	# show the | -- | ... row:
	string += '|'
	for _ in lineArr:
		string += ' -- |'
	string += "\n"

	# show the data rows:
	for ii in range(1, len(allLinesArray)):		
		lineArr = allLinesArray[ii]
		string += '|' + '|'.join(lineArr) + "|\n"

	with open(fName, 'w') as inFile:
		inFile.write(string)
		
	print(string)
	
	
def analyzePinLists():
	'''
		Iterate over all *.txt files in folder arduino-variants
		Build all lists and output csv and md file
	'''
	for fName in os.listdir('arduino-variants'):
		if fName.startswith('Pins-') and fName.endswith('.txt'):
			analyzePinList('arduino-variants/' + fName)
			
	allPinNamesList = list(allPinNames)
	allPinNamesList.sort()
	allVariantNames.sort()
	#print(allPinNamesList)
	headerLineArray = ['Pin']
	for variant in allVariantNames:
		headerLineArray.append(variant)

	#print(headerLine)
	allLinesArray.append(headerLineArray)
	for pinName in allPinNamesList:
		pinArray = [pinName]
		for variant in allVariantNames:
			variantDict = allDict[variant]
			if pinName in variantDict:
				pinArray.append(variantDict[pinName])
			else:
				pinArray.append('?')
		allLinesArray.append(pinArray)
		
	for row in allLinesArray:
		print(row)
		
	writeCsv('Arduino-PinNumbers.csv')
	writeMd('Arduino-PinNumbers.md')

		
##################################


analyzePinLists()
