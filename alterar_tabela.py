from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'alter table contatos add column id int auto_increment primary key'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
