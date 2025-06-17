import pymysql

def conectar():
    try:
        conexao = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='Phpp2004.',
            database='cadastro',
        )
        print('Conectado ao banco de dados!')
        return conexao
    except pymysql.MySQLError as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None