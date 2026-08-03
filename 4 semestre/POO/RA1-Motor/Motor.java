public class Motor {

    private static final int RPM_INICIAL = 1000;
    private static final int RPM_MAX = 8000;
    private static final int RPM_MIN = 0;

    private boolean ligado;
    private int rpm;

    public Motor() {
        this.ligado = false;
        this.rpm = 0;
    }

    // --- Getters ---

    public boolean isLigado() {
        return ligado;
    }

    public int getRpm() {
        return rpm;
    }

    // --- Métodos públicos ---

    public void ligar() {
        if (ligado) {
            System.out.println("Motor já está ligado.");
            return;
        }
        ligado = true;
        rpm = RPM_INICIAL;
        System.out.println("Motor ligado. RPM inicial: " + rpm);
    }

    public void desligar() {
        if (!ligado) {
            System.out.println("Motor já está desligado.");
            return;
        }
        ligado = false;
        rpm = 0;
        System.out.println("Motor desligado. RPM: " + rpm);
    }

    public void acelerar(int nivel) {
        if (!ligado) {
            System.out.println("Não é possível acelerar: motor desligado.");
            return;
        }

        int novoRpm = rpm + (nivel * 1000);

        if (novoRpm >= RPM_MAX) {
            rpm = RPM_MAX;
            System.out.println("Limite máximo atingido! RPM travado em " + rpm + ".");
        } else if (novoRpm <= RPM_MIN) {
            rpm = 0;
            ligado = false;
            System.out.println("RPM zerado. Motor desligado automaticamente.");
        } else {
            rpm = novoRpm;
            String direcao = (nivel > 0) ? "Acelerando" : "Desacelerando";
            System.out.println(direcao + " (nível " + nivel + "). RPM atual: " + rpm);
        }
    }

    public void exibirStatus() {
        String estado = ligado ? "LIGADO" : "DESLIGADO";
        System.out.println("[Motor] Estado: " + estado + " | RPM: " + rpm);
    }

    // --- Main para teste ---

    public static void main(String[] args) {
        Motor m = new Motor();

        m.exibirStatus();   // DESLIGADO | RPM: 0
        m.ligar();          // Motor ligado. RPM: 1000
        m.acelerar(3);      // RPM: 1000 + 3000 = 4000
        m.acelerar(5);      // RPM: 4000 + 5000 = 9000 → travado em 8000
        m.acelerar(-2);     // RPM: 8000 - 2000 = 6000
        m.acelerar(-7);     // RPM: 6000 - 7000 → motor desliga
        m.exibirStatus();   // DESLIGADO | RPM: 0
    }
}