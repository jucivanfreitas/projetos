from flask import Flask, render_template, session, abort
import os


app = Flask(__name__)


# Configure o caminho do diretório de templates
template_dir = os.path.abspath('app/templates')
app.template_folder = template_dir

### tentativa de conectar google ao projeto
def login_is_required(functions):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # sessão requerida
        else:
            return functions(*args, **kwargs)

    return wrapper

### tentativa de conectar google ao projeto


@app.route('/')
##@login_is_required
def home():
    return render_template('templates/home.html')


### tentativa de conectar google ao projeto


@app.route('/login')

def login2():
    return render_template('/auth/login')
    pass


@app.route('/callback')
def callback():
    pass

@app.route('/logout')
def logout():
    session.clear()
    pass


@app.route('/area_protegida')
@login_is_required
def area_protegida():
    return "protected"

### tentativa de conectar google ao projeto

if __name__ == '__main__':
    app.run(debug=True)
