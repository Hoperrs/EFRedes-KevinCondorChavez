from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from os import path

app = Flask(__name__)

DB_PATH = path.abspath('C:\\Users\\user\\Desktop\\RedesEF-KevinCondorChavez\\registro.json')
db = TinyDB(DB_PATH)

@app.route('/registrar', methods=['POST'])
def registrar():
    # obtengo usuario desde el req body
    usuario = request.json.get('usuario')

    # valido que el valor exista
    if not usuario:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    
    User = Query()
    # Verificar
    if db.search(User.usuario == usuario):
        return jsonify({'error': 'Usuario ya registrado'}), 400    # Registro
    db.insert({'usuario': usuario})
    return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201

if __name__ == '__main__':
    app.run(port=5001, debug=True)
