from flask import Flask, render_template, request, jsonify, flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = ''  # Use your actual Gmail address
app.config['MAIL_PASSWORD'] = ''  # Use your generated App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/message', methods=['GET', 'POST'])
def message():
    global email, name, message
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        message = request.form.get('message')

    msg = Message(
        subject=f'Message from {name}',
        sender='should_match_mail_username',
        recipients=['mail_reciever']
    )
    msg.body = f"Email Address of sender: {email}\n\n Name of sender: {name}\n\n Message from sender: {message}"

    mail.send(msg)
    return "<script>alert('✅ Email sent successfully!'); window.history.back();</script>"

if __name__ == '__main__':
    app.run(debug=True)
