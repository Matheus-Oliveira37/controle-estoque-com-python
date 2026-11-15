from database import conectar
from rich import print
import csv


def cadastrar_produtos(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO produtos
    (nome, preco, quantidade)
    VALUES (%s, %s, %s)
    """

    valores = (nome, preco, quantidade)

    cursor.execute(sql, valores)

    conexao.commit()

    print("[chartreuse2]Produto cadastrado![/]")

    cursor.close()
    conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos


def buscar_produto(nome):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT * FROM produtos
    WHERE nome LIKE %s
    """

    cursor.execute(sql, (f"%{nome}%",))

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()
    
    return produtos


def atualizar_estoque(id_produto, nova_quantidade):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE produtos
    SET quantidade = %s
    WHERE id = %s
    """

    cursor.execute(sql, (nova_quantidade, id_produto))

    conexao.commit()

    print("[chartreuse2]Estoque atualizado![/]")

    cursor.close()
    conexao.close()


def excluir_produto(id_produto):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    DELETE FROM produtos
    WHERE id = %s
    """

    cursor.execute(sql, (id_produto,))

    conexao.commit()

    print("[chartreuse2]Produto removido![/]")

    cursor.close()
    conexao.close()

def estoque_baixo():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""SELECT * FROM produtos
                   WHERE quantidade < 10"""
                   )
    
    produtos = cursor.fetchall()
    
        
    cursor.close()
    conexao.close()
    
    return produtos
    
def order_preco():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""SELECT * FROM produtos
                   ORDER BY preco DESC""")
    
    produtos = cursor.fetchall()
        
    conexao.close()
    cursor.close()
    
    return produtos
    
def valor_total():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""SELECT SUM(preco * quantidade)
                   FROM produtos""")
    
    total = cursor.fetchone()[0]

    conexao.close()
    cursor.close()
    
    return total or 0

def exportar_csv():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM produtos")
    
    produtos = cursor.fetchall()
    
    with open(
        "produtos.csv",
        mode="w",
        newline="",
        encoding="utf-8"
    ) as arquivo:
        
        escritor = csv.writer(arquivo)
        
        escritor.writerow([
            "ID",
            "Nome",
            "Preço",
            "Quantidade",
            "Data Cadastro"
        ])
        
        for produto in produtos:
            escritor.writerow(produto)
            
    cursor.close()
    conexao.close()