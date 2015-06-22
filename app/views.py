from app import app
# both these urls route to this function
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
