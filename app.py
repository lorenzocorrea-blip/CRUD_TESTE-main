from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_db():
    return mysql.connector.connect(host="localhost", user="root", password="root@root", database="teste_crud")

# 1. READ (Ler do banco)
@app.route("/tarefas", methods=["GET"])
def listar():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tarefas")
    return jsonify(cursor.fetchall())

# 2. CREATE (Salvar no banco)
@app.route("/tarefas", methods=["POST"])
def criar():
    texto = request.get_json()["descricao"]
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", (texto,))
    db.commit()
    return jsonify({"status": "ok"}), 201

app.run(port=5000)