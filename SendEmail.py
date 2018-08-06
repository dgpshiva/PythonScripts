import smtplib
from email.mime.text import MIMEText
import sys

msg = MIMEText(sys.argv[4])
msg['Subject'] = sys.argv[3]
msg['From'] = sys.argv[1]
msg['To'] = sys.argv[2]

s = smtplib.SMTP('mail.slb.com')
s.sendmail(sys.argv[1], sys.argv[2], msg.as_string())
s.quit()
exit(0)