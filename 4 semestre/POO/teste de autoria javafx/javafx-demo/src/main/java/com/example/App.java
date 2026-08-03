package com.example;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.scene.text.Text;
import javafx.stage.Stage;

public class App extends Application {
    @Override
    public void start(Stage stage) {
        // Label de instrução
        Label label = new Label("Digite seu nome:");

        // Campo de entrada
        TextField textField = new TextField();
        textField.setPromptText("Seu nome");

        // Texto que exibirá a saudação
        Text textoSaudacao = new Text();

        // Botão de confirmação
        Button botao = new Button("Confirmar");
        botao.setOnAction(e -> {
            String nome = textField.getText();
            if (nome == null || nome.isBlank()) {
                textoSaudacao.setText("Olá, visitante!");
            } else {
                textoSaudacao.setText("Olá, " + nome + "!");
            }
        });

        // Layout vertical
        VBox root = new VBox(10); // espaçamento 10
        root.setAlignment(Pos.CENTER);
        root.getChildren().addAll(label, textField, botao, textoSaudacao);

        Scene scene = new Scene(root, 400, 200);

        stage.setTitle("Exemplo JavaFX");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}