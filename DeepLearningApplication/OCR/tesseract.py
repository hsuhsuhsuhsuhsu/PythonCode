
import pytesseract
from PIL import Image

#%%
#ENG
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(r"C:\Users\hsu\Desktop\OCRtest\111.png")
    img.show()
    print(pytesseract.image_to_string(img, lang="eng"))
    # path = "output.txt"
    # os.chdir(r"C:\Users\hsu\Desktop\OCRtest")
    # f = open (path,'w')
    # print(pytesseract.image_to_string(img, lang="eng"),file = f)
    # f.close()

if __name__ == "__main__":
    main()
    
#%%
#CHI
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(r"C:\Users\hsu\Desktop\OCRtest\222.jpg")
    img.show()
    print(pytesseract.image_to_string(img, lang="chi_tra"))
    #path = "outputchi.txt"
    #os.chdir(r"C:\Users\hsu\Desktop\OCRtest")
    #f = open (path,'w')
    #print(pytesseract.image_to_string(img, lang="chi_tra"),file = f)
    #f.close()

if __name__ == "__main__":
    main()
    
#%%
#ENG+CHI
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(r"C:\Users\hsu\Desktop\OCRtest\123.jpg")
    img.show()
    print(pytesseract.image_to_string(img, lang="chi_tra+eng"))
    #path = "outputchieng.txt"
    #os.chdir(r"C:\Users\hsu\Desktop\OCRtest")
    # f = open (path,'w')
    # print(pytesseract.image_to_string(img, lang="chi_tra+eng"),file = f)
    # f.close()

if __name__ == "__main__":
    main()





