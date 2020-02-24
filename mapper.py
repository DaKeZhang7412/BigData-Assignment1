import sys
import StringIO
import os
import csv

def mapper(data_directory):
    # Data location
    # dataDirectory = 'testData'
    # dataDirectory = 'data'

    for subdir, dirs, files in os.walk(data_directory):

        for fileName in files:
            filePath = subdir + os.sep + fileName

            if "FlumeData." in filePath:

                file = open(filePath, 'r')
                # counting lines from file
                for line in file:
                    #break line into words
                    words = line.split(',')
                    id_str = ""
                    full_text = ""
                    for word in words: # Iterate the words in line
                        # extract user id number and Full text
                        if word.startswith('"id_str":') and id_str == "" : # find user id in the line
                            id_str = word[10:-1]
                        if word.startswith('"full_text":') and full_text == "": # find user tweet
                            full_text = word[13:-1]
                        # save id and tweet into output csv file
                        if id_str != "" and full_text != "":
                            with open('tweet.csv', 'a') as outputFile:
                                csv_writer  = csv.writer(outputFile, delimiter=',')
                                appendText = [id_str, full_text, "Trump"]
                                csv_writer.writerow(appendText)

                            break # jump out of loop

                # Closing current file
                file.close()

# This function allows you to test the mapper with the provided test file
def main():
    sys.stdin = StringIO.StringIO(data_directory)
    # Input data direct
    # data_directory = "data"
    #sys.stdin = StringIO.StringIO(data_directory)
    print("please be patient, it will take a while to calculate!")
    mapper(data_directory)
    print("Done!")

if __name__ == "__main__":
    main()
