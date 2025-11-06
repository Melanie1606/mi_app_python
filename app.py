from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, soy Melanie y este es mi contenedor corriendo correctamente 🎉"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
