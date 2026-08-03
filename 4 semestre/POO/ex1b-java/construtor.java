class ContaBancaria {
    private String titular;
    private double saldo;

    public ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public void depositar(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.printf("[+] Depósito de R$%.2f realizado na conta de %s.\n", valor, this.titular);
        } else {
            System.out.println("[-] Erro: O valor do depósito deve ser maior que zero.");
        }
    }

    public void sacar(double valor) {
        if (valor <= 0) {
            System.out.println("[-] Erro: O valor do saque deve ser maior que zero.");
        } else if (valor > this.saldo) {
            System.out.printf("[-] Erro: Saldo insuficiente para o saque de R$%.2f na conta de %s.\n", valor, this.titular);
        } else {
            this.saldo -= valor;
            System.out.printf("[-] Saque de R$%.2f realizado na conta de %s.\n", valor, this.titular);
        }
    }
}

public class construtor {
    public static void main(String[] args) {
        ContaBancaria contaAlice = new ContaBancaria("Alice", 1000.00);
        ContaBancaria contaBruno = new ContaBancaria("Bruno", 500.00);

        System.out.println("========================================");
        System.out.println("TESTE DA CONTA 1: ALICE");
        System.out.println("========================================");
        
        System.out.printf("Saldo ANTES do depósito: R$%.2f\n", contaAlice.getSaldo());
        contaAlice.depositar(500.00);
        System.out.printf("Saldo DEPOIS do depósito: R$%.2f\n", contaAlice.getSaldo());
        
        System.out.println("----------------------------------------");
        
        System.out.printf("Saldo ANTES do saque: R$%.2f\n", contaAlice.getSaldo());
        contaAlice.sacar(200.00);
        System.out.printf("Saldo DEPOIS do saque: R$%.2f\n", contaAlice.getSaldo());

        System.out.println("\n========================================");
        System.out.println("TESTE DA CONTA 2: BRUNO");
        System.out.println("========================================");
        
        System.out.printf("Saldo ANTES do depósito: R$%.2f\n", contaBruno.getSaldo());
        contaBruno.depositar(300.50);
        System.out.printf("Saldo DEPOIS do depósito: R$%.2f\n", contaBruno.getSaldo());
        
        System.out.println("----------------------------------------");
        
        System.out.printf("Saldo ANTES do saque: R$%.2f\n", contaBruno.getSaldo());
        contaBruno.sacar(700.00);
        System.out.printf("Saldo DEPOIS do saque: R$%.2f\n", contaBruno.getSaldo());
    }
}