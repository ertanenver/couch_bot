import smtplib

gmail_user = 'TgBotTmb@gmail.com'
gmail_password = 'qjmg sbqo pila tztj'

sent_from = gmail_user
to = ['soshinyaa73@gmail.com', '89156721778v@gmail.com']
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    return 'successfully sent the mail'
    
print(send_email(gmail_user,gmail_password,to,'subject','body'))

import smtplib

# Define your SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # For use with the STARTTLS command

# Define your email credentials
username = 'TgBotTmb@gmail.com'
password = 'qjmg sbqo pila tztj'

# Define your email content
from_address = 'TgBotTmb@gmail.com'
to_address = 'soshinyaa73@gmail.com'
subject = 'Test Email'
body = 'This is a test email.'

message = f'Subject: {subject}\n\n{body}'

# Create a secure SMTP connection
server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(username,password)
server.sendmail(from_address, to_address, message)
server.quit()

