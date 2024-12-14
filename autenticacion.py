from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from os import path

app = Flask(__name__)

DB_PATH = path.abspath('C:\\Users\\user\\Desktop\\RedesEF-KevinCondorChavez\\registro.json')
db = TinyDB(DB_PATH)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.json.get('usuario')
    if not usuario:
        return jsonify({'error': 'Usuario no proporcionado'}), 400
    User = Query()
    if db.search(User.usuario == usuario):
        return jsonify({'mensaje': 'Ok'}), 200
    return jsonify({'mensaje': 'Usuario no registrado'}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)
