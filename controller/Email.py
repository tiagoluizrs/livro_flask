import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from config import app_active, app_config
config = app_config[app_active]

class EmailController():
    def send_email(self, t_email, subject, content_text, f_email="contato@site.com.br"):
        message = Mail(
            from_email=f_email,
            to_emails=t_email,
            subject=subject,
            html_content=content_text)
        try:
            sg = SendGridAPIClient(config.SENDGRID_API_KEY)
            response = sg.send(message)
            
            print(response.status_code)
            print(response.body)
            print(response.headers)

            return {
                'status_code' : response.status_code,
                'body' : response.body,
                'headers' : response.headers
            }
        except Exception as e:
            print(e.message)
            raise e
        
        