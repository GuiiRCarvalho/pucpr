import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        SuperHeroi p1 = new SuperHeroi("Guilherme Carvalho", "M", 1.75,
                Arrays.asList("Super Velocidade", "Invisivlidade", "Super Força"));
        p1.usarHabilidades();
        System.out.println(p1);
    }
}