import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(toMail, subject, content):

    fromMail = "your-email"
    server = smtplib.SMTP("smtp.gmail.com",587)

    server.ehlo()
    server.starttls()
    server.login(fromMail, "gmail-password")

    message = MIMEMultipart('alternative')
    message['Subject']= subject

    htmlContent = MIMEText(content, 'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    print("Email sent!")

    server.quit()