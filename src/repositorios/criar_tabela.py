import sqlite3

CAMINHO_USUARIOS_DB: str = "src/repositorios/database.db"
usuarios: str = "usuarios"


CAMINHO: str = CAMINHO_USUARIOS_DB
nome_tabela: str = usuarios

# Função para criar a tabela de usuários


def criar_tabela():
    # Conectar ao banco de dados (ou criar se não existir)
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para criar a tabela
    comando_sql_usuarios = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL,
        id_loja INTEGER NOT NULL
    );
    """

    # Comando SQL para criar a tabela 'lojas'
    comando_sql_lojas = """
    CREATE TABLE IF NOT EXISTS lojas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL
    );
    """

    # Comando SQL para criar a tabela 'produtos'
    comando_sql_produtos = """
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        descricao TEXT,
        quantidade INTEGER NOT NULL,
        id_loja INTEGER NOT NULL
    );
    """

    comando_sql_notificacoes = """
        CREATE TABLE notificacoes (
            id integer primary key  autoincrement,
            mensagem text,
            from_user_id integer,
            to_loja_id integer,
            foreign key (from_user_id) references usuarios(id),
            foreign key (to_loja_id) references lojas(id)
        )
    """

    # Executar os comandos SQL
    cursor.execute(comando_sql_usuarios)
    cursor.execute(comando_sql_lojas)
    cursor.execute(comando_sql_produtos)
    cursor.execute(comando_sql_notificacoes)

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()
    print(f"Tabela '{nome_tabela}' criada com sucesso.")


def apagar_tabelas():
    # Conectar ao banco de dados
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para obter os nomes de todas as tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()

    # Apagar todas as tabelas, exceto 'sqlite_sequence'
    for tabela in tabelas:
        if tabela[0] != "sqlite_sequence":
            cursor.execute(f"DROP TABLE IF EXISTS {tabela[0]};")
            print(f"Tabela '{tabela[0]}' apagada com sucesso.")

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()


def adicionar_administrador(nome: str, username: str, email: str, senha: str):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "administrador"
    id_loja = 0  # Administradores não estão associados a uma loja específica

    comando_sql = """
    INSERT INTO usuarios (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Administrador '{nome}' adicionado com sucesso.")


def adicionar_gerente(nome: str, username: str, email: str, senha: str, id_loja: int):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "gerente"

    comando_sql = """
    INSERT INTO usuarios (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Gerente '{nome}' adicionado com sucesso.")


def adicionar_vendedor(nome: str, username: str, email: str, senha: str, id_loja: int):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "vendedor"

    comando_sql = """
    INSERT INTO usuarios (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Vendedor '{nome}' adicionado com sucesso.")


def adicionar_loja(nome, endereco):
    # Conectar ao banco de dados
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para inserir uma nova loja
    comando_sql = """
    INSERT INTO lojas (nome, endereco)
    VALUES (?, ?);
    """

    # Executar o comando SQL
    cursor.execute(comando_sql, (nome, endereco))

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()
    print(f"Loja '{nome}' adicionada com sucesso.")


def adicionar_produto(nome, preco, descricao, quantidade, id_loja):
    # Conectar ao banco de dados
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para inserir um novo produto
    comando_sql = """
    INSERT INTO produtos (nome, preco, descricao, quantidade, id_loja)
    VALUES (?, ?, ?, ?, ?);
    """

    # Executar o comando SQL
    cursor.execute(comando_sql, (nome, preco, descricao, quantidade, id_loja))

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()
    print(f"Produto '{nome}' adicionado com sucesso à loja ID {id_loja}.")


if __name__ == "__main__":

    # Chamar a função para apagar todas as tabelas
    apagar_tabelas()

    # Chamar a função para criar a tabela
    criar_tabela()

    adicionar_administrador("admin", "admin", "admin", "admin")
    adicionar_gerente("gerente", "gerente", "gerente", "gerente", 1)
    adicionar_vendedor("vendedor", "vendedor", "vendedor", "vendedor", 1)

    adicionar_loja("Loja Exemplo", "Rua Exemplo, 123")

    adicionar_produto("Produto Exemplo", 29.99, "Descrição do produto", 10, 1)
