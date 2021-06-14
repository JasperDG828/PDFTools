from array import array
from PyPDF2 import PdfFileReader
from tkinter import filedialog as fd
from datetime import datetime

from PyPDF2.pdf import PdfFileWriter

#-------------------------------------------#

def getInformation(pdfPath:str=None):
    if(pdfPath==None):
        print("Select a pdf-file to start")
        path = fd.askopenfilename(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        path=pdfPath
    f=open(path, "rb")
    pdf=PdfFileReader(f)

    info=pdf.getDocumentInfo()
    pages=pdf.getNumPages()

    txt=f"""
    {path}

    Title: {info.title}

    Author: {info.author}
    Creator: {info.creator}
    Producer: {info.producer}
    Subject: {info.subject}
    Pages: {pages}
    """
    f.close()

def merge(files:array=None, out:str=None):
    writer = PdfFileWriter()
    if(files==None):
        inputFiles = fd.askopenfilenames(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        inputFiles=files
    if(out==None):
        output = fd.asksaveasfilename(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        output=out
    for path in inputFiles:
        reader = PdfFileReader(path)
        for page in range(reader.getNumPages()):
            writer.addPage(reader.getPage(page))
    
    with open(output+".pdf", "wb") as out:
        writer.write(out)
        out.close()

def reversePages(inPath: str):
    reader = PdfFileReader(inPath)
    writer = PdfFileWriter()
    i=0
    while i<reader.getNumPages():
        writer.addPage(reader.getPage(reader.getNumPages()-i-1))
        i=i+1
    now=datetime.now()
    name=f"temp/PythonPdfTools{now.strftime('%d_%m_%Y_%H_%M_%S')}.pdf"
    f=open(name, "wb")
    writer.write(f)
    f.close()
    return name



def mergeOddEven(oddIn:str=None, evenIn:str=None, out:str=None, reverseEven:bool=False):
    if oddIn==None:
        odd = fd.askopenfilename(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        odd=oddIn

    if evenIn==None:
        even=fd.askopenfilename(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        even=evenIn
    if out==None:
        output=fd.asksaveasfilename(filetypes=(("PDF Documents", "*.pdf"),("PDF Documents", "*.PDF")))
    else:
        output=out
    
    writer=PdfFileWriter()
    oddReader = PdfFileReader(odd)
    if reverseEven:
        EvenReader=PdfFileReader(reversePages(even))
    else:
        EvenReader=PdfFileReader(even)
    i=0
    j=EvenReader.getNumPages()
    a=False#These are variables to check if there are any pages left
    b=False
    while not (a==True and b==True):
        #odd
        try:
            writer.addPage(oddReader.getPage(i))
        except:
            a=True
        #even
        try:
            writer.addPage(EvenReader.getPage(i))
        except:
            b=True
        i=i+1
    outF = open(output+".pdf", "wb")
    writer.write(outF)
    outF.close()
    
