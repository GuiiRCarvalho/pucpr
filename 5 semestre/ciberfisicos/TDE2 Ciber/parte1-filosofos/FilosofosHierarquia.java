import java.util.concurrent.Semaphore;

public class FilosofosHierarquia {

    static final int N = 5;
    static Semaphore[] garfos = new Semaphore[N];
    static int[] refeicoes = new int[N];
    static volatile boolean rodando = true;

    public static void main(String[] args) throws InterruptedException {
        for (int i = 0; i < N; i++) {
            garfos[i] = new Semaphore(1, true);
        }

        Thread[] threads = new Thread[N];
        for (int i = 0; i < N; i++) {
            threads[i] = new Thread(new Filosofo(i));
            threads[i].start();
        }

        Thread.sleep(10000);
        rodando = false;
        for (int i = 0; i < N; i++) {
            threads[i].join();
        }

        System.out.println();
        System.out.println("Fim, sem deadlock. Refeicoes de cada filosofo:");
        for (int i = 0; i < N; i++) {
            System.out.println("Filosofo " + i + ": " + refeicoes[i]);
        }
    }

    static void log(int id, String estado) {
        System.out.println("Filosofo " + id + ": " + estado);
    }

    static class Filosofo implements Runnable {
        int id;
        int menor;
        int maior;

        Filosofo(int id) {
            this.id = id;
            int esquerda = id;
            int direita = (id + 1) % N;
            this.menor = Math.min(esquerda, direita);
            this.maior = Math.max(esquerda, direita);
        }

        public void run() {
            try {
                while (rodando) {
                    log(id, "pensando");
                    Thread.sleep(100);

                    log(id, "com fome");
                    garfos[menor].acquire();
                    Thread.sleep(100);
                    garfos[maior].acquire();

                    log(id, "comendo");
                    refeicoes[id]++;
                    Thread.sleep(100);

                    garfos[maior].release();
                    garfos[menor].release();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
