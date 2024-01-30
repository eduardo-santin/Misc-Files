# rotates all pages in a PDF file by a given angle

# imports
from PyPDF2 import PdfReader, PdfWriter
import sys

def rotate_all(input_file, rotation):
    # Open the input file
    input_pdf = PdfReader(input_file)
    # Create a new PDF writer object
    output_pdf = PdfWriter()
    # Loop through each page of the input PDF
    for page in input_pdf.pages:
        # Rotate the page and add it to the new PDF
        page = page.rotate(rotation)
        output_pdf.add_page(page)
    # Save the new PDF to a file
    output_pdf.write(input_file)


# Run the function if the script is run
if __name__ == '__main__':
    # Get the input file and rotation from the command line
    input_file = sys.argv[1]
    rotation = int(sys.argv[2])
    # Run the function
    rotate_all(input_file, rotation)