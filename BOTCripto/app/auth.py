# app/auth.py
from flask import Blueprint, render_template, redirect, url_for, session
import firebase_admin
from firebase_admin import credentials, auth


bp = Blueprint('auth', __name__, url_prefix='/auth')

cred = credentials.Certificate('app/firebase_config.json')
firebase_admin.initialize_app(cred)

@bp.route('/login')
def login():
    # Verificar se o usuário já está autenticado
    if 'user' in session:
        return redirect(url_for('main.index'))

    return render_template('auth/login.html')

@bp.route('/authenticate', methods=['POST'])
def authenticate():
    # Lógica de autenticação com Firebase Admin SDK aqui
    # Exemplo fictício:
    # email = request.form['email']
    # password = request.form['password']
    # user = auth.sign_in_with_email_and_password(email, password)

    # Se a autenticação for bem-sucedida, armazene o usuário na sessão
    # session['user'] = user

    # Redirecione para a página principal
    return redirect(url_for('main.index'))
