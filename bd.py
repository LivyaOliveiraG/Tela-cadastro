import mysql.connector
from flask import Flask, render_template, request 



conexao = mysql.connector.connect(
    host='localhost',
    port = 3306,
    database='site',
    user='root',
    password='adim'
)

cursor = conexao.cursor()

if conexao.is_connected():
    print("conectado")


cursor.close()
conexao.close()
