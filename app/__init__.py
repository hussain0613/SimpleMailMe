import json

from flask import Flask, request, jsonify, Response

from app.models.email import SMTPClient, MultipartMessage


CONFIG: dict
with open('config.json', 'r') as f:
    CONFIG = json.load(f)


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/send/', methods=['POST'])
def send():
    if not request.is_json:
        return 'Bad request', 400
    
    for key in ['name', 'subject', 'email', 'message']:
        if key not in request.json:
            return 'Bad request', 400
    

    mail_sender: str = CONFIG["MAIL_USERNAME"]
    if CONFIG.get("MAIL_DISPLAY_NAME", None):
        mail_sender = f"{CONFIG['MAIL_DISPLAY_NAME']} <{mail_sender}>"
    
    mail_subject: str = " - ".join([CONFIG.get("MAIL_SUBJECT_PREFIX", "Message via WebApp"), request.json['subject']])
    
    
    multipart_message = MultipartMessage(
        subject= mail_subject,
        sender= mail_sender,
        recipients=CONFIG['MAIL_TO']
    )

    multipart_message.message['Reply-To'] = request.json['email']
    
    email_body: str = ""
    for key in request.json:
        email_body += f"\n{key.capitalize()}: {request.json[key]}"

    multipart_message.attach_text(email_body)


    smtp_client = SMTPClient(CONFIG)
    smtp_client.send_message(multipart_message.message)


    return Response(status=204)
