from email.message import EmailMessage
import smtplib
import ssl

sender_email = "YOUR_EMAIL" #enter email
sender_password = "YOUR_APP_PASS" #enter password
reciever_email = "RECIEVER_EMAIL" #temp mail

email_subject = "MAIL_SUBJECT"
email_body = "MAIL_CONTENT"

eMail = EmailMessage()
eMail["From"] = sender_email
eMail["To"] = reciever_email
eMail["Subject"] = email_subject
eMail.set_content(email_body)

mainContext = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = mainContext) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, reciever_email, eMail.as_string())