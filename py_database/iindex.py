import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conn = sqlite3.connect(ROOT_PATH/"clientes.sqlite")
cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

def criarTabela(cursor,conn):
  cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(240), email VARCHAR(240))")
  conn.commit()

def inserirRegistro(conn, cursor, nome, email):
  data = (nome,email)
  cursor.execute("Insert INTO clientes (nome,email) VALUES (?,?);", data)
  conn.commit()
  
def atualizarRegistro(conn, cursor, nome, email, id):
  data = (nome,email,id)
  cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
  conn.commit()
  
  
def deletarRegistro(conn, cursor, id):
  data = (id,)
  cursor.execute("DELETE FROM clientes WHERE id=?;", data)
  conn.commit()
  
def inserVariosRegistro(conn, cursor,listaDados):
  cursor.executemany("INSERT INTO clientes (nome, email) values(?,?)", listaDados)
  conn.commit()

def consultarVariosRegistro( cursor):
  cursor.execute("SELECT * FROM clientes")
  resultado = cursor.fetchall()
  return resultado

def consultarUmRegistro(cursor, id):
  cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
  return cursor.fetchone()
# atualizarRegistro(conn, cursor, "teste", "teste@gmail.com", 1)
# deletarRegistro(conn, cursor, 1)
# lista = [("Jack","jack@gmail.com"),("Jack2","jack2@gmail.com"),]
# inserVariosRegistro(conn, cursor, lista)
cliente = consultarUmRegistro(cursor, 2)
print(consultarVariosRegistro(cursor))
print(consultarVariosRegistro(cursor))
print((dict(cliente)))
  

