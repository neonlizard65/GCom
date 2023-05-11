from flask import Flask, render_template, Request, Response, request, redirect, jsonify
from datetime import datetime
from flask_migrate import Migrate
import models
from models import Dogovor, Manager, Request, Tariff, User
from connection import db
from os import listdir
from os.path import isfile, join
import string
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://aleksei:123@localhost/gcom"
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def index2():
    return redirect("/")

@app.route("/home")
def index3():
    return redirect("/")

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/licenses")
def licenses():
    return render_template("licenses.html")

#Database
@app.route("/documents")
def documents():
    doc_path = "static/res/documents"
    doc_files = [f for f in listdir(doc_path) if isfile(join(doc_path, f))]
    print(doc_files)
    return render_template("documents.html", docs = doc_files)

@app.route("/requisites")
def requisites():
    return render_template("requisites.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/to_condo")
def to_condo():
    tariffs = db.session.query(Tariff).filter_by(type="В квартиру")  
    return render_template("to_condo.html", tariffs = tariffs)

@app.route("/to_house")
def to_house():
    tariffs = db.session.query(Tariff).filter_by(type="В дом")  
    return render_template("to_house.html", tariffs = tariffs)

@app.route("/to_office")
def to_office():
    tariffs = db.session.query(Tariff).filter_by(type="В офис")  
    return render_template("to_office.html", tariffs = tariffs)

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/request")
def a_request():
    return render_template("request.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cabinet")
def cabinet():
    return render_template("cabinet.html")

@app.route("/get/tariffs")
def get_tariffs():
    return jsonify(db.session.query(Tariff).all())

@app.route("/handle_request", methods = ["POST"])
def handle_request():
    if request.method == "POST":
        fio = request.form["fio"]
        adress = request.form["adress"]
        phone = request.form["phone"]
        tariffid = request.form["tariff"]
        additional = request.form["additional"]
        new_client = models.User(name=fio, password=generate_password(), address = adress, number = phone, balance = 0)
        db.session.add(new_client)
        db.session.commit()
        new_request = models.Request(clientid = new_client.id, tariffid = tariffid, date = datetime.now(), additional = additional)
        db.session.add(new_request)
        db.session.commit()
        return redirect("handled")
    return Response("Ошибка на стороне сервера", status=500)
def generate_password():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(10))
    return result_str

@app.route("/handled")
def handled():
    return render_template("handled.html")