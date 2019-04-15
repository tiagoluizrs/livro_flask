import sendgrid
from sendgrid.helpers.mail import *

from config import app_active, app_config
config = app_config[app_active]

class EmailController():
    def __init__(self):
        self.content_type = {
            "text": "text/plain",
            "html": "text/html"
        }

    def send_email(self, t_email, subject, content_text, f_email="contato@site.com.br", c_type='text'):
        try:
            sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)
            from_email = Email(f_email)
            to_email = Email(t_email)
            
            content = Content(self.content_type[c_type], content_text)
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            
            return {
                'status_code' : response.status_code,
                'body' : response.body,
                'headers' : response.headers
            }
        except Exception as e:
            print(e)
            raise e
        
        