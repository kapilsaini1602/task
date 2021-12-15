import sqlite3
import pytesseract as pytesseract
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Keys
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
import imaplib
import email

url = 'https://www.vfsglobal.ca/IRCC-AppointmentWave1/'

s = Service("/Users/zestgeek26/PycharmProjects/task/pro_scrap/login_pg/chromedriver3")
driver = webdriver.Chrome(service=s)
driver.get(url)

time.sleep(2)
username = 'Jjelu66@yahoo.com'
password = 'Canada@123'


def get_email_otp():
    print("Trigger")
    ################ IMAP SSL ##############################
    with imaplib.IMAP4_SSL(host="imap.mail.yahoo.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
        ############### Login to Mailbox ######################
        resp_code, response = imap_ssl.login("Jjelu66@yahoo.com", "vhcvmdeogsqytiti")
        ############### Set Mailbox #############
        resp_code, mail_count = imap_ssl.select(mailbox="Inbox", readonly=False)
        ############### Retrieve Mail IDs for given Directory #############
        resp_code, mails = imap_ssl.search(None, '(FROM "donotreply@vfshelpline.com")', '(UNSEEN)')
        for mail_id in mails[0].decode().split()[-2:]:
            resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)')
            message = email.message_from_bytes(mail_data[0][1])
            for part in message.walk():
                if part.get_content_type() == "text/html":
                    otp_file = open("otp_reader.txt", 'w')
                    otp_file.write(str(part))
                    otp_file.close()
                    fs = open('otp_reader.txt', 'r')
                    otp = fs.read().split()
                    next_word = otp[otp.index("is") + 1]
                    result = re.sub('[^A-Za-z0-9]+', '', next_word)
                    fs.close()
                    if result is not None:
                        return result
            break
        imap_ssl.close()


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
    print(driver.title)
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
time.sleep(2)
conn = sqlite3.connect('/Users/zestgeek26/PycharmProjects/task/pro_scrap/db.sqlite3')
cursor = conn.execute(
    "SELECT * FROM applicant_data where category = 'Biometric Enrolment Student Only' and center='Canada Visa Application Center - Chandigarh' LIMIT 5")
rows = cursor.fetchall()

select_center = driver.find_element(By.ID, 'LocationId')
select_center_new = Select(select_center)
select_center_new.select_by_visible_text(rows[0][1])  # by text
time.sleep(2)
# Application id

# Select Number of applicants
application_center = driver.find_element(By.ID, 'NoOfApplicantId')
application_center_new = Select(application_center)
application_center_new.select_by_index(len(rows))
time.sleep(2)

# appointment cateogry
appointment_category = driver.find_element(By.ID, 'VisaCategoryId')
appointment_category_new = Select(appointment_category)
appointment_category_new.select_by_visible_text(rows[0][2])  # by text
time.sleep(1)

value1 = select_center_new.first_selected_option.text
value2 = appointment_category_new.first_selected_option.text

terms_and_cond = driver.find_element(By.ID, 'IAgree')
terms_and_cond.click()
time.sleep(2)

continue_btn = driver.find_element(By.ID, "btnContinue")
continue_btn.click()
time.sleep(4)
##Add applicant button

looping = 0
while looping < len(rows):
    AddApplicant = driver.find_element_by_link_text('Add Applicant')
    AddApplicant.click()
    time.sleep(4)
    dob = driver.find_element(By.ID, "DateOfBirth")
    dob.send_keys(rows[looping][3])  # Filling Data

    FirstNam = driver.find_element(By.ID, "FirstName").clear()
    FirstName = driver.find_element(By.ID, "FirstName")
    FirstName.send_keys(rows[looping][4])  # Filling Data
    time.sleep(4)

    LastName = driver.find_element(By.ID, "LastName").clear()
    LastNam = driver.find_element(By.ID, "LastName")
    LastNam.send_keys(rows[looping][5])  # Filling Data
    time.sleep(4)

    # Mobile = driver.find_element(By.ID, "Mobile")
    # Mobile.send_keys(applicant_data[looping]['Mobile'])  # Filling Data
    # time.sleep(4)

    validateEmailId = driver.find_element(By.ID, "validateEmailId").clear()
    validateEmailI = driver.find_element(By.ID, "validateEmailId")
    validateEmailI.send_keys(rows[looping][6])  # Filling Data
    time.sleep(4)

    # Insertion of Applicant Data in DB

    # Ending of Insertion of Applicant data in DB

    submit_btn_app = driver.find_element(By.ID, "submitbuttonId")
    submit_btn_app.click()
    time.sleep(5)
    # Alert Popup
    # WebDriverWait(driver, 10).until(EC.alert_is_present())
    # driver.switch_to.alert.accept()
    # time.sleep(5)
    looping = looping + 1

    time.sleep(3)

### outside loop filled 5 applicants

otp = driver.find_element(By.CLASS_NAME, "submitbtn")  # Send OTP
otp.click()
time.sleep(25)

input_otp = driver.find_element(By.ID, "OTPe")
input_otp.send_keys(get_email_otp())  # Filling OTP
time.sleep(4)

otp_sub = driver.find_element(By.ID, "txtsub")
otp_sub.click()
time.sleep(4)

if len(rows) > 4:
    driver.execute_script("window.open('https://www.vfsglobal.ca/IRCC-AppointmentWave1/');")

# calendar_id = driver.find_element(By.CLASS_NAME, "fc-day-number")
# try:
#     calendar_id.send_keys("22")
#     calendar_id.click()
# except Exception as e:
#     print(str(e))

# calendar_id.send_keys("2021-12-04")
# calendar_id.click()
# time.sleep(2)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# for item in soup.findAll("td", {'style': "color: rgb(255, 106, 106);"}):
#     aa = (item.get("data-date"))
#     aa.click()
#     print(aa)
# # for item in s oup.findAll("td",  {'style="width: 15px; height: 15px; background-color: #BCED91; border: 1px solid
# # #9a8f8f;'}): print(item.get("data-date"))
# confrom_date = driver.find_element(By.ID, "btnConfirm")
# print(confrom_date)
# confrom_date.click()
# time.sleep(2)

# confrom_date = driver.find_element(By.ID, "btnConfirm")
# print(confrom_date)
# confrom_date.click()
# time.sleep(2)

# switching to other tab


# if len(rows) > 5:
#     driver.execute_script("window.open('https://www.vfsglobal.ca/IRCC-AppointmentWave1/');")
#     driver.switch_to.window(driver.window_handles[1])


# for item in soup.findAll("td",  {'style="width: 15px; height: 15px; background-color: #BCED91; border: 1px solid
# #9a8f8f;'}): print(item.get("data-date"))
# confrom_date = driver.find_element(By.ID, "btnConfirm")
# confrom_date.click()
# time.sleep(2)
# try:
#     from_dp = driver.find_element(By.ID, "calendar")
#     print(from_dp)
# except:
#     from_dp = driver.find_element(By.ID, "caldiv")
#     print("Except part", from_dp)

# for item in driver.find("td", {'style':"color: rgb(204, 204, 204); background-color: rgb(255, 106, 106);"}):
#     print(item.get("data-date"))
