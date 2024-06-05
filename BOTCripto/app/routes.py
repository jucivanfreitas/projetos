# app/routes.py
from flask import Blueprint, render_template, jsonify, session, redirect, request, url_for,flash
from .auth import bp as auth_bp
import json
import os
from .forms.forms import process_create_endpoint_form  # Adicione esta importação



main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/check_auth')
def check_auth():
    # Verifique se o usuário está autenticado
    if 'user' in session:
        return jsonify({'authenticated': True}), 200
    else:
        return jsonify({'authenticated': True}), 401 #valor para produção = True

# Adicione a rota /welcome dentro do Blueprint main_bp
@main_bp.route('/home')
def home():
    if check_auth() ==True:
        return render_template('home.html')
    else:
        return render_template('home.html')#('index.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/opportunities')  # Adicione esta rota
def opportunities():
    return render_template('opportunities.html')

@main_bp.route('/performance')  # Adicione esta rota
def performance():
    return render_template('performance.html')


@main_bp.route('/settings')  # Adicione esta rota
def settings():
    return render_template('settings.html')
settings

# Adicione a rota /create_endpoint dentro do Blueprint main_bp
@main_bp.route('/create_endpoint', methods=['GET', 'POST'])
def create_endpoint():
    return process_create_endpoint_form()  # Use a função do arquivo forms.py


# Adicione estas rotas no final do arquivo

@main_bp.route('/edit_endpoint/<int:index>', methods=['POST'])
def edit_endpoint(index):
    # Obtenha os dados do formulário de edição
    exchange = request.form.get('exchange')
    base_point = request.form.get('base_point')
    endpoints = request.form.get('endpoints')
    observation = request.form.get('observation')

    # Carregue os dados existentes do arquivo JSON
    with open('app/pares/endpoint.json', 'r') as file:
        data = json.load(file)

    # Verifique se o índice está dentro dos limites
    if 0 <= index < len(data):
        # Atualize os dados do item correspondente ao índice
        data[index]['exchange'] = exchange
        data[index]['base_point'] = base_point
        data[index]['endpoints'] = endpoints
        data[index]['observation'] = observation

        # Salve os dados de volta no arquivo JSON
        with open('app/pares/endpoint.json', 'w') as file:
            json.dump(data, file, indent=2)

        flash('Endpoint editado com sucesso!', 'success')
    else:
        flash('Índice de edição inválido!', 'danger')

    return redirect(url_for('main.create_endpoint'))

@main_bp.route('/delete_endpoint/<int:index>', methods=['POST'])
def delete_endpoint(index):
    # Carregue os dados do arquivo JSON
    with open('app/pares/endpoint.json', 'r') as json_file:
        data = json.load(json_file)

    # Verifique se o índice está dentro dos limites
    if 0 <= index < len(data):
        # Remova o endpoint com base no índice
        deleted_endpoint = data.pop(index)

        # Grave os dados atualizados de volta no arquivo JSON
        with open('app/pares/endpoint.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

        flash(f'Endpoint "{deleted_endpoint["exchange"]}" apagado com sucesso!', 'success')
    else:
        flash('Índice inválido para exclusão.', 'error')

    return redirect(url_for('main.create_endpoint'))

@main_bp.route('/update_endpoint', methods=['POST'])
def update_endpoint():
    try:
        # Obtenha os dados JSON da solicitação
        data = request.get_json()

        # Carregue os dados existentes do arquivo JSON
        file_path = 'app/pares/endpoint.json'
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        # Atualize os dados do item correspondente
        existing_data[data['index']] = data['data']

        # Salve os dados atualizados de volta no arquivo JSON
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)

        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False})
