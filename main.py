from flask import Flask, render_template
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


# if __name__ == '__main__':
app.run(debug=True)
