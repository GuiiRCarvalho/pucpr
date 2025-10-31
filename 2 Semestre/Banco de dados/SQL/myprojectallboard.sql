CREATE DATABASE my_allboard;
USE my_allboard;

CREATE TABLE alunos_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    serie VARCHAR(30) NOT NULL
);

CREATE TABLE professor_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    grade_horaria INT NOT NULL,
    CPF VARCHAR(11) UNIQUE NOT NULL
);

CREATE TABLE gestor_educacional_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(200) UNIQUE NOT NULL, 
    senha VARCHAR(50) NOT NULL, 
    cpf VARCHAR(11) UNIQUE NOT NULL, 
    curso_educado VARCHAR(50) NOT NULL,
    quantidade_instituicoes INT NOT NULL
);

CREATE TABLE instituicao_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cursos_oferecidos INT NOT NULL,
    plano_de_acesso INT NOT NULL,
    FOREIGN KEY (plano_de_acesso) REFERENCES plano_de_acesso_id(id)
);

CREATE TABLE plano_de_acesso_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    opcoes_planos_oferecidos VARCHAR(400) NOT NULL
);

CREATE TABLE conteudo_educacional_id (
    id_conteudo_educacional INT AUTO_INCREMENT PRIMARY KEY,
    materia VARCHAR(50) NOT NULL,
    id_professor INT NOT NULL,
    curso_associado VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professor_id(id)
);

CREATE TABLE materia_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE avaliacoes_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT NOT NULL,
    id_materia INT NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES alunos_id(id),
    FOREIGN KEY (id_materia) REFERENCES materia_id(id)
);
