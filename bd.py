import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='site',
    user='root',
    password='adim'
)

cusor = conexao.cursor()

if conexao.is_connected():
    print("conectado")



conexao.close()
cusor.close()