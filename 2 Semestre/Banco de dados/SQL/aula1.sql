 -- Criando data base
 CREATE DATABASE db_teste;
 -- Posicionanado software no data base
 use db_teste; 
 --DROP DATABASE db_teste caso fosse apagar

 CREATE TABLE tb_teste(
    teste_id INT PRIMARY KEY AUTO_INCREMENT,
    teste_nome varchar (50)
    teste_compl TEXT,
    teset_idade INT,
    teste_admissao date,
    teste_log DATETIME,
 );
SELECT * tb_teste
-- Crud (DML>> Estou trabalhando com regsitro de tabelas)
-- C - Create >> Insert
-- R - Retrieve >> Select
-- U - Uptade
-- D - Delete
-- ------------------

--1) Insert
Insert INTO tb_teste(
    teste_nome 
    teste_compl
    teset_idade 
    teste_admissao 
    teste_log 
)
VALUES(
    'Guilherme Reis Carvalho',
    'Teste de insercao no primeiro banco',
    19,
    '2025-04-24',
    '2025-05-24 08:54:00'
);
 