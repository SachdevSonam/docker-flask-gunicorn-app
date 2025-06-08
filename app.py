from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello from Flask + gunicorn!"

@app.route('/api')
def api():
    return{"message": "This is API endpoint"}
    
	
	