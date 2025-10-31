<?php
// Dados de conexão
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "musica_db";

// Conectar ao banco
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Pegar dados do formulário
$titulo = $_POST['titulo'];
$duracao = $_POST['duracao'];
$compositor = $_POST['compositor'];
$album = $_POST['album'];

// Inserir no banco
$sql = "INSERT INTO musica (titulo, duracao, compositor, album) 
        VALUES ('$titulo', '$duracao', '$compositor', '$album')";

if ($conn->query($sql) === TRUE) {
    echo "Música adicionada com sucesso!";
} else {
    echo "Erro: " . $sql . "<br>" . $conn->error;
}

// Fechar conexão
$conn->close();
?>
