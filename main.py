from PyPDF2 import PdfFileWriter, PdfFileReader
import slate3k as slate
import sys, getopt

# VARS
mode = 0 #2 for bookmark mode, 3 for pattern mode, 1 for extract mode
# USER STUFF
def help_me():
    f = open(README.md, 'r')
    f_content = f.read()
    print(f_content)
    f.close

pe = '' # extract bookmarks

try:
    opts, args = getopt.getopt(sys.argv[1:], 'e', ['pe='])
except getopt.GetoptError:
    print('Error: Invalid argument')
    help_me()
    sys.exit(2)
for opt, arg in opts:
    if opt in ('-e', '--pe'):
        extract_mode = 1

inputPdfPath = sys.argv[1]
target = sys.argv[2]
instruction_file = sys.argv[3]

def extOp(pdfIndex, text, offset):

    content = text[pdfIndex]
    j = content.find('Operation')
    opStart = content.find('\n', j+1) + 2
    opEnd = content.find('\n', opStart + 1)
    op = content[opStart:opEnd]
    print("Extracted Op:\n", content[opStart:opEnd])
    return op

def addFromHeir():
    a = 4 

def addFromPatt():
    with open(inputPdfPath, 'rb') as f:
        text = slate.PDF(f)
     
    pattern = (open(instruction_file, 'rb')).readlines()
    offset = int(pattern[1])

    for i in range(0, NOP):
        #print(text[i]) 
        bookmark = extOp(i, text, offset) + ' - Sid ' + str(i+1)
        output.addBookmark(bookmark, i, None)

    # show bookmarks on open
    output.setPageMode("/UseOutlines")

    # save to new pdf
    with open("output.pdf", 'wb') as outfp:
        output.write(outfp)

def parseInstructions():
    inst = open(instruction_file, 'r')
    inst_text = inst.read()
    if inst_text.startswith('###') == True:
        mode = 3
        addFromPatt()
    else:
        mode = 2
        addFromHeir()

def extractHeir():
    a = 1

#Read pdf
inputPdfPath = "input.pdf"
inputPdf = open(inputPdfPath, 'rb')
readPdf = PdfFileReader(inputPdf)

output = PdfFileWriter()

# get number of pages
NOP = readPdf.getNumPages()
# copy pdf
for i in range(0, NOP):
    output.addPage(readPdf.getPage(i)) 
# show bookmarks on open
output.setPageMode("/UseOutlines")

if mode == 0:
    parseInstructions()

else:
    extractHeir()
# save to new pdf
with open(target, 'wb') as outfp:
    output.write(outfp)

'''
method to generate bookmark file, call with par from cmd
option to import bookmark file instead of extraction


'''


