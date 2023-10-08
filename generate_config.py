import json
if __name__ == '__main__':
    config = {
        "MAIL_SERVER": "localhost", # or "smtp.gmail.com" for example
        "MAIL_PORT": 465, # or 587 for example
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": False,
        "MAIL_USERNAME": "",
        "MAIL_PASSWORD": "",
        "MAIL_TO": [""],
        "MAIL_SUBJECT_PREFIX": None, # or "Message via WebApp - " for example
        "MAIL_DISPLAY_NAME": None # or "WebApp Mailer" for example
    }

    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)