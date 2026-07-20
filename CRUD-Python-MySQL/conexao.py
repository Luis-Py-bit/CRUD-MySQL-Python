import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SUA_SENHA",
    database="sistema_produtos"
)

print("Conectado com sucesso!")
