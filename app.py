from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '¡App funcionando en Render!'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "No se recibió el código de autorización."

    token_response = get_access_token(code)
    if 'access_token' in token_response:
        return f"Access Token: {token_response['access_token']}"
    else:
        return f"Error al obtener token: {token_response}"

def get_access_token(code):
    url = "https://api.mercadolibre.cl/oauth/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": "8124944839883970",  # tu client_id
        "client_secret": "ApMUdaSXq4JbnIcmumfd53egwblUW1AD",  # tu client_secret
        "code": code,
        "redirect_uri": "https://mi-app-fci6.onrender.com/callback"
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
