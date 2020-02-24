import sys
import StringIO
import os

def mapper(test_data_directory):

	lineCount = 0
	fileCount = 0
	
	# Data location
	# dataDirectory = 'testData'
	# dataDirectory = 'data'

	for subdir, dirs, files in os.walk(input("Enter data directory: ")):

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
	
	print("Total Row Count for {} Directory is {}".format(dataDirectory, lineCount))
	print("Total File Count for {} Directory is {}".format(dataDirectory, fileCount))


# This function allows you to test the mapper with the provided test file
def main():
    # sys.stdin = StringIO.StringIO(test_data_directory)
    mapper(test_data_directory)
    # sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
