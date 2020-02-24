import sys
import StringIO
import os

def rowCount():

	lineCount = 0
	fileCount = 0
	
	# Data location
	data_directory = ''
	sys.stdin = StringIO.StringIO(data_directory)

	for subdir, dirs, files in os.walk(data_directory):
		for fileName in files:
			filePath = subdir + os.sep + fileName	
			
			if "FlumeData." in filePath:
				# counting files from Directory
				fileCount += 1
				file = open(filePath, 'r')
				# counting lines from file
				for line in file:
					lineCount += 1
				
				# Closing files
				file.close() 
	
	print("Total Row Count for {} Directory is {}".format(data_directory, lineCount))
	print("Total File Count for {} Directory is {}".format(data_directory, fileCount))


# This function allows you to test the mapper with the provided test file
def main():
    rowCount()
    # sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
