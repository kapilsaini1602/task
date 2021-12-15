# import time
# from itertools import chain
# import email
# import imaplib
#
# # note for yahoo, enable less secure apps with https://login.yahoo.com/account/security Under Yahoo settings
# # Allow apps that use less secure sign in
# # Some non-Yahoo apps and devices use less secure sign-in technology, which could leave your account vulnerable. You can turn off access (which we recommend) or choose to use them despite the risks.
#
# # Due to inbox Yahoo security, you may need to train the service to know your sending email is not spam!
# # ensure to whitelist the sender email so it does not end up in the spambox http://onlinegroups.net/blog/2014/02/25/how-to-whitelist-an-email-address/
#
# # for oanda order packages
# import json
# from oandapyV20 import API
# import oandapyV20.endpoints.orders as orders
# from oandapyV20.exceptions import V20Error
# # from exampleauth import exampleAuth
# import logging
#
# imap_ssl_host = 'imap.mail.yahoo.com'  # 'imap.gmail.com'  # imap.mail.yahoo.com
# imap_ssl_port = 993
# username = 'Jjelu66@yahoo.com'
# password = 'izztfovdvrzfihba'
#
# # Restrict mail search. Be very specific.
# # Machine should be very selective to receive messages.
# criteria = {
#     'FROM': 'donotreply@vfshelpline.com'  # ,
#     # 'SUBJECT': 'signal',
#     # 'BODY':    'signal is this',
# }
# # criteria = {
# #     'FROM':    'PRIVILEGED EMAIL ADDRESS',
# #     'SUBJECT': 'SPECIAL SUBJECT LINE',
# #     'BODY':    'SECRET SIGNATURE',
# # }
# uid_max = 0
#
#
# def search_string(uid_max, criteria):
#     c = list(map(lambda t: (t[0], '"' + str(t[1]) + '"'), criteria.items())) + [('UID', '%d:*' % (uid_max + 1))]
#     return '(%s)' % ' '.join(chain(*c))
#     # Produce search string in IMAP format:
#     #   e.g. (FROM "me@gmail.com" SUBJECT "abcde" BODY "123456789" UID 9999:*)
#
#
# def get_first_text_block(msg):
#     type = msg.get_content_maintype()
#
#     if type == 'multipart':
#         for part in msg.get_payload():
#             if part.get_content_maintype() == 'text':
#                 return part.get_payload()
#     elif type == 'text':
#         return msg.get_payload()
#
#
# server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
# server.login(username, password)
# print(username)
# server.select('INBOX')
# result, data = server.uid('search', None, search_string(uid_max, criteria))
#
# uids = [int(s) for s in data[0].split()]
# if uids:
#     uid_max = max(uids)
#     # Initialize `uid_max`. Any UID less than or equal to `uid_max` will be ignored subsequently.
#
# server.logout()
#
# # set up logginng info for debugging
#
# logging.basicConfig(
#     filename="log.out",
#     level=logging.INFO,
#     format='%(asctime)s [%(levelname)s] %(name)s : %(message)s',
# )
#
# # accountID, token = exampleAuth()
#
# # Keep checking messages ...
# # I don't like using IDLE because Yahoo does not support it.
# while 1:
#     # Have to login/logout each time because that's the only way to get fresh results.
#
#     server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
#     server.login(username, password)
#     server.select('INBOX')
#
#     result, data = server.uid('search', None, search_string(uid_max, criteria))
#
#     uids = [int(s) for s in data[0].split()]
#     for uid in uids:
#         # Have to check again because Gmail sometimes does not obey UID criterion.
#
#         if uid > uid_max:
#             result, data = server.uid('fetch', uid, '(RFC822)')  # fetch entire message
#             msg = email.message_from_string(data[0][1])
#
#             uid_max = uid
#
#             # sample text = "sym,EUR_USD,qty,1,Close,0.45,Htp,0.4545,Hsl,0.4455"
#
#             text = get_first_text_block(msg)
#             print('New message :::::::::::::::::::::')
#             print(text)
#             tok = text.split(',')
#             sym = tok[1]
#             qty = float(tok[3])
#             cl = float(tok[5])
#             tp = float(tok[7])
#             sl = float(tok[9])
#             print('pair ' + sym)
#             print('qty ' + str(qty))
#             print('cl ' + str(cl))
#             print('tp ' + str(tp))
#             print('sl ' + str(sl))
#
#             # for Oanda:
#             # https://github.com/oanda/v20-python-samples
#             # -*- coding: utf-8 -*-
#             """create order demo.
#             demonstrates:
#             - placing a market order
#             - placing a faulty market order
#             - logging
#             """
#
#             print('send your order via order via oanda')
#
#             api = API(access_token=token)
#
#             orderConf = [
#                 # ok
#                 {
#                     "order": {
#                         "units": qty,
#                         "instrument": sym,
#                         "timeInForce": "FOK",
#                         "type": "MARKET",
#                         "positionFill": "DEFAULT"
#                     }
#                 }  # ,
#                 # wrong instrument, gives an error
#                 # {
#                 #   "order": {
#                 #      "units": "100",
#                 #      "instrument": "UR_USD",
#                 #      "timeInForce": "FOK",
#                 #      "type": "MARKET",
#                 #      "positionFill": "DEFAULT"
#                 #    }
#                 #  }
#
#             ]
#
#             # create and process order requests
#             for O in orderConf:
#                 r = orders.OrderCreate(accountID=accountID, data=O)
#                 print("processing : {}".format(r))
#                 print("===============================")
#                 print(r.data)
#                 try:
#                     response = api.request(r)
#                 except V20Error as e:
#                     print("V20Error: {}".format(e))
#                 else:
#                     print("Response: {}\n{}".format(r.status_code,
#                                                     json.dumps(response, indent=2)))
#
#     server.logout()
#     print('check email....')
#     time.sleep(1)
# username = 'Jjelu66@yahoo.com'
# password = 'izztfovdvrzfihba'

import imaplib  # Library to interact with IMPAP server
import sys
# my reusable library to prompt password using tkinter


# IMAP4 server for gmail
# IMAP_server = "imap.gmail.com"  # gmail IMAP server
from itertools import chain
#
# IMAP_server = "imap.mail.yahoo.com"  # Yahoo IMAP server
# mail_id = "Jjelu66@yahoo.com"
#
#
# if __name__ == "__main__":
#     """
#     Entry block of the script
#     """
#
#     # Instantiate IMAP4 interface
#     imap = imaplib.IMAP4_SSL(IMAP_server)
#
#     # Instantiate the tkinter class to prompt for password
#     ui = 'izztfovdvrzfihba'
#     pwd = 'izztfovdvrzfihba'
#
#     # login to the server
#     try:
#         status, summary = imap.login(mail_id, pwd)
#         if status == "OK":
#             print(summary)
#     except imaplib.IMAP4.error:
#         print("Error logging into Mail")
#         sys.exit(0)  # Successful termination
#
#     # Get list of mailboxes in server
#     status, mailboxes = imap.list()
#     if status == "OK":
#         print("***List of mailboxes***")
#         for index, mailbox in enumerate(mailboxes):
#             print(index + 1, mailbox)
#     else:
#         print("Error retreiving mailbox information - {}".format(status))
#
#     # Connect to a particular mailbox
#     status, data = imap.select("Inbox")  # inbox name from list() used above
#
#
#
#
#     criteria = {
#         'FROM': 'support@quantlabs.net'  # ,
#         # 'SUBJECT': 'signal',
#         # 'BODY':    'signal is this',
#     }
#
#
#
#
#     if status == "OK":
#         print("No of items in mailbox: {}".format(data))
#         print(status)
#         # Process the mailbox
#
#
#
#         imap.close()
#
#     # Logout of the IMAP server
#     imap.logout()
import imaplib
import email

################ IMAP SSL ##############################

with imaplib.IMAP4_SSL(host="imap.mail.yahoo.com", port=imaplib.IMAP4_SSL_PORT) as imap_ssl:
    print("Connection Object : {}".format(imap_ssl))

    ############### Login to Mailbox ######################
    print("Logging into mailbox...")
    resp_code, response = imap_ssl.login("Jjelu66@yahoo.com", "vhcvmdeogsqytiti")

    print("Response Code : {}".format(resp_code))
    print("Response      : {}\n".format(response[0].decode()))

    ############### Set Mailbox #############
    resp_code, mail_count = imap_ssl.select(mailbox="Inbox", readonly=True)

    ############### Retrieve Mail IDs for given Directory #############
    resp_code, mails = imap_ssl.search(None, '(FROM "donotreply@vfshelpline.com")', '(UNSEEN)')

    print("Mail IDs : {}\n".format(mails[0].decode().split()))

    ############### Display Few Messages for given Directory #############
    for mail_id in mails[0].decode().split()[-2:]:
        print("================== Start of Mail [{}] ====================".format(mail_id))
        resp_code, mail_data = imap_ssl.fetch(mail_id, '(RFC822)')  ## Fetch mail data.
        message = email.message_from_bytes(mail_data[0][1])  ## Construct Message from mail data
        print("From       : {}".format(message.get("From")))
        print("To         : {}".format(message.get("To")))
        print("Bcc        : {}".format(message.get("Bcc")))
        print("Date       : {}".format(message.get("Date")))
        print("Subject    : {}".format(message.get("Subject")))

        print("Body : ")

        for part in message.walk():
            print(part.get_content_type())
            if part.get_content_type() == "text/html":
                file1 = open("otp.txt",'w')
                file1.write(str(part))
                file1.close()
        break




            # if part.get_content_type() == "text/plain":
            #     body_lines = part.as_string().split("\n")
            #     print("\n".join(body_lines[:12])) ### Print first 12 lines of message


    print("================== End of Mail [{}] ====================\n")

    ############# Close Selected Mailbox #######################
    print("\nClosing selected mailbox....")
    imap_ssl.close()
