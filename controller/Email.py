from flask_mail import Message

from extensions import mail
from config import app_active, app_config
config = app_config[app_active]

class EmailController():
    def send_email(self, t_email, subject, content_text, f_email=None):
        try:
            message = Message(
                subject=subject,
                recipients=[t_email],
                html=content_text,
                sender=f_email or config.MAIL_DEFAULT_SENDER
            )
            mail.send(message)

            return {
                'status_code': 200,
                'body': 'E-mail enviado com sucesso'
            }
        except Exception as e:
            print(e)
            raise e
