from app import create_app
from config import app_config, app_active

config = app_config[app_active]
config.APP = create_app(app_active)

# alias usado pelo comando `flask` (CLI) para descobrir a aplicação,
# por exemplo no comando `flask run`.
app = config.APP

if __name__ == '__main__':
    app.run(host=config.IP_HOST, port=config.PORT_HOST)
