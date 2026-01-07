from meu_projeto import app
from flask import render_template, url_for

@app.route("/")
def home():
    usuario = "usuario 1"
    idade = 27

    context = {
        "usuario": usuario,
        "idade": idade
    }
    return render_template("index.html", context=context)


@app.route("/sobre/")
def sobre():
    return "Página Sobre"