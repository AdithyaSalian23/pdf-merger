import os
from PyPDF2 import PdfMerger

merger = PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

merger.write("combined.pdf")
merger.close()
