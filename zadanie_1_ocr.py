import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\AppData\Local\Tesseract-OCR\tesseract.exe'


def pic_to_text(file_path):
    img = cv2.imread(file_path)
    gray_pic = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return pytesseract.image_to_string(gray_pic)
    '''
    cv2.imshow('image', gray_pic)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

path = r'images\5.jpg'
text = pic_to_text(file_path=path)
print(text)