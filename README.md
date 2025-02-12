# Smart OCR

Smart OCR is a tool designed to extract data from PDF files and convert it directly into JSON format. This facilitates easy data manipulation and integration into various applications.

## Features

- **PDF to JSON Conversion**: Efficiently converts structured data within PDF documents into JSON format.
- **Optical Character Recognition (OCR)**: Utilizes OCR technology to interpret and extract textual data from PDFs.

## Requirements

- Python 3.x
- Required Python libraries (as specified in `requirements.txt`)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yashgadbail/smart-ocr.git
   cd smart-ocr
   ```

2. **Install Dependencies**:

   It's recommended to use a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Place PDF Files**:

   Ensure your target PDF files are accessible to the application.

2. **Run the Application**:
   Execute `python extractor.py`

   Execute the main application script:

   ```bash
   python app.py
   ```

   The application will process the PDF files and output the extracted data in JSON format.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

gemini
