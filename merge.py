# import pypdf
from PyPDF2 import PdfReader, PdfWriter

# import os
import os

# import sys
import sys

def merger(pdf1, pdf2):

    # read pdf1
    pdf1File = open(pdf1, 'rb')
    pdf1Reader = PdfReader(pdf1File)
    # get all pages from pdf1
    pages = len(pdf1Reader.pages)
    pages_list = []
    for i in range(pages):
        pages_list.append(pdf1Reader.pages[i])
    
    # read pdf2
    pdf2File = open(pdf2, 'rb')
    pdf2Reader = PdfReader(pdf2File)
    # get all pages from pdf2
    pages = len(pdf2Reader.pages)
    pages_list2 = []
    for i in range(pages):
        pages_list2.append(pdf2Reader.pages[i])
    

    # merge pdf1 and pdf2
    pdfWriter = PdfWriter()
    for page in pages_list:
        pdfWriter.add_page(page)
    for page in pages_list2:
        pdfWriter.add_page(page)
    
    # write to a new pdf file
    pdfOutputFile = open('merged.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

if __name__ == '__main__':
    pdf1 = sys.argv[1]
    pdf2 = sys.argv[2]
    merger(pdf1, pdf2)
