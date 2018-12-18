from PyPDF2 import PdfFileWriter, PdfFileReader
import slate3k as slate
import sys, getopt
import os, sys

# VARS
mode = 0 #2 for bookmark mode, 3 for pattern mode, 1 for extract mode
batch_mode = False
# USER STUFF
def help_me():
    f = open('README.md', 'r')
    f_content = f.read()
    print(f_content)
    f.close

e = '' # extract bookmarks
b = '' # batch mode
i = '' # input
o = '' # output
p = '' # pattern

try:
    opts, args = getopt.getopt(sys.argv[1:], 'e:b:i:o:p:', ['e=', 'b=', 'i=', 'o=', 'p='])
except getopt.GetoptError:
    print('Error: Invalid argument')
    help_me()
    sys.exit(2)
#print(sys.argv)
for opt, arg in opts:
    
    if opt in ('-e'):
        mode = 1
    elif opt in ('-b'):
        batch_mode = True
        inputPdfPath = arg
    elif opt in ('-i'):
        inputPdfPath = arg
    elif opt in ('-o'):
        target = arg
    elif opt in ('-p'):
        instruction_file = arg

def extOp(pdfIndex, text, offset):

    content = text[pdfIndex]
    j = content.find('Operation')
    opStart = content.find('\n', j+1) + 2
    opEnd = content.find('\n', opStart + 1)
    op = content[opStart:opEnd]
    print("Extracted Operation:\n", content[opStart:opEnd])
    return op

def addFromHeir():
    a = 4 

def addFromPatt(path, NOP, pdfWriter):
    with open(path, 'rb') as f:
        text = slate.PDF(f)
     
    pattern = (open(instruction_file, 'rb')).readlines()
    offset = int(pattern[1])

    for i in range(0, NOP):
        #print(text[i]) 
        bookmark = extOp(i, text, offset) + ' - Sid ' + str(i+1)
        pdfWriter.addBookmark(bookmark, i, None)

    # show bookmarks on open
    pdfWriter.setPageMode("/UseOutlines")

def parseInstructions(path, NOP, pdfWriter):
    inst = open(instruction_file, 'r')
    inst_text = inst.read()
    if inst_text.startswith('###') == True:
        mode = 3
        addFromPatt(path, NOP, pdfWriter)
    else:
        mode = 2
        addFromHeir(path, NOP, pdfWriter)

def extractHeir():
    a = 1

def generatePdf(inputFileName, path):
    #Read pdf
    if batch_mode == True:
        outputPdfPath = path+'/newFiles/'+inputFileName
        inputPdf = open(path +'/' + inputFileName, 'rb')
        # create new folder if none exists
        if not os.path.exists(path+'/newFiles'):
            os.makedirs(path+'/newFiles')

    else:
        inputPdf = open(inputFileName, 'rb')
        outputPdfPath = path
    
    readPdf = PdfFileReader(inputPdf)

    output = PdfFileWriter()

    # get number of pages
    NOP = readPdf.getNumPages()
    # copy pdf
    for i in range(0, NOP):
        output.addPage(readPdf.getPage(i)) 
    # show bookmarks on open
    output.setPageMode("/UseOutlines")

    if mode == 0 and batch_mode == True:
        print(inputFileName)
        parseInstructions(path + '/' + inputFileName, NOP, output)
        print('\n')
    
    elif mode == 0 and batch_mode == False:
        print(os.path.basename(inputFileName))
        parseInstructions(inputFileName, NOP, output)

    else:
        extractHeir()
    # save to new pdf
    with open(outputPdfPath, 'wb') as outfp:
        output.write(outfp)

if batch_mode == False:
    generatePdf(inputPdfPath, target)

elif batch_mode == True:
    #get list of pdfs in folder non-recursively
    files = os.listdir(inputPdfPath)
    print(files)
    files = [x for x in files if x.endswith('.pdf')]
    print(files,'\n\n')
    #apply action for all of them and save them in new subfolder
    for file in files:
        generatePdf(file, inputPdfPath)
'''
method to generate bookmark file, call with par from cmd
option to import bookmark file instead of extraction


'''


