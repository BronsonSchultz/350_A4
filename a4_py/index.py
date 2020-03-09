from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class CreateRoomForm(FlaskForm):
    rooms = list()
    room_name = StringField("your message")
    create = SubmitField("Create")

