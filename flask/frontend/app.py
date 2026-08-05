from flask import Flask, render_template, request
import requests

BACKEND_URL = "http://0.0.0.0:9000"
app = Flask(__name__)

@app.route('/')
def home():
    print("Hi! welcome to the Flask app.")
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    form_data = request.form.to_dict()
    requests.post(BACKEND_URL + '/register', json=form_data)
    return ("Data submitted successfully")

@app.route('/submittodoitem', methods=['POST'])
def todo():
    form_data = request.form.to_dict()
    requests.post(BACKEND_URL + '/submittodoitem', json=form_data)
    return ("todo list created successfully")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)