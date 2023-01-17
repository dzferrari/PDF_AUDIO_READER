'''
Python script to extract from pdf and create a text file
'''
import argparse
import os
import PyPDF3

parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", help="path to the PDF file", required=True)
parser.add_argument("--output", "-o", help="output file name")
args = parser.parse_args()

pdfFileObj = open(args.file, "rb")
pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    mytext += pageObj.extractText()

pdfFileObj.close()

# if output file name not provided, use input file name with .txt extension
if args.output is None:
    base_name = os.path.basename(args.file)
    base_name = os.path.splitext(base_name)[0]
    args.output = f'{base_name}.txt'

with open(args.output, "w") as f:
    f.write(mytext)
