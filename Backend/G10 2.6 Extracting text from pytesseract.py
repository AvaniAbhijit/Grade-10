import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_file="image.png" #add the name of image file (ensure that image and file are saved in same directory)
extracted_text = pytesseract.image_to_string(image_file) #extract text from the image using pytesseract
print(extracted_text) #print the extracted text on console
