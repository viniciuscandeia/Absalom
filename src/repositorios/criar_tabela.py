import sqlite3


CAMINHO_USUARIOS_DB: str = 'src/repositorios/usuarios.db'
usuarios: str = 'usuarios'


CAMINHO: str = CAMINHO_USUARIOS_DB
nome: str = usuarios

# Função para criar a tabela de usuários


def criar_tabela():
    # Conectar ao banco de dados (ou criar se não existir)
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para criar a tabela
    comando_sql = f'''
    CREATE TABLE IF NOT EXISTS {nome} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL,
        id_loja INTEGER NOT NULL
    );
    '''

    # Executar o comando SQL
    cursor.execute(comando_sql)

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()
    print(f"Tabela '{nome}' criada com sucesso.")


# Chamar a função para criar a tabela
criar_tabela()
