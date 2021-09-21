from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = "super-secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/apna_bank'

db = SQLAlchemy(app)


# db model
class Customer(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    current_balance = db.Column(db.Integer, nullable=False)


class Transfer(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String, nullable=False)
    receiver_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/transfer", methods=['GET'])
def transfer_details():
    data = Customer.query.filter_by().all()
    jatin = Customer.query.filter_by(sno='1').first()

    return render_template('index.html', data=data, jatin=jatin)


@app.route("/user", methods=['GET', 'POST'])
def user_page():
    if request.method == 'POST':
        receiver = 0
        amount = 0
        receiver = request.form.get('receiver')
        jj = receiver
        amount = request.form.get('amount')
        data = Customer.query.filter_by(email=jj).first()
        sender = Customer.query.filter_by(sno='1').first()
        data.current_balance += int(amount)
        sender.current_balance -= int(amount)

        transfer = Transfer(sender_name=(sender.first_name + " " + sender.last_name),
                            receiver_name=(data.first_name + " " + data.last_name), email=sender.email,
                            amount=int(amount), date=datetime.now())
        db.session.add(transfer)
        db.session.commit()
        return redirect('/transfer')
    return render_template('user.html')


@app.route("/history", methods=['GET', 'POST'])
def transaction_history():
    history = Transfer.query.filter_by().all()
    return render_template('history.html', history=history)


app.run(debug=True)
