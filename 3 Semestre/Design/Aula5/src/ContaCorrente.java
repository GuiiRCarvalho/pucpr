// ContaCorrente.java
public class ContaCorrente extends ContaAbstrata {
    private double limiteChequeEspecial;

    public ContaCorrente(String numeroConta, double saldo, Cliente cliente, double limiteChequeEspecial) {
        super(numeroConta, saldo, cliente);
        this.limiteChequeEspecial = limiteChequeEspecial;
    }

    public double getLimiteChequeEspecial() {
        return limiteChequeEspecial;
    }

    public void setLimiteChequeEspecial(double limiteChequeEspecial) {
        this.limiteChequeEspecial = limiteChequeEspecial;
    }

    @Override
    public double obterLimite() {
        return getSaldo() + limiteChequeEspecial;
    }
}
