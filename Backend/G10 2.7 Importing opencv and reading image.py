import pytesseract
import cv2 #importing opencv
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_file="image.png"
image = cv2.imread(image_file)#This reads the image file using OpenCV, treating it as an array of pixels.
extracted_text = pytesseract.image_to_string(image)
print(extracted_text)
