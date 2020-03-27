import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open('test2.jpg')
code = pytesseract.image_to_string(image, lang='chi_sim_vert')
print(code)