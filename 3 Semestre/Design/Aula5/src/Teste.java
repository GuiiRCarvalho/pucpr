// Teste.java
public class Teste {
    public static void main(String[] args) {
        IBancoGeral banco = new BancoItau();

        Cliente cliente1 = new Cliente("João", "123.456.789-00");
        Cliente cliente2 = new Cliente("Maria", "987.654.321-00");

        // Criando contas
        ContaAbstrata poupanca = banco.abrirConta(cliente1, "001", 500.0, "Poupanca");
        ContaAbstrata corrente = banco.abrirConta(cliente2, "002", 1000.0, "ContaCorrente");

        // Operações na poupança
        banco.depositar(poupanca, 200.0);
        banco.sacar(poupanca, 100.0);

        // Operações na conta corrente
        banco.depositar(corrente, 500.0);
        banco.sacar(corrente, 2000.0); // usa cheque especial

        // Resultados
        System.out.println("Saldo Poupança (" + poupanca.getCliente().getNome() + "): " + poupanca.getSaldo());
        System.out.println("Saldo Conta Corrente (" + corrente.getCliente().getNome() + "): " + corrente.getSaldo());
    }
}
