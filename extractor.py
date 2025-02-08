import fitz
import os
from pathlib import Path

def extract_pdf_pages_as_images(pdf_folder, output_folder):
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        doc = fitz.open(pdf_path)
        
        # Extract each page as an image
        for page_num in range(len(doc)):
            page = doc[page_num]
            pix = page.get_pixmap()
            
            # Create output filename
            output_file = os.path.join(
                output_folder, 
                f"{pdf_file[:-4]}_page_{page_num + 1}.png"
            )
            
            # Save the image
            pix.save(output_file)
        
        doc.close()

if __name__ == "__main__":
    pdf_folder = "<Folder Name>"
    output_folder = "extracted_images"
    
    extract_pdf_pages_as_images(pdf_folder, output_folder)