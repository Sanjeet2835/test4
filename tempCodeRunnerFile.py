from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# route for home page 
@app.route('/')  
def home():
    return render_template('index.html') 

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


#route for login page
# @app.route('/login', methods= ['GET','POST'])
# def login():
   # if request.method=='POST':
   #     username = request.form.get('username')
   #     password =request.form.get('password')

if __name__=='__main__':
    app.run(host='neura.local', debug=True, port=7777)