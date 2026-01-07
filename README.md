# Meu Aprendizado em Flask

Este README é um registro do que eu aprendo sobre Flask e desenvolvimento web em Python.  
Cada nova coisa que eu aprender pode ser adicionada aqui, junto com exemplos e explicações.

---

## Sumário

1. [Introdução ao Flask](#introdução-ao-flask)  
2. [Render Template](#render-template)

---

## Introdução ao Flask

Flask é um micro-framework em Python para desenvolvimento web.  
Ele permite criar servidores, rotas, templates e APIs de forma rápida e simples.

Exemplo básico:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre/")
def sobre():
    return "página Sobre"


if __name__ == "__main__":
    app.run(debug=True)
```

---

## Render Template

No Flask, usamos `render_template` para servir arquivos HTML completos ao invés de retornar apenas strings.

```python
@app.route("/")
def home():
    return render_template("index.html")
```

Por quê usar `render_template`:
1. Flask procura o arquivo dentro de `templates/`.
2. Permite separar o HTML do Python, isso mantém o código organizado.
3. Permite passar variáveis dinâmicas para o template:
```python
@app.route("/user/<nome>/")
def user(nome):
    return render_template("index.html", nome=nome)
```
No HTML(`index.html`):
```html
<h1>Olá, {{ nome }}!</h1>
```
- O navegador verá algo como: `Olá, João`, substituindo a variável `nome`.