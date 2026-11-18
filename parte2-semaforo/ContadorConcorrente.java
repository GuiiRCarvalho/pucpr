import java.util.concurrent.Semaphore;

public class ContadorConcorrente {

    static final int T = 8;
    static final int M = 200000;

    static volatile int count = 0;
    static Semaphore sem = new Semaphore(1, true);

    public static void main(String[] args) throws InterruptedException {
        System.out.println("T = " + T + ", M = " + M + ", esperado = " + (T * M));

        for (int exec = 1; exec <= 3; exec++) {
            rodar("Execucao " + exec + " sem semaforo", false);
            rodar("Execucao " + exec + " com semaforo", true);
        }
    }

    static void rodar(String nome, boolean usarSemaforo) throws InterruptedException {
        count = 0;
        Thread[] threads = new Thread[T];
        for (int i = 0; i < T; i++) {
            threads[i] = new Thread(new Tarefa(usarSemaforo));
        }

        long inicio = System.currentTimeMillis();
        for (int i = 0; i < T; i++) {
            threads[i].start();
        }
        for (int i = 0; i < T; i++) {
            threads[i].join();
        }
        long tempo = System.currentTimeMillis() - inicio;

        System.out.println(nome + ": esperado = " + (T * M) + ", obtido = " + count
                + ", tempo = " + tempo + " ms");
    }

    static class Tarefa implements Runnable {
        boolean usarSemaforo;

        Tarefa(boolean usarSemaforo) {
            this.usarSemaforo = usarSemaforo;
        }

        public void run() {
            for (int i = 0; i < M; i++) {
                if (usarSemaforo) {
                    try {
                        sem.acquire();
                        try {
                            count = count + 1;
                        } finally {
                            sem.release();
                        }
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } else {
                    count = count + 1;
                }
            }
        }
    }
}
