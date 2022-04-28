from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'insert into contatos (nome, tel) values (%s, %s)'
args = ('Júnior', '98765-4321')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as err:
        print(f'Erro: {err.msg}')
    else:
        print(f'1 registro incluído, ID: ', cursor.lastrowid)