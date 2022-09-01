from flask import Flask, redirect,url_for

app = Flask(__name__, static_folder='static')

@app.route("/add", methods=["GET"])
def add():
    return "Mini Homebroker"

@app.route("/comprar")
def comprar():
    return "Compra de ativo"

@app.route("/vender")
def vender():
    return "Venda de ativo"

@app.route("/pesquisar")
def pesquisar():
    return "Tela de pesquisa"

if __name__ =='__main__':
    app.run(debug=True)