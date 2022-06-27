from fpdf import FPDF

import os
from os import listdir
from os.path import isfile, join

import sys


def is_image(filename):
	return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("error: no directory/pdf file name have been set")
		sys.exit(1)
	
	path = sys.argv[1] 
	if not os.path.isdir(path):
		print(f"error: {path} not a directory")
		sys.exit(1)
	
	files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and is_image(f)]

	print(f"{len(files)} files has been detected")

	pdf_name = sys.argv[-1]
	print(f"crating a PDF file {pdf_name}.pdf")

	pdf = FPDF()
	print(pdf)
	for image in files:
    pdf.add_page()
    pdf.image(image,x,y,w,h)

	pdf.output(pdf_name, "F")

