// BancoItau.java
public class BancoItau implements IBancoGeral {

    @Override
    public ContaAbstrata abrirConta(Cliente c, String numeroConta, double saldoInicial, String tipo) {
        if (tipo.equalsIgnoreCase("Poupanca")) {
            return new Poupanca(numeroConta, saldoInicial, c);
        } else if (tipo.equalsIgnoreCase("ContaCorrente")) {
            return new ContaCorrente(numeroConta, saldoInicial, c, 1000.0); // limite fixo de 1000
        }
        return null;
    }

    @Override
    public boolean depositar(ContaAbstrata c, double valor) {
        if (c != null) {
            c.depositar(valor);
            return true;
        }
        return false;
    }

    @Override
    public boolean sacar(ContaAbstrata c, double valor) {
        if (c != null) {
            return c.sacar(valor);
        }
        return false;
    }
}
