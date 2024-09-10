CREATE TABLE Casa (
    id_casa INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    fase_da_construcao TEXT,
    modelo_casa INTEGER
);

CREATE TABLE IF NOT EXISTS Casa (
    id_casa INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    fase_da_construcao TEXT,
    modelo_casa INTEGER
    id_material INTEGER
    FOREIGN KEY (id_material) REFERENCES Materiais(id_material)
);

CREATE TABLE Familia (
    id_familia INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    nome TEXT,
    numero_membros INTEGER,
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
