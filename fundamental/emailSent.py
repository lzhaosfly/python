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

Best,
Lei
""")

msg.add_alternative("""
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
            recipie
        </a>
""", subtype='html')

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
