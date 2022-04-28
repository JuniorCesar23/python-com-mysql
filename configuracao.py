from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='junior',
    passwd=''
)

print(conexao)