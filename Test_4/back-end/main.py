from flask import Flask
from routes import bp

# Inicializando o Flask
app = Flask(__name__)

# Registrando o Blueprint de rotas
app.register_blueprint(bp)

# Rodando a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
