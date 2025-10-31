package br.com.guilherme.Junit;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculadoraTeste {
    @Test
    void deveSomardoisnumero(){
        Calculadora calculadora = new Calculadora();
        int esperado = 10;
        int atual = calculadora.somar(5,5);
        assertEquals(esperado,atual, "A soma de 5 e 5 deve ser 10");
    }
   @Test
    void deveSubtrairDoisNumero(){
        Calculadora calculadora = new Calculadora();
        int esperado = 0;
        int atual = calculadora.subtrair(10,10);
        assertEquals(esperado,atual, "A subtracao de 10 - 10 deve ser 0");
    }
}
