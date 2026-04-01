#Nombre: Rosmery Aruni Paye RU: 200075568
from flask import Flask
app = Flask(__name__)
@app.route('/')
def inicio():
    return "<h1>Pagina de inicio</h1>"
@app.route('/acerca-de')
def acerca_de():
    return "<h1>Informacion de nosotros</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Pagina de contacto</h1>"

@app.route('/info')
@app.route('/informacion')
@app.route('/about')
def informacion():
    return "<h1>Pagina de Informacion</h1>"

if __name__ == '__main__':
    app.run(debug=True)