# Import the SMTP = simple mail transport protocol to sent email
import smtplib

# which email is this being sent from
sender_email='supine.me@gmail.com'
# Passwod so we can log in to the senders account and send the email
password="xiaq olqr hger mgyz"
# Who is this email going to be sent to
recipient_email= "hdr.jawad96@gmail.com"
# Messge body
email_text='''
Dummy text. you wqhat's up.
'''
# Our function
def send_email():
    # setup the email server. gmail host, and use a common port
    server=smtplib.SMTP('smtp.gmail.com',587)

    # Start the TLS layer to enable the encryption of data
    server.starttls()
    # Login to the senders email account
    server.login(sender_email, password)

    # send the email
    server.sendmail(sender_email,recipient_email, email_text)
    # clean up
    server.quit()


# call our code to send the emails
send_email()