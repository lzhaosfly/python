# Email related

## 0. set up email

**Make sure you open the POP3/SMTP/IMAP set up for your mail!**


## 1. sending email

```python
import os
import mimetypes
import smtplib
from email.message import EmailMessage

MAIL_USER = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

msg = EmailMessage()
msg['Subject'] = 'This is test Subject'
msg['From'] = MAIL_USER
# Note, this way will use alias
msg['To'] = ['Lei1<leizhaotest@126.com>', 'Lei2<zhao434@usc.edu>']

msg.set_content("""
Hello,
This is email body, 回顾
""")

# msg.add_alternative("""
#         <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
#             recipie
#         </a> 
# """, subtype='html')

with open('./enumTest.py', 'rb') as file:
    file1 = file.read()
    ctype, encoding = mimetypes.guess_type('./enumTest.py')
    print(ctype)
    maintype, subtype = ctype.split('/', 1)
    msg.add_attachment(file1, maintype=maintype,
                       subtype=subtype, filename='enumTest.py')

try:
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(user=MAIL_USER, password=MAIL_PASSWORD)
    s.send_message(msg)
except Exception as error:
    print(error)
finally:
    s.quit()
```

Note:

-   With python 3.6 or later, we can use `EmailMessage`
-   When connect SMTP, please use `smtplib.SMTP_SSL('smtp.gmail.com', 465)`, do not use others!!!
-   For address, you can use `alias<email>` to represent alias for an email
-   If just simple text, then use `msg.set_content`
-   If it's html file, then use `msg.add_alternative([html], subtype='html')`
-   If you want to attach a file, then you need to check the above example. Using `msg.add_attachment(file, maintype=maintype, subtype=subtype, filename=filename)`
-   Make sure you quit the mail finally

## 2. Imap

```python
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
    email_message = email.message_from_bytes(message_data[b'RFC822']) # [Message object](https://docs.python.org/3/library/email.compat32-message.html#module-email.message)
    print(email_message.get('subject'))  # get subject
    print(email_message.get_payload())  # get body

# imapObj.delete_messages(UIDs) # delete
```

Note:

-   Search keys:
    1. `'ALL'`
    2. `'BEFORE date'`, `'ON date'`, `'SINCE date'`
    3. `'SUBJECT string'`, `'BODY string'`, `'TEXT string'`
    4. `'FROM string'`, `'TO string'`, `'CC string'`, `'BCC string'`
    5. `'SEEN'`, `'UNSEEN'`
    6. `'ANSWERED'`, `'UNANSWERED'`
    7. `'DELETED'`, `'UNDELETED'`
    8. `'DRAFT'`, `'UNDRAFT'`
    9. `'FLAGGED'`, `'UNFLAGGED'`
    10. `'LARGER N'`, `'SMALLER N'` Returns all messages larger or smaller than N bytes
    11. `'NOT search-key'` Returns the messages that search-key would not have returned
    12. `'OR search-key1 search-key2'` Returns the messages that match either the first or second search-key.

- You can use `imaplib._MAXLINE = 10000000` limits 10000000 bytes