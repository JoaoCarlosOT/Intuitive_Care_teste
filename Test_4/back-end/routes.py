from flask import Blueprint, jsonify
from data_handler import load_data

# Criando um Blueprint para as rotas
bp = Blueprint('api', __name__)

# Rota para retornar todos os dados do CSV
@bp.route('/operadoras', methods=['GET'])
def get_operadoras():
    # Carregar os dados
    dados = load_data()
    
    # Se ocorrer algum erro ao carregar os dados
    if dados is None:
        return jsonify({'erro': 'Erro ao carregar os dados.'}), 500
    
    # Retornar todos os dados no formato JSON
    return jsonify(dados)
