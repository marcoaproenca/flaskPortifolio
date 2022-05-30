from flask import Flask, render_template

app = Flask(__name__)

# route    -> pagina do site / caminho após o endereço do site. Ex: wwww.uol.com.br/login
# Função   -> o que vc quer exibir na pagina
# template -> Arquivo HTML da pagina. Criar a pasta templates

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario = nome_usuario)

if __name__ == "__main__":
    app.run(debug=True)