# MULTILINGUAL-OCR-MODEL
Welcome to the Multilingual OCR System project! This project leverages advanced technologies and APIs such as OpenCV, Pytesseract, Googletrans, PIL, and Tkinter to achieve efficient text extraction and translation from images. This system is particularly useful in the fintech industry for automating various tasks such as data entry, KYC processes, invoice processing, cheque clearing, and improving customer service.
# Table of Contents
Introduction
Features
Technologies Used
Installation
Usage
Contributing
License
Acknowledgements
# Introduction
The Multilingual OCR System is designed to read text from images, recognize and translate it into multiple languages. The project integrates various libraries and APIs to ensure high accuracy and efficiency in text extraction and translation.
# Features
Image Preprocessing: Enhances image quality for better OCR performance using OpenCV.

Text Extraction: Utilizes Pytesseract for character recognition with CNNs and LSTM networks.

Multilingual Translation: Supports translation into multiple languages using Googletrans.

User-Friendly GUI: Provides an intuitive interface for users to upload images and view results using Tkinter.
# Technologies used 
OpenCV: Used for image preprocessing tasks such as noise reduction, thresholding, and edge detection.

Pytesseract: A Python wrapper for the Tesseract-OCR Engine, leveraging CNNs and LSTM networks for text recognition.

Googletrans: A Python API for Google Translate, using sequence-to-sequence models and attention mechanisms for accurate translation.

PIL (Python Imaging Library): Used for basic image handling tasks like loading, converting, and resizing images.

Tkinter: A standard Python interface for creating graphical user interfaces.
# Installation 
To set up the project locally, follow these steps:

Clone the repository:

git clone https://github.com/your_username/multilingual-ocr-system.git
cd multilingual-ocr-system
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install the required packages:

pip install -r requirements.txt
Download and install Tesseract-OCR:

For Windows: Download the installer from Tesseract at UB Mannheim.

For macOS: Use Homebrew to install Tesseract:

brew install tesseract
For Linux: Use the package manager to install Tesseract:

sudo apt-get install tesseract-ocr
# Usage
1.Run the GUI application:

Final OCR 100 lang.py

2.Use the interface:

Click on the "Browse Image" button to select an image file.
Choose the desired language for translation from the dropdown menu.
The system will display the extracted text and its translation.
