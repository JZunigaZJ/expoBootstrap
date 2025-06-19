from flask import Flask,redirect, url_for, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Registro')
def registro():
    return render_template('registro.html')

@app.route('/Contactenos')
def contactenos():
    return render_template('contactenos.html')

@app.route('/Nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/Casa1')
def primeraCasa():
    return render_template('casa1.html')

@app.route('/Casa2')
def segundaCasa():
    return render_template('casa2.html')

@app.route('/Casa3')
def terceraCasa():
    return render_template('casa3.html')

@app.route('/Casa4')
def cuartaCasa():
    return render_template('casa4.html')

@app.route('/Casa5')
def quintaCasa():
    return render_template('casa5.html')

@app.route('/Casa6')
def sextaCasa():
    return render_template('casa6.html')

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')