import cv2
import sys
import pytesseract    
imPath='large.jpg'  
  # Uncomment the line below to provide path to tesseract manually
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
config = ('-l eng --oem 1 --psm 3')
 
  # Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)
 
  # Run tesseract OCR on image
strings = pytesseract.image_to_string(im, config=config)
  # Print recognized text
n=len(strings);
for i in range (n):
    if strings[i]=='p'or strings[i]=='P':
        i1=i;
        i1=i1+1;
        if strings[i1]=='u' or strings[i1]=='U':
            i1=i1+1;
            if strings[i1]=='n' or strings[i1]=='N':
                i1=i1+1;
                if strings[i1]=='e' or strings[i1]=='E':
                    final='PUNE'
    else:
       if(strings[i]=='M' or strings[i]=='m'):
           i1=i;
           i1=i1+1;
           if(strings[i1]=='u' or strings[i1]=='U'):
                i1=i1+1;
                if(strings[i1]=='m'or strings[i1]=='M'):
                    i1=i1+1;
                    if(strings[i1]=='b' or strings[i1]=='B'):
                        i1=i1+1;
                        if(strings[i1]=='a' or strings[i1]=='A'):
                            i1=i1+1;
                            if(strings[i1]=='i' or strings[i1]=='I'):
                                final='MUMBAI'
print(final)
                   