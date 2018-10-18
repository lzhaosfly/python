import os
from imapclient import IMAPClient
import email

MAIL_USER = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

imapObj = IMAPClient('imap.gmail.com', use_uid=True)
imapObj.login(MAIL_USER, MAIL_PASSWORD)
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['ON', '17-Oct-2018', 'SEEN'])

# [28342, 28343, 28344, 28348, 28350, 28357, 28358, 28365, 28366, 28367, 28368]
print(UIDs)

for msgid, message_data in imapObj.fetch(UIDs[-2], ['RFC822']).items():
    email_message = email.message_from_bytes(message_data[b'RFC822'])
    print(email_message.get('subject'))  # get subject
    print(email_message.get_payload())  # get body

# imapObj.delete_messages(UIDs) # delete
