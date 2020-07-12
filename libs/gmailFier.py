from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmail(messageHeader, receipientEmail, body):
    CLIENT_SECRET_FILE = 'credentials.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/']
    
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    emailMsg = body
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = receipientEmail
    mimeMessage['subject'] = messageHeader
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
    
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print(message)
