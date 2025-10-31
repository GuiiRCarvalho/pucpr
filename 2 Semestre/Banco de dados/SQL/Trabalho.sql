CREATE DATABASE IF NOT EXISTS db_escola;
USE db_escola;

create table usuario(
	tb_usuario_id int primary key auto_increment,
    tb_nome varchar(50) not null,
    tb_sexo varchar(50) not null,
	tb_serie varchar(50) not null
    
);
create table professor(
	tb_professor_id int primary key auto_increment,
    tb_professor_materia varchar(50) not null,
    tb_professor_nome varchar(50) not null
);