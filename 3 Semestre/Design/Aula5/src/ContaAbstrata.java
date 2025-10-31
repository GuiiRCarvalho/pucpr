// ContaAbstrata.java
public abstract class ContaAbstrata {
    private String numeroConta;
    private double saldo;
    private Cliente cliente;

    public ContaAbstrata(String numeroConta, double saldo, Cliente cliente) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.cliente = cliente;
    }

    public String getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(String numeroConta) {
        this.numeroConta = numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    // Método abstrato
    public abstract double obterLimite();

    // Métodos concretos
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public boolean sacar(double valor) {
        if (valor > 0 && valor <= obterLimite()) {
            saldo -= valor;
            return true;
        }
        return false;
    }
}
