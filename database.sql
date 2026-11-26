CREATE DATABASE teste_crud;

USE teste_crud;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100)
    );

INSERT INTO tarefas (descricao) VALUES ('Estudar CRUD'), ('Tomar café');