from flask import Flask
from flask import render_template, redirect, flash, url_for
from chatroom import ChatForm
from index import CreateRoomForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a'


log = dict()
def get_room_msgs(dic, name):
    if name not in dic:
        dic[name] = list()
    return dic[name]

def add_msg_to_room(dic, name, l):
    if name not in dic:
        dic[name] = list()
    dic[name].append(l)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/index', methods=['GET', 'POST'])
def index():

    form = CreateRoomForm()
    if form.room_name.data in form.rooms:
        flash("already exists")
    else:
        if form.room_name.data not in ("", None):
            form.rooms.append(form.room_name.data)
    return render_template('index.html', title='Home', form=form)


@app.route('/chatroom/<name>', methods=['GET', 'POST'])
def chatroom(name):
    form = ChatForm()


    if form.message.data not in ("", None):
        add_msg_to_room(log, name, form.message.data)
        redirect('/chatroom/<name>')

    out = get_room_msgs(log, name)

    return render_template('chatroom.html', title='Chatroom: ' + name, form=form, name=name, out=out)


# EOF
