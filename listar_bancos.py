from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='junior',
    passwd=''
)

cursor = conexao.cursor()
cursor.execute('show databases')

for indice, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {indice}: {database[0]}')