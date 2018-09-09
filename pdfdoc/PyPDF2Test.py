import PyPDF2
#读取PDF
pdfFileObj = open('class.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)#页数
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())

#创建PDF
pdfFileWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pageObjNew = pdfReader.getPage(pageNum)
    pdfFileWriter.addPage(pageObjNew)

pdfOutputFile = open('newClass.pdf','wb')
pdfFileWriter.write(pdfOutputFile)
#pdfOutputFile.close()
#pdfFileObj.close()

#叠加页面（常应用在曾加水印）
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
pageObj.mergePage(pdfWatermarkReader.getPage(0))
pdfWithWaterWriter = PyPDF2.PdfFileWriter()
pdfWithWaterWriter.addPage(pageObj)

for pageNum in range(1,pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWithWaterWriter.addPage(pageObj)
resultPdfFile = open('watermarkClass.pdf','wb')
pdfWithWaterWriter.write(resultPdfFile)
resultPdfFile.close()
pdfOutputFile.close()
pdfFileObj.close()