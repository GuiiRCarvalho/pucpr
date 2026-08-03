public class Main{
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