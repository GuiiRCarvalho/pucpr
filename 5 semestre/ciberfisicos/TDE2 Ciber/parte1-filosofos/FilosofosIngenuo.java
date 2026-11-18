import java.util.concurrent.Semaphore;

public class FilosofosIngenuo {

    static final int N = 5;
    static Semaphore[] garfos = new Semaphore[N];

    public static void main(String[] args) {
        for (int i = 0; i < N; i++) {
            garfos[i] = new Semaphore(1);
        }
        for (int i = 0; i < N; i++) {
            new Thread(new Filosofo(i)).start();
        }
    }

    static void log(int id, String estado) {
        System.out.println("Filosofo " + id + ": " + estado);
    }

    static class Filosofo implements Runnable {
        int id;
        int esquerda;
        int direita;

        Filosofo(int id) {
            this.id = id;
            this.esquerda = id;
            this.direita = (id + 1) % N;
        }

        public void run() {
            try {
                while (true) {
                    log(id, "pensando");
                    Thread.sleep(100);

                    log(id, "com fome");
                    garfos[esquerda].acquire();
                    log(id, "pegou o garfo " + esquerda + " (esquerda)");
                    Thread.sleep(100);
                    garfos[direita].acquire();
                    log(id, "pegou o garfo " + direita + " (direita)");

                    log(id, "comendo");
                    Thread.sleep(100);

                    garfos[direita].release();
                    garfos[esquerda].release();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
