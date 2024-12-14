from flask import Flask, request, jsonify
import requests
from tinydb import TinyDB, Query

app = Flask(__name__)
db_mensajes = TinyDB('mensajes.json')  # BD para los mensajes

# URL de la API de Autenticación
AUTENTICACION_URL = 'http://127.0.0.1:5002/autenticar'

def validar_usuario(usuario):
    """Llama a la API de Autenticación para validar si un usuario está registrado."""
    response = requests.post(AUTENTICACION_URL, json={'usuario': usuario})
    return response.status_code == 200

@app.route('/escribir', methods=['POST'])
def escribir():
    usuario = request.json.get('usuario')
    mensaje = request.json.get('mensaje')
    if not usuario or not mensaje:
        return jsonify({'error': 'Usuario o mensaje no proporcionado'}), 400
    if not validar_usuario(usuario):
        return jsonify({'error': 'Usuario no registrado'}), 404
    db_mensajes.insert({'usuario': usuario, 'mensaje': mensaje})
    return jsonify({'mensaje': 'Mensaje registrado exitosamente'}), 201

@app.route('/leer', methods=['GET'])
def leer():
    usuario = request.args.get('usuario')
    if not usuario:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    if not validar_usuario(usuario):
        return jsonify({'error': 'Usuario no registrado'}), 404
    mensajes = db_mensajes.search(Query().usuario == usuario)
    return jsonify({'mensajes': mensajes}), 200

if __name__ == '__main__':
    app.run(port=5003, debug=True)
