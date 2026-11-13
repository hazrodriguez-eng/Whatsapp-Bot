import os
from flask import Flask, request

app = Flask(__name__)

# 1. Este endpoint es el que Meta llamará para verificar URL
@app.route('/webhook', methods=['GET'])
def verificar_webhook():
    # El token secreto 
    VERIFY_TOKEN = "mi_token_secreto_123" 
    
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Token incorrecto', 403
    return 'Hola, el servidor está activo', 200

# 2. Este endpoint es el que recibirá los mensajes y botones cuando te escriban
@app.route('/webhook', methods=['POST'])
def recibir_mensajes():
    data = request.json
    # Aquí llegará la información cuando un cliente presione un botón
    print(data) 
    return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    # Render asigna un puerto automático mediante la variable de entorno PORT
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
