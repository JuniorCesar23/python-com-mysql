from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

tabela_contatos = """
    create table contatos (
        nome varchar(50),
        tel varchar(40)
    )
"""

tabela_emails = """
    create table emails (
        id int auto_increment primary key,
        dono varchar(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tabela_emails)
    except ProgrammingError as erro:
        print(f'Erro: {erro.msg}')