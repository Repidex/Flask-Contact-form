from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from datetime import datetime

app =Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql://root:@localhost/repidexdb"
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name =db.Column(db.String(20), nullable=False)
    phone_num =db.Column(db.String(12), nullable=False) 
    msg =db.Column(db.String(100), nullable=False)
    date =db.Column(db.String(12), nullable=True)
    email =db.Column(db.String(20), nullable=False)


@app.route("/", methods=['GET','POST'])
def contact(): 
    if(request.method == 'POST'):
    #ADD entry to the database
        name =request.form.get('name')
        email =request.form.get('email')
        phone =request.form.get('phone')
        message =request.form.get('message')
        entry = Contacts(name=name, phone_num = phone, date=datetime.now(),email=email, msg=message)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")   

if __name__ == '__main__':
    app.run(debug = True)