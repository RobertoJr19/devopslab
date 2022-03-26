from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - RRibeiro - FIAP"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0',  port=port)