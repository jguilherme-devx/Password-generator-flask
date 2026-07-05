from flask import Flask, render_template, request
import secrets
import string

caracteres_simples = string.ascii_letters

caracteres_medio = string.ascii_letters + string.digits

caracteres_forte = string.ascii_letters + string.digits + string.punctuation

def simples():
    senha_simples = ''.join(secrets.choice(caracteres_simples) for _ in range(12))
    return senha_simples

def medio():
    senha_media = ''.join(secrets.choice(caracteres_medio) for _ in range(12))
    return senha_media

def forte():
    senha_forte = ''.join(secrets.choice(caracteres_forte) for _ in range(24))
    return senha_forte


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', post=False)


@app.route('/', methods=['POST'])
def submit():
    tipo = request.form['botao']

    if tipo == "simples":
        senha = simples()

    elif tipo == "medio":
        senha = medio()

    else:
        senha = forte()

    return render_template('index.html', post=True, senha=senha)


if __name__ == '__main__':
    app.run(debug=True)
