import cv2
import pytesseract
import openpyxl
pytesseract.pytesseract.tesseract_cmd = r"PATH TO TESSERACT"


# Загрузка изображения автомобиля
image = cv2.imread("PATH TO CAR IMAGE")

# Предобработка изображения для улучшения точности распознавания
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Распознавание текста на изображении с помощью Tesseract
text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')

# Запись распознанного номера в файл Excel
wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = text
wb.save("PATH TO XLSX FILE")
