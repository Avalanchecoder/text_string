import cv2
import sys
import pytesseract
import RPi.GPIO as GPIO
from time import sleep 
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
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
    while True: 
       GPIO.output(8, GPIO.HIGH) 
       sleep(5) 
       GPIO.output(8, GPIO.LOW) 
       sleep(5)

else:
        print(text)
