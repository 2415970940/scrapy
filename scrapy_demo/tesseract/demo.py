import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"G:\progamapp\Tesseract-OCR\tesseract.exe"
tessdata_dir_config = '--tessdata-dir "G:\\progamapp\\Tesseract-OCR\\tessdata"'
image = Image.open("test.png")
text = pytesseract.image_to_string(image,config=tessdata_dir_config)
print(text)