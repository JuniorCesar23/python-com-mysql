from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute('drop table emails')
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')