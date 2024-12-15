from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from os import path

app = Flask(__name__)

# En Windows: La ruta debe ser abosluta
# DB_PATH = path.abspath('C:\\Users\\user\\Desktop\\RedesEF-KevinCondorChavez\\registro.json')
# db = TinyDB(DB_PATH)

# En linux: La ruta puede ser relativa
db = TinyDB('registro.json')

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
    app.run(port=3002, debug=True)
