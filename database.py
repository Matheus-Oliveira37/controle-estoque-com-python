import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha_aqui",
            database="estoque_db"
        )
        
        return conexao


    
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar com o banco de dados: {erro}")
        
        
