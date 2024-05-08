from flask import Flask, render_template, request, redirect, session, url_for
import requests
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# User data stored in memory for demonstration. Replace with a database in a real application.
users = {'username': 'password'}  # Storing hashed passwords for security.

# Replace 'YOUR_API_KEY' with your actual Open Exchange Rates API key
API_KEY = '5a96da934f-3d98927201-sd4x8o'

# Endpoint for the Open Exchange Rates API
BASE_URL = 'https://open.er-api.com/v6/latest/'


def validate_currency_code(currency_code):
    # Perform basic validation for currency codes
    if not currency_code.isalpha() or len(currency_code) != 3:
        return False
    return True


def validate_amount(amount):
    # Perform validation for the amount
    try:
        float(amount)
        return True
    except ValueError:
        return False


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'Username already exists. Please choose a different username.'
        hashed_password = hash_password(password)
        users[username] = hashed_password
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        if username in users and users[username] == hashed_password:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password. Please try again.'
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/')
def index():
    if 'logged_in' in session:
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/convert', methods=['POST'])
def convert():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    from_currency = request.form['from_currency'].upper()
    to_currency = request.form['to_currency'].upper()
    amount = request.form['amount']

    # Validate input data
    if not (validate_currency_code(from_currency) and validate_currency_code(to_currency) and validate_amount(amount)):
        return 'Invalid input data.'

    # Make a request to the Open Exchange Rates API to get latest exchange rates
    response = requests.get(f'{BASE_URL}{from_currency}?apikey={API_KEY}')

    if response.status_code == 200:
        data = response.json()

        if 'rates' in data:
            conversion_rate = data['rates'].get(to_currency)
            if conversion_rate is not None:
                converted_amount = float(amount) * conversion_rate
                return render_template('result.html', from_currency=from_currency, to_currency=to_currency,
                                       amount=amount, converted_amount=converted_amount)
            else:
                return 'Invalid currency code.'
        else:
            return 'Invalid currency code.'
    else:
        return 'Error accessing currency conversion API.'


if __name__ == '__main__':
    app.run(debug=True)

