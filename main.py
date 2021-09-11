from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

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


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/transfer")
def transfer_details():
    data = Customer.query.filter_by().all()

    return render_template('transfer.html', data=data)


@app.route("/user")
def user_page():
    data = Customer.query.filter_by().all()

    return render_template('user.html', data=data)


@app.route("/transaction", methods=['GET', 'POST'])
def transaction(debit):
    if request.method == 'POST':
        debit = request.form.get('debit')
        credit = request.form.get('credit')
        amount = request.form.get('amount')

        data = Customer.query.filter_by(debit=debit).first()
        data1 = Customer.query.filter_by(credit=credit).first()


# if __name__ == '__main__':
app.run(debug=True)
