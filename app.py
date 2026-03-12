from flask import Flask, send_from_directory  
import os, openpyxl
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FRONTEND_DIR = os.path.join(BASE_DIR, 'front-end')
STATIC_DIR = os.path.join(FRONTEND_DIR, 'static')

DB_DIR = os.path.join(os.path.dirname(__file__), '..', 'DB')
EXCEL_FILE = os.path.join(DB_DIR, 'clientes.xlsx')

COLUMNS = ["ID", "Nome", "CPF", "Email", "Telefone", "Endereço", "Observações", "Data Cadastro"]

def init_excel():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    if not os.path.exists(EXCEL_FILE):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Clientes"
        sheet.append(COLUMNS)
        workbook.save(EXCEL_FILE)

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="/" + STATIC_DIR)

@app.route("/")                              
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/consulta")                              
def consulta_page():
    return send_from_directory(FRONTEND_DIR, "consulta.html")

@app.route("/alterar")                              
def alterar_page():
    return send_from_directory(FRONTEND_DIR, "alterar.html")

if __name__ == "__main__":
    print("BASE_DIRECTORY:", BASE_DIR)
    print("FRONTEND_DIRECTORY:", FRONTEND_DIR)
    print("STATIC_DIRECTORY:", STATIC_DIR)
    app.run(debug=True)
