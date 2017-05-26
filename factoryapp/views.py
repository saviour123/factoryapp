from .main import app

@app.route('/')
def index():
    return render_template('layout.html')
