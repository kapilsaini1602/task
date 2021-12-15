# # import re
# # import imaplib
# # import email
# # import time
# #
# #
# # def pri_otp():
# #     fs = open('otp.txt', 'r')
# #     list_of_words = fs.read().split()
# #     next_word = list_of_words[list_of_words.index("is") + 1]
# #     result = re.sub('[^A-Za-z0-9]+', '', next_word)
# #
# #
# # def get_otp():
# #     start = time.time()
# #     with imaplib.IMAP4_SSL(host="imap.mail.yahoo.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
# #         print("Logging into mailbox...")
# #         resp_code, response = imap_ssl.login("Jjelu66@yahoo.com", "vhcvmdeogsqytiti")
# #         print("Response Code : {}".format(resp_code))
# #         print("Response      : {}\n".format(response[0].decode()))
# #         ############### Set Mailbox #############
# #         resp_code, mail_count = imap_ssl.select(mailbox="Inbox", readonly=False)
# #         ############### Retrieve Mail IDs for given Directory #############
# #         resp_code, mails = imap_ssl.search(None, '(FROM "donotreply@vfshelpline.com")', '(UNSEEN)')
# #         for mail_id in mails[0].decode().split()[-2:]:
# #             resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)')
# #             message = email.message_from_bytes(mail_data[0][1])
# #             for part in message.walk():
# #                 print(part.get_content_type())
# #                 if part.get_content_type() == "text/html":
# #                     otp_file = open("otp_reader.txt", 'w')
# #                     otp_file.write(str(part))
# #                     otp_file.close()
# #                     fs = open('otp_reader.txt', 'r')
# #                     list_of_words = fs.read().split()
# #                     next_word = list_of_words[list_of_words.index("is") + 1]
# #                     result = re.sub('[^A-Za-z0-9]+', '', next_word)
# #                     fs.close()
# #                     end = time.time()
# #                     print(end - start)
# #                     return result
# #             break
# #         imap_ssl.close()
# #
# #
# # get_otp()
#
#
# # Import module
# import sqlite3
#
# # Connecting to sqlite
# conn = sqlite3.connect('vfs.db')
# cursor = conn.cursor()
# table = """CREATE TABLE applicant_details(id INTEGER AUTOINCREMENT,dob VARCHAR(25), first_name VARCHAR(30),last_name VARCHAR(30),mobile VARCHAR(15),
# validate_email_id VARCHAR(30),center VARCHAR(20) );"""
#
# cursor.execute(table)
#
# # Creating a cursor object using the
# # cursor() method
# # cursor = conn.cursor()
# # value1 = "abc_center"
# # value2 = "def_category"
# # # Creating table
# #
# #
# # # Queries to INSERT records.
# # sqlite_insert_with_param = """INSERT INTO demo
# #                   (center,category)
# #                   VALUES (?, ?);"""
# # data_tuple = (value1,value2)
# # cursor.execute(sqlite_insert_with_param, data_tuple)
# # conn.commit()
# # cursor.execute("INSERT INTO demo VALUES (?, ?)", value1,value2)
#
# # Commit your changes in
# # the database
# # conn.commit()
# #
# # # Closing the connection
# conn.close()
import sqlite3
import json

conn = sqlite3.connect('/Users/zestgeek26/PycharmProjects/task/pro_scrap/db.sqlite3')
cursor = conn.execute(
    "SELECT * FROM applicant_data where category = 'Biometric Enrolment Student Only' and center='Canada Visa Application Center - Chandigarh' LIMIT 5 OFFSET 5 ")
rows = cursor.fetchall()
print(len(rows))
print(rows)
# print(rows[0][2])
# ls = [(7, 'Canada Visa Application Center - New Delhi', 'Biometric Enrolment Student Only', '2021-12-02', 'Verma', 'kunal', 'v@yahoo.in', ''),
#       (8, 'Canada Visa Application Center - New Delhi', 'Biometric Enrolment Student Only', '2019-02-07', 'verma', 'dh', 'ks@yahoo.in', ''),
#       (9, 'Canada Visa Application Center - New Delhi', 'Biometric Enrolment Student Only', '2000-02-14', 'Sahil', 'gupta', 'sh@yahoo.com', ''),
#       (10, 'Canada Visa Application Center - New Delhi', 'Biometric Enrolment Student Only', '2000-03-14', 'santosh', 'kumar', 'sk@gmail.com', ''),
#       (11, 'Canada Visa Application Center - New Delhi', 'Biometric Enrolment Student Only', '2001-04-14', 'Mittal', 'Ms', 'ms@yahoo.com', '')]
#
# looping = 0
# var = "abc"
# while looping <5 and var == "abc":
#     print(rows[looping][3])
#     print(rows[looping][4])
#     print(rows[looping][5])
#     print(rows[looping][6])
#     looping=looping+1
#     print("Break")
# print(ls[0][1])
# looping = 0
# while looping<5:
#
# while looping <5:
#     print(row[1])
#     print(row[2])
#     store = [
#         {
#             "dob": row[3],
#             "FirstNam": row[4],
#             "LastNam": row[5],
#             "validateEmailI": row[6],
#         },
#     ]
#     print(store)
#
# for row in rows:
#     print(row[1])
#     print(row[2])
#     store = [
#         {
#             "dob": row[3],
#             "FirstNam": row[4],
#             "LastNam": row[5],
#             "validateEmailI": row[6],
#         },
#     ]
#     print(store)
# if len(rows) > 1:
#     driver.execute_script("window.open('https://www.geeksforgeeks.org/');")

# Tabbing to other tab
# check_win = 'abc'
# if check_win == "abc":
#     driver.execute_script("window.open('https://www.vfsglobal.ca/IRCC-AppointmentWave1/');")
#     driver.switch_to.window(driver.window_handles[1])
