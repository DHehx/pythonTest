import PyPDF2
pdfFileObj = open('600446_2018_z.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)#页数
pageObj = pdfReader.getPage(1)
print(pageObj.extractText(),"utf-8")