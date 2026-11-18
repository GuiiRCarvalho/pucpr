import java.util.concurrent.locks.ReentrantLock;

public class DeadlockCorrigido {

    static ReentrantLock LOCK_A = new ReentrantLock();
    static ReentrantLock LOCK_B = new ReentrantLock();

    public static void main(String[] args) throws InterruptedException {
        Thread t1 = new Thread(new Tarefa("T1"));
        Thread t2 = new Thread(new Tarefa("T2"));

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Terminou sem deadlock");
    }

    static class Tarefa implements Runnable {
        String nome;

        Tarefa(String nome) {
            this.nome = nome;
        }

        public void run() {
            try {
                System.out.println(nome + " tentando pegar LOCK_A");
                LOCK_A.lock();
                try {
                    System.out.println(nome + " pegou LOCK_A");
                    Thread.sleep(50);
                    System.out.println(nome + " tentando pegar LOCK_B");
                    LOCK_B.lock();
                    try {
                        System.out.println(nome + " pegou LOCK_B");
                        System.out.println(nome + " concluiu");
                    } finally {
                        LOCK_B.unlock();
                    }
                } finally {
                    LOCK_A.unlock();
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
