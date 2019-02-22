import cv2
import sys
import pytesseract
imPath = 'large.jpg'
     
  # Uncomment the line below to provide path to tesseract manually
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3')
 
  # Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)
 
  # Run tesseract OCR on image
text = pytesseract.image_to_string(im, config=config)
if (text=='PUNE'):
    print('rada rada')
else:
        print(text)
