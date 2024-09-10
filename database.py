import sqlite3

# Nome do arquivo do banco de dados
nome_do_banco = 'meu_banco_de_dados.db'

# Conectando ao banco de dados (ou criando-o se não existir)
conn = sqlite3.connect(nome_do_banco)

# Criando um cursor para executar comandos SQL
cur = conn.cursor()

# Comandos SQL para criar tabelas
comandos_sql = """
CREATE TABLE IF NOT EXISTS Casa (
    id_casa INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    fase_da_construcao TEXT,
    modelo_casa INTEGER
);

CREATE TABLE IF NOT EXISTS Materiais (
    id_material INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    quantidade INTEGER,
    preco FLOAT,
    id_casa INTEGER,
    FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);

CREATE TABLE IF NOT EXISTS Familia (
    id_familia INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    numero_membros INTEGER,
    id_casa INTEGER,
    FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);

CREATE TABLE IF NOT EXISTS Voluntario (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    email TEXT,
    senha TEXT,
    funcao TEXT CHECK(funcao IN ('lider', 'voluntario'))
);
"""

# Executando os comandos SQL para criar as tabelas
cur.executescript(comandos_sql)

# Commit e fechamento da conexão
conn.commit()
conn.close()

print(f"Banco de dados '{nome_do_banco}' criado com sucesso!")
