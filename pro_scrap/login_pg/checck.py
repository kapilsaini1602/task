import pytesseract as pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from PIL import Image, ImageFilter, ImageEnhance
from selenium.webdriver.common.by import By
import pytesseract
import os

import cv2
import pytesseract

#
url = 'https://www.vfsglobal.ca/IRCC-AppointmentWave1'

s = Service("/Users/zestgeek26/PycharmProjects/task/pro_scrap/login_pg/chromedriver3")
driver = webdriver.Chrome(service=s)
driver.get(url)

username = 'Jjelu66@yahoo.com'
password = 'Canada@123'

driver.execute_script(f'var element = document.getElementById("EmailId"); element.value = "{username}";')
driver.execute_script(f'var element = document.getElementById("Password"); element.value = "{password}";')

# Submitting the form or click the login button also
# driver.execute_script(f'document.getElementsByClassName("submitbtn")[0].submit();')

soup = BeautifulSoup(driver.page_source, 'html.parser')

image = soup.find("img", {"id": "CaptchaImage"})
# print(image['src'])

element = driver.find_element(By.ID, "CaptchaImage")

location = element.location
size = element.size

driver.save_screenshot("image.png")
image = Image.open("image.png")

x = location['x']
y = location['y']
width = location['x'] + size['width']
height = location['y'] + size['height']
im = Image.open('image.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('image.png')
imageRead = cv2.imread('image.png')
gray = cv2.cvtColor(imageRead, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening
import re

img_text = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
img_text = re.sub('[^A-Za-z0-9]+', '', img_text)
print(img_text)

print(type(img_text))
print(img_text)

#
# #####
#
#
# import base64
# from PIL import Image
# from io import BytesIO
#
# with open("image.png", "rb") as image_file:
#     data = base64.b64encode(image_file.read())
#
# im = Image.open(BytesIO(base64.b64decode(data)))
# im.save('image1.png', 'PNG')
#
# import os
# import easyocr
# import cv2
# import re
# from matplotlib import pyplot as plt
# import numpy as np
# import requests
# import io
# img = cv2.imread("image.png")
# height, width, _ = img.shape
# cv2.imshow("Img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # Cutting image
# roi = img[0: height, 400: width]
#
# url_api = "https://api.ocr.space/parse/image"
# _, compressedimage = cv2.imencode("image.png", roi, [1, 90])
# file_bytes = io.BytesIO(compressedimage)
#
# resulting = requests.post(url_api, files={"image.png": file_bytes},
#                        data = {"apikey":'50e091609188957'})
#
# print(resulting)
#
#
#

# IMAGE_PATH = 'image.png'
# reader = easyocr.Reader(['en'])
# result = reader.readtext(IMAGE_PATH, paragraph="False")
# reader = easyocr.Reader(['en'], gpu=False)
# result = reader.readtext(IMAGE_PATH)
# result = result[0][1]
# result = str(result)
# a = re.sub('[^A-Za-z0-9]+', '', result)
# print(a.upper())

# text = result[1]
# text = text.upper()
# print("chek",text)


##

# image = cv2.imread('image.png',0)
# thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]
#
# result = cv2.GaussianBlur(thresh, (5,5), 0)
# result = 255 - result
#
# data = pytesseract.image_to_string(result, lang='eng',config='--psm 6')
# print(data)
#
# cv2.imshow('thresh', thresh)
# cv2.imshow('result', result)
# cv2.waitKey()


## Actual Func
# def get_Text():
#     imageRead = cv2.imread('image.png')
#     gray = cv2.cvtColor(imageRead, cv2.COLOR_BGR2GRAY)
#     blur = cv2.GaussianBlur(gray, (3, 3), 0)
#     thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
#     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#     opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#     invert = 255 - opening
#
#     img_text = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
#     img_text = str(img_text).replace(" ", '').replace("\n", "").replace("\f", "").upper()
#
#     print(type(img_text))
#     print(img_text)
#     return img_text


applicant_data = [
    {
        "dob":123,
        "FirstNam": "kapil",
        "LastNam": "Saini",
        "Mobile": "",
        "validateEmailI": "abc@gmail.com",
    },

    {
        "dob":123,
        "FirstNam": "kapil",
        "LastNam": "Saini",
        "Mobile": "",
        "validateEmailI": "abc@gmail.com",

    },

    {
        "dob":123,
        "FirstNam": "kapil",
        "LastNam": "Saini",
        "Mobile": "",
        "validateEmailI": "abc@gmail.com",

    },

    {
        "dob":123,
        "FirstNam": "kapil",
        "LastNam": "Saini",
        "Mobile": "",
        "validateEmailI": "abc@gmail.com",

    },

    {
        "dob":123,
        "FirstNam": "kapil",
        "LastNam": "Saini",
        "Mobile": "",
        "validateEmailI": "abc@gmail.com",

    },
]

looping = 0
while looping<=4:
    AddApplicant = driver.find_element_by_link_text('Add Applicant')
    AddApplicant.click()

    dob = driver.find_element(By.ID, "DateOfBirth")
    dob.send_keys(applicant_data[looping]['dob']) #Filling Data

    FirstNam = driver.find_element(By.ID, "FirstName").clear()
    FirstName = driver.find_element(By.ID, "FirstName")
    FirstName.send_keys(applicant_data[looping]['FirstNam']) #Filling Data

    LastName = driver.find_element(By.ID, "LastName").clear()
    LastNam = driver.find_element(By.ID, "LastName")
    LastNam.send_keys(applicant_data[looping]['LastNam']) #Filling Data

    Mobile = driver.find_element(By.ID, "Mobile")
    Mobile.send_keys(applicant_data[looping]['Mobile']) #Filling Data

    validateEmailId = driver.find_element(By.ID, "validateEmailId").clear()
    validateEmailI = driver.find_element(By.ID, "validateEmailId")
    validateEmailI.send_keys(applicant_data[looping]['validateEmailI']) #Filling Data

    submit_btn_app = driver.find_element(By.ID, "submitbuttonId")
    submit_btn_app.click()
    # Alert Popup
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()

    looping = looping+1







