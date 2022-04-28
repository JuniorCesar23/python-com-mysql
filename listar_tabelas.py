from bd import nova_conexao

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('show tables')

    for indice, table in enumerate(cursor, start=1):
        print(f'Tabela {indice}: {table[0]}')