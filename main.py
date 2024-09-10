import pandas as pd
from fpdf import FPDF
from pathlib import Path
import glob

# Create a list of filepaths
filepaths = glob.glob('textFiles/*.txt')

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the file name without extension and convert it to title case
    filename = Path(filepath).stem

    # Add the name to the PDF
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, txt=f"{filename.title()}", ln=1)

    with open(filepath) as file:
        data = file.read()

        # Using multi cells for storing file data to PDF
        pdf.set_font(family="Times", style="", size=12)
        pdf.multi_cell(w=0, h=6, txt=f"{data}")

# Produce the PDF
pdf.output(f"PDFs/output.pdf")
