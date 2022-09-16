# Import the SMTP = simple mail transport protocol to sent email
import email.utils
import smtplib
# Import MIME text format library. MIME - Multipurpose Internet Mail Extension, its an internet standard we follow to encode email contenets, like attachments, pictures, links and text etc
from email.mime.text import  MIMEText

# which email is this being sent from
sender_email='supine.me@gmail.com'
sender_name="Jawad"

# Passwod so we can log in to the senders account and send the email
password="xiaq olqr hger mgyz"
# Who is this email going to be sent to
recipient_email= "hdr.jawad96@gmail.com"
# we can use a list of emails as well...
recipient_name="Haider"

# Messge body
# email_text='''\
# From: supine.me@gmail.com
# Subject: This is a subjet
#
# Hi Haider,
# Yo what's up. Hope you got back from your trip.
# let me know when you are ready for the meeting. see you at the club:)
#
#
# regards,
# Jawad Haider
# '''
email_text='''
New Dummy text. We are following industry email standards and protocols.
'''
# Our function
def send_email():
    print("Sending email")
    # get message ready in email format
    message=MIMEText(email_text)
    # print(type(message))
    # print(message)
    message['To']= email.utils.formataddr((recipient_name,recipient_email))
    message['From']=email.utils.formataddr((sender_name,sender_email))
    message['Subject']= 'NOT SPAM. '
    # set up the email server. gmail host, and use a common port
    server=smtplib.SMTP('smtp.gmail.com',587)

    # Start the TLS layer to enable the encryption of data
    server.starttls()
    # Login to the senders email account
    server.login(sender_email, password)

    # Email header
    # send the email
    # server.sendmail(sender_email,recipient_email, email_text)
    print(message.as_string())
    server.sendmail(sender_email, recipient_email, message.as_string())
    # clean up
    server.quit()
    print("Email sent :)")


# call our code to send the emails
send_email()