from flask import render_template
from app import app
from .models import User
from .models import Text

@app.route('/')
@app.route('/index')
def index():
    user = User.query.get(1)
    texts = Text.query.filter(Text.user_id == user.id)
    return render_template("index.html",
                           title='Home',
                           user=user,
                           texts=texts)

