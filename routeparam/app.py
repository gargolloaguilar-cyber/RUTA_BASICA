#Nombre: Rosmery Aruni Paye RU: 200075568
from flask import Flask

app = Flask(__name__)

@app.route('/usuario/<nombre>')
def perfil_usuario(nombre):
    return f'Perfil de: <strong>{nombre}</strong>'
@app.route('/post/<id>')
def mostrar_post(id):
    return f'mostrando el post: <strong>{id}</strong>'

@app.route('/categoria/<categoria>/<producto>')
def productos(categoria, producto):
    return f'Categoria: <strong>{categoria}</strong>, Producto: <strong>{producto}</strong>'


if __name__ == '__main__':
    app.run(debug=True)