from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class ChatForm(FlaskForm):
    all_messages = list()
    name = ""
    message = StringField("your message")
    send = SubmitField("Send")

