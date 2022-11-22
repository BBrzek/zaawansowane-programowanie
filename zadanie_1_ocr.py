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

path = r'images\4.jpg'
text = pic_to_text(file_path=path)
print(text)

def test_pic(file_path):
    img = cv2.imread(file_path)
    gray_pic = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    converted_img = cv2.adaptiveThreshold(cv2.medianBlur(gray_pic, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imshow('image', converted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

test_pic(file_path=path)