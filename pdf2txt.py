from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import os
from tqdm import tqdm


file_list = os.listdir("/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERpdf/")

def convert_pdf_to_string(file_path):

	output_string = StringIO()
	with open(file_path, 'rb') as in_file:
	    parser = PDFParser(in_file)
	    doc = PDFDocument(parser)
	    rsrcmgr = PDFResourceManager()
	    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
	    interpreter = PDFPageInterpreter(rsrcmgr, device)
	    for page in PDFPage.create_pages(doc):
	        interpreter.process_page(page)

	return(output_string.getvalue())

for file in tqdm(file_list):
	filename = file.split(".")[0]
	with open("/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERtxt/%s.txt"%filename, 'w') as f:
		try:
			content = convert_pdf_to_string("/Users/mengjiexu/Documents/Projects/Twitter/AQ/AAERpdf/"+file)
			f.write(content)
		except:
			print(file)
		