from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_cursor():
    db = sqlite3.connect("bot.db")
    return db.cursor()

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/asistencia", methods=["GET"])
def asistencia():

    cur = get_cursor()

    asistencia = cur.execute("SELECT * FROM asistencia").fetchall()

    cur.close()
        
    return render_template("asistencia.html", asistencia = asistencia)

@app.route("/sobre_nosotros", methods=["GET"])
def sobre_nosotros():
    return render_template("sobre_nosotros.html")

@app.route("/comandos", methods=["GET"])
def comandos():
    return render_template("comandos.html")