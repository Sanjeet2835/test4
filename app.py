from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime

app = Flask(__name__)


# route for home page 
@app.route('/home')  
def home():
    return render_template('index.html') 

@app.route('/')  
def homee():
    return render_template('index.html') 


# Set a strong secret key for session management
app.secret_key = 'your_strong_secret_key'  # Replace with a strong secret key

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# In-memory user storage
users = {}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, username):
        self.id = username

# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in users else None

# Route for user signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        if username in users:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('signup'))

        # Save new user
        users[username] = {'password': password, 'entries': []}
        flash('Signup successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Authenticate user
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('journal'))
        flash('Invalid username or password', 'danger')

    return render_template('login.html')

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

# Journal route for logged-in users
@app.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST':
        entry_content = request.form['entry']
        
        # Create a new journal entry
        new_entry = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'content': entry_content
        }
        users[current_user.id]['entries'].append(new_entry)
        flash('Entry saved!', 'success')
        return redirect(url_for('journal'))

    entries = users[current_user.id]['entries']
    return render_template('journal.html', entries=entries)





@app.route('/motivational-quotes')
def motivational_quotes():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it."
    ]
    return render_template('motivationalquotes.html', quotes=quotes)

@app.route('/audio-library')
def audio():
    return render_template('audio.html')

@app.route('/get-started')
def get_started():
    return render_template('neura.html')  # This is the page after clicking "Get Started"

@app.route('/neura')
def neurafinal():
    return render_template('neurafinal.html')

@app.route('/emergencyhelp')
def emergency():
    return render_template('emergency.html')

#route for login page
# @app.route('/login', methods= ['GET','POST'])
# def login():
   # if request.method=='POST':
   #     username = request.form.get('username')
   #     password =request.form.get('password')

if __name__=='__main__':
    app.run(host='neura.local', debug=True, port=7777)