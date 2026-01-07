# Meu Aprendizado em Flask

Este README é um registro do que eu aprendo sobre Flask e desenvolvimento web em Python.  
Cada nova coisa que eu aprender pode ser adicionada aqui, junto com exemplos e explicações.

---

## Sumário

1. [Introdução ao Flask](#introdução-ao-flask)  
2. [Render Template](#render-template)
3. [Estrutura de Rotas](#estrutura-de-rotas)
4. [Links e `url_for`](#links-e-url_for)
5. [Passando Dados do Servidor](#passando-dados-do-servidor)

---

## Introdução ao Flask

Flask é um micro-framework em Python para desenvolvimento web.  
Ele permite criar servidores, rotas, templates e APIs de forma rápida e simples.

Exemplo básico:

```python
from flask import Flask, url_for, render_template

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
<h1>Olá, {{nome}}!</h1>
```

- O navegador verá algo como: `Olá, João`, substituindo a variável `nome`.

---

## Estrutura de Rotas

No Flask, uma rota é um caminho que o servidor responde.
Cada rota é associada a uma função Python, que decide o que será retornado.
`@app.route("/")` está associado a função `home()`e `@app.route("/sobre/")`está associado a função `sobre()`

---

## Links e `url_for`

O `url_for`é a forma recomendada de criar links internos para suas rotas.
Ele gera a URL dinâmicamente a partir do nome da função, ao invés de depender de um caminho fixo.

### Por quê usar `url_for`?

- **Dinâmico**: Se você mudar a rota no código, os links não quebram.
- **Seguro**: Evita apontar para URLs erradas ou externas acidentalmente.
- **Flexível**: Permite passar parâmetros de rota facilmente.

---

## Passando Dados do Servidor

- ### O que acontece no Flask?

O Flask funciona de forma semelhante ao padrão **MVC (model – view – controller)**.

- **Servidor (Flask/Python)** \- prepara os dados.
- **Template (HTML + Jinja2)** \- exibe os dados.
- **Rota(`@app.route`)** \- conecta o navegador ao servidor.

O HTML não reconhece o Python. Quem envia os dados para o HTML é o FLASK, usando `render_template`.

Forma mais simples de passar dados:

```python
@app.route("/")
def home():
    usuario = "usuario 1"
    idade = 27
    return render_template("index.html", usuario=usuario, idade=idade)
```

No `index.html`:

```html
<p>Bem vindo {{ usuario }} à aula de Flask!</p>
<p><strong>Idade</strong>: {{ idade }}</p>
```

O que tá acontecendo:

- `usuario=usuario` cria uma variável no template.
- `idade=idade` cria outra variável.
- `{{}}` é a sintaxe **Jinja2** para exibir dados.

**Boa prática**: usar um contexto (dicionário)

```python
@app.route("/")
def home():
    context = {
        "usuario": "usuario 1",
        "idade": 27
    }
    return render_template("index.html", context=context)
```

Agora como tudo está dentro do dicionário usamos o `context`:

```html
<p>Bem vindo {{ context.usuario }} à aula de Flask!</p>
<p><strong>Idade</strong>: {{ context.idade }}</p>
```

Também funciona: `{{ context["usuario"] }}`. Porém a notação com ponto é mais usada.

---
