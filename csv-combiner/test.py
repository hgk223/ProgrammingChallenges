import sys
import os
import csv
import unittest

class TestMethods(unittest.TestCase):
    def test_headers(self): #test to determine that program can read headers from file
        headers=[]
        file="fixtures/accessories.csv"
        opened=open(file, 'r')
        readFile=csv.reader(opened)
        line=readFile.__next__()
        for col in line:
            if col not in headers:
                headers.append(col)
        opened.close()
        self.assertTrue(headers==["email_hash","category"])
    def test_reader(self):
        file="fixtures/accessories.csv"
        headers=["email_hash","category","file_name"]
        opened=open(file, 'r')
        readFile=csv.reader(opened)
        fileHeads=readFile.__next__() #get header line
        fileName = os.path.basename(file)
        outputWriter=[]
        for readLine in readFile:
            if len(fileHeads)==len(headers)-1:
                readLine.append(fileName)
                outputWriter.append(readLine)
            else:
                newLine=[]
                for x in range(len(headers)-1):
                    if headers[x] in fileHeads:
                        y=fileHeads.index(headers[x])
                        newLine.append(readLine[y])
                    else:
                        newLine.append('')
                newLine.append(fileName)
                outputWriter.append(newLine)
            #exit if condition and loop 
        opened.close()
        self.assertTrue(len(outputWriter)==215)
        self.assertTrue(outputWriter[0]==["b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6","Satchels","accessories.csv"])
    def test_reader_headers(self):
        file="fixtures/accessories.csv"
        headers=["email_hash","password","category","file_name"]
        opened=open(file, 'r')
        readFile=csv.reader(opened)
        fileHeads=readFile.__next__() #get header line
        fileName = os.path.basename(file)
        outputWriter=[]
        for readLine in readFile:
            if len(fileHeads)==len(headers)-1:
                readLine.append(fileName)
                outputWriter.append(readLine)
            else:
                newLine=[]
                for x in range(len(headers)-1):
                    if headers[x] in fileHeads:
                        y=fileHeads.index(headers[x])
                        newLine.append(readLine[y])
                    else:
                        newLine.append('')
                newLine.append(fileName)
                outputWriter.append(newLine)
            #exit if condition and loop 
        opened.close()
        self.assertTrue(len(outputWriter)==215)
        self.assertTrue(outputWriter[0]==["b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6","","Satchels","accessories.csv"])


if __name__ == '__main__':
    unittest.main()