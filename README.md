#Usando SQLite CLI
##Instale o SQLite:

Se ainda não tiver o SQLite instalado, você pode baixá-lo e instalá-lo a partir do site oficial do SQLite.

Abra o Terminal ou Prompt de Comando:

No Windows, você pode usar o Prompt de Comando ou o PowerShell. No macOS ou Linux, use o Terminal.

Crie um Novo Banco de Dados:

Execute o comando abaixo para criar um novo banco de dados (o arquivo será criado no diretório atual):

sh
Copiar código
sqlite3 nome_do_banco_de_dados.db
Substitua nome_do_banco_de_dados.db pelo nome desejado para o seu banco de dados.

Crie Tabelas no Banco de Dados:

Após executar o comando acima, você será levado ao prompt interativo do SQLite. Agora você pode criar suas tabelas. Por exemplo:

sql
Copiar código
CREATE TABLE Casa (
    id_casa INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    fase_da_construcao TEXT,
    modelo_casa INTEGER
);

CREATE TABLE Materiais (
    id_material INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    quantidade INTEGER,
    preco FLOAT,
    id_casa INTEGER,
    FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);

CREATE TABLE Voluntario (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    email TEXT,
    senha TEXT,
    funcao TEXT CHECK(funcao IN ('lider', 'voluntario'))
);

CREATE TABLE Familia (
    id_familia INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    numero_membros INTEGER,
    id_casa INTEGER,
    FOREIGN KEY (id_casa) REFERENCES Casa(id_casa)
);
