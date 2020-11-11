from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Senha.12345!@localhost/campeonatoesportivo'
db = SQLAlchemy(app)

class campeonatoesportivo(db.Model):
    __tablename__ = 'cadastro'
    _id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(14))
    email = db.Column(db.String(50))
    sexo = db.Column(db.String(9))
    data_nascimento = db.Column(db.String(10))
    def __init__(self, nome, telefone, email, sexo, data_nascimento):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.data_nascimento = data_nascimento

db.create_all()


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/detalhe")
def detalhe():
    return render_template("detalhe.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nnome"))
        telefone = (request.form.get("ntelefone"))
        email = (request.form.get("nemail"))
        sexo = (request.form.get("nsexo"))
        data_nascimento = (request.form.get("nnascimento"))
        if nome:
            f = campeonatoesportivo(nome,telefone,email,sexo,data_nascimento)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@app.route("/listar")
def listar():
    valor = campeonatoesportivo.query.all()
    return render_template("listar.html", campeonatoesportivo=valor)

if __name__ == "__main__":
    app.run(debug=True)
