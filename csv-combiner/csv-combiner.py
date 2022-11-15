#file: csv-combiner.py
#goal: take in several .csv files as arguments, output new combined file to stdout. new file will have additional column with filename of origin
#method: go through each .csv file in order of input

#imports
import sys
import os
import csv
#main function
def combine():
    outputWriter=csv.writer(sys.stdout)
    #program has to account for files potentially having different headers
    #loop through files' first lines and get headers
    headers=[]
    files = sys.argv[1:] #get list of files to combine
    for file in files:
        readFile=csv.reader(open(file, 'r'))
        line=readFile.__next__()
        for col in line:
            if col not in headers:
                headers.append(col)
    #end loop
    headers.append("file_name")
    #now add the headers to the file
    outputWriter.writerow(headers)
    #now we have the headers for the csv files, and need to loop through the files to add to output
    for file in files:
        readFile=csv.reader(open(file, 'r'))
        fileHeads=readFile.__next__() #get header line
        fileName = os.path.basename(file)
        for readLine in readFile:
            if len(fileHeads)==len(headers)-1:
                readLine.append(fileName)
                outputWriter.writerow(readLine)
            else:
                newLine=[]
                for x in range(len(headers)-1):
                    if headers[x] in fileHeads:
                        y=fileHeads.index(headers[x])
                        newLine.append(readLine[y])
                    else:
                        newLine.append('')
                newLine.append(fileName)
                outputWriter.writerow(newLine)
            #exit if condition and loop    
    #end loop    

#call main function
combine()
