# BOTCripto\app\forms\forms.py
import json
import os
from flask import redirect, url_for, request, render_template

def load_endpoints_data():
    file_path = 'app/pares/endpoint.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    return []

def process_create_endpoint_form():
    file_path = 'app/pares/endpoint.json'  # Mova esta linha para cá
    if request.method == 'POST':
        # Processar os dados do formulário
        exchange = request.form.get('exchange')
        base_point = request.form.get('base_point')
        endpoints = request.form.get('endpoints')
        observation = request.form.get('observation')

        # Montar o objeto JSON
        endpoint_data = {
            'exchange': exchange,
            'base_point': base_point,
            'endpoints': endpoints,
            'observation': observation
        }

        # Carregar dados existentes do arquivo
        data = load_endpoints_data()

        # Adicionar os novos dados à lista
        data.append(endpoint_data)

        # Gravar os dados no arquivo JSON
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

        # Redirecionar para a página principal ou outra página desejada
        return redirect(url_for('main.create_endpoint'))

    # Se a solicitação for GET, renderizar o formulário e os dados da tabela
    endpoints = load_endpoints_data()
    return render_template('bots/create_endpoint.html', endpoints=endpoints)
