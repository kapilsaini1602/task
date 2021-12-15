# import requests
#
#
# def ocr_space_file(filename, overlay=False, api_key='50e091609188957', language='eng'):
#
#     payload = {'isOverlayRequired': overlay,
#                'apikey': '50e091609188957',
#                'language': 'eng',
#                }
#     with open(filename, 'rb') as f:
#         r = requests.post('https://api.ocr.space/parse/image',
#                           files={filename: f},
#                           data=payload,
#                           )
#     print(r)
#     print(r.content.decode())
#     return r.content.decode()
#
#
# ocr_space_file(filename='image.png', language='eng')

import io
import json
import cv2
import numpy as np
import requests

img = cv2.imread("abc.jpeg")
height, width, _ = img.shape
# Cutting image
roi = img[0: height, 0: width]
# Ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".png", roi)
file_bytes = io.BytesIO(compressedimage)
result = requests.post(url_api,
                       files={"abc.jpeg": file_bytes},
                       data={"apikey": '50e091609188957',
                             "language": "eng"})
print(result)
print(result.content.decode())
result = result.content.decode()
result = json.loads(result)
parsed_results = result.get("ParsedResults")[0]
text_detected = parsed_results.get("ParsedText")

print(text_detected)

import pytesseract as pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PIL import Image, ImageFilter, ImageEnhance
from selenium.webdriver.common.by import By
import pytesseract
import os
from selenium.webdriver.common.by import By
import easyocr
import cv2
import pytesseract
import time
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.vfsglobal.ca/IRCC-AppointmentWave1/'

s = ("chromedriver")
driver = webdriver.Chrome(executable_path="/Users/zestgeek14/PycharmProjects/Scrapping_xml/testPack/chromedriver")
driver.get(url)

username = 'Jjelu66@yahoo.coom'
password = 'Canada@123'


def get_Text():
    IMAGE_PATH = 'image.png'
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH, paragraph="False")
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(IMAGE_PATH)
    result = result[0][1]
    result = str(result)
    result = re.sub('[^A-Za-z0-9]+', '', result)
    img_text = result.upper()
    print(result)
    print(img_text)
    return img_text


while True:
    driver.execute_script(f'var element = document.getElementById("EmailId"); element.value = "{username}";')
    driver.execute_script(f'var element = document.getElementById("Password"); element.value = "{password}";')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

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

    img_text = get_Text()

    cap_Input = driver.find_element(By.ID, "CaptchaInputText")
    cap_Input.send_keys(img_text)

    driver.find_element(By.CLASS_NAME, "submitbtn").send_keys(Keys.RETURN)

    time.sleep(3)
    if driver.current_url == url:
        continue
    else:
        break
schedule_appointment = driver.find_element_by_link_text('Schedule Appointment')
schedule_appointment.click()

select_center = driver.find_element(By.ID, 'LocationId')
select_center_new = Select(select_center)
select_center_new.select_by_index(4)
# select_center_new.select_by_visible_text('my text') # by text

# Application id
application_center = driver.find_element(By.ID, 'NoOfApplicantId')
application_center_new = Select(application_center)
application_center_new.select_by_index(5)

# appointment cateogry
appointment_category = driver.find_element(By.ID, 'VisaCategoryId')
appointment_category_new = Select(appointment_category)
appointment_category_new.select_by_index(2)
time.sleep(1)
terms_and_cond = driver.find_element(By.ID, 'IAgree')
terms_and_cond.click()
time.sleep(2)

continue_btn = driver.find_element(By.ID, "btnContinue")
continue_btn.click()

##Add applicant button
# i= 0
# record1 = ['2000-11-20','Santosh','Kuma','8607696612',"kapils.zestgeek@gmail.com"]
# record2 = ['2000-1-21','Santos','Kum','8607696634',"kapilq.zestgeek@gmail.com"]
# record3 = ['2000-5-22','Santh','Ku','8607696656',"kapila.zestgeek@gmail.com"]
# record4 = ['2000-4-23','Sansh','K','8607696678',"kapilz.zestgeek@gmail.com"]
# record5 = ['2000-3-2','Sosh','Kumard','8607696690',"kapilzz.zestgeek@gmail.com"]
while i <= 5:
    AddApplicant = driver.find_element_by_link_text('Add Applicant')
    AddApplicant.click()
    dob = driver.find_element(By.ID, "DateOfBirth")
    dob.send_keys('2000-11-23')
    FirstNam = driver.find_element(By.ID, "FirstName").clear()
    FirstName = driver.find_element(By.ID, "FirstName")
    FirstName.send_keys('Santosh')
    LastName = driver.find_element(By.ID, "LastName").clear()
    LastNam = driver.find_element(By.ID, "LastName")
    LastNam.send_keys('Kumar')
    Mobile = driver.find_element(By.ID, "Mobile")
    Mobile.send_keys('8607696626')
    validateEmailId = driver.find_element(By.ID, "validateEmailId").clear()
    validateEmailI = driver.find_element(By.ID, "validateEmailId")
    validateEmailI.send_keys("kapil.zestgeek@gmail.com")
    submit_btn_app = driver.find_element(By.ID, "submitbuttonId")
    submit_btn_app.click()
    # Alert Popup
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    i = i + 1
    print(i)

# Adding list
dob = driver.find_element(By.ID, "DateOfBirth")
dob.send_keys('2000-11-23')
FirstNam = driver.find_element(By.ID, "FirstName").clear()
FirstName = driver.find_element(By.ID, "FirstName")
FirstName.send_keys('Santosh')
LastName = driver.find_element(By.ID, "LastName").clear()
LastNam = driver.find_element(By.ID, "LastName")
LastNam.send_keys('Kumar')
Mobile = driver.find_element(By.ID, "Mobile")
Mobile.send_keys('8607696626')
validateEmailId = driver.find_element(By.ID, "validateEmailId").clear()
validateEmailI = driver.find_element(By.ID, "validateEmailId")
validateEmailI.send_keys("kapil.zestgeek@gmail.com")
submit_btn_app = driver.find_element(By.ID, "submitbuttonId")
submit_btn_app.click()
# Alert Popup
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()

# OTP
otp = driver.find_element(By.CLASS_NAME, "submitbtn")
otp.click()
# try:
#     AddApplicant = driver.find_element_by_link_text('Add Applicant')
#     AddApplicant.click()
# except:
#     pass
