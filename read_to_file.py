'''
Sample python script to demonstrate text extraction form PDF
'''
import PyPDF2

pdfFileObj = open("quotes.pdf", "rb")

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)

	mytext += pageObj.extractText()

pdfFileObj.close()

with open("quotes.txt", "w") as f:
    f.write(mytext)
