# run.py
from app import create_app

# Defina uma versão (por exemplo, timestamp)
version = '1.0'

app = create_app(version)

if __name__ == '__main__':
    app.run(debug=True)
