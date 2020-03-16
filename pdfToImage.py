import sys
import os
import re
import unicodedata

from pdf2image import convert_from_path

from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError)


images = convert_from_path(./doc.pdf)


for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
    os.system("tesseract.exe "+ fname + " A" + str(i) + " -l eng")


os.system("copy A*.txt final.txt")




