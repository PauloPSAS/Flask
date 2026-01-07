from meu_projeto import app
from flask import render_template, url_for

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contatos/")
def novapag():
    return "Outra view!"