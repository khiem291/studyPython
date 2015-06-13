'''
Created on Jun 7, 2015

@author: KHIEM
'''
from  PyPDF2 import PdfFileReader
input1 = PdfFileReader(open('System_SysI_w-02062015-185913.pdf', 'rb'))
for i in range(input1.getNumPages()):
    page= input1.getPage(i)
    print page.extractText()


# can use ps2ascii cli linux