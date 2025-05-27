from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '¡App funcionando en Render!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    return f'Recibí el código: {code}'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
