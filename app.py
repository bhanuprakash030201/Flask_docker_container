# app.py

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask inside Docker!"

@app.route('/index', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        user_input = request.form.get('message')
        message = f'You entered: {user_input}'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
