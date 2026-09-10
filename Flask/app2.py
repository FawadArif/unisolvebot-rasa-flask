from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            return render_template('register.html', email_error="Email is already registered.")
        
        if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'[!@#$%^&*]', password):
            flash("Password must be at least 8 characters long, contain a capital letter and a symbol.")
            return render_template('register.html')

        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            session['name'] = user.name
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid email or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        return redirect('/login')
    name = session.get('name')
    return render_template('dashboard.html', name=name)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('name', None)
    return redirect('/login')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data['message']

    # Replace with your Rasa server URL
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    response = requests.post(rasa_url, json={"sender": "user", "message": message})

    bot_response = response.json()
    if bot_response:
        return jsonify({"response": bot_response[0]['text']})
    else:
        return jsonify({"response": "Sorry, I didn't understand that."})

@app.route('/privacypolicy')
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/termsofservices')
def termsofservices():
    return render_template('termsofservices.html')

if __name__ == '__main__':
    app.run(debug=True)
