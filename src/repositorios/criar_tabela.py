import sqlite3

CAMINHO_USUARIOS_DB: str = "src/repositorios/usuarios.db"
usuarios: str = "usuarios"


CAMINHO: str = CAMINHO_USUARIOS_DB
nome_tabela: str = usuarios

# Função para criar a tabela de usuários


def criar_tabela():
    # Conectar ao banco de dados (ou criar se não existir)
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    # Comando SQL para criar a tabela
    comando_sql = f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        tipo TEXT NOT NULL,
        id_loja INTEGER NOT NULL
    );
    """

    # Executar o comando SQL
    cursor.execute(comando_sql)

    # Commit e fechar a conexão
    conexao.commit()
    conexao.close()
    print(f"Tabela '{nome_tabela}' criada com sucesso.")


# Função para adicionar um administrador


def adicionar_administrador(nome: str, username: str, email: str, senha: str):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "administrador"
    id_loja = 0  # Administradores não estão associados a uma loja específica

    comando_sql = f"""
    INSERT INTO {nome_tabela} (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Administrador '{nome}' adicionado com sucesso.")


# Função para adicionar um gerente
def adicionar_gerente(nome: str, username: str, email: str, senha: str, id_loja: int):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "gerente"

    comando_sql = f"""
    INSERT INTO {nome_tabela} (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Gerente '{nome}' adicionado com sucesso.")


# Função para adicionar um vendedor
def adicionar_vendedor(nome: str, username: str, email: str, senha: str, id_loja: int):
    conexao = sqlite3.connect(CAMINHO)
    cursor = conexao.cursor()

    tipo = "vendedor"

    comando_sql = f"""
    INSERT INTO {nome_tabela} (nome, username, email, senha, tipo, id_loja)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    valores = (nome, username, email, senha, tipo, id_loja)

    cursor.execute(comando_sql, valores)
    conexao.commit()
    conexao.close()
    print(f"Vendedor '{nome}' adicionado com sucesso.")


if __name__ == "__main__":

    # Chamar a função para criar a tabela
    criar_tabela()

    adicionar_administrador('admin', 'admin', 'admin', 'admin')
    adicionar_gerente('gerente', 'gerente', 'gerente', 'gerente', 1)
    adicionar_vendedor('vendedor', 'vendedor', 'vendedor', 'vendedor', 1)
