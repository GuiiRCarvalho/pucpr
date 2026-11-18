import java.util.concurrent.locks.ReentrantLock;

public class DeadlockTravando {

    static ReentrantLock LOCK_A = new ReentrantLock();
    static ReentrantLock LOCK_B = new ReentrantLock();

    public static void main(String[] args) {
        Thread t1 = new Thread(new Runnable() {
            public void run() {
                try {
                    System.out.println("T1 tentando pegar LOCK_A");
                    LOCK_A.lock();
                    System.out.println("T1 pegou LOCK_A");
                    Thread.sleep(50);
                    System.out.println("T1 tentando pegar LOCK_B");
                    LOCK_B.lock();
                    System.out.println("T1 pegou LOCK_B");
                    System.out.println("T1 concluiu");
                    LOCK_B.unlock();
                    LOCK_A.unlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t2 = new Thread(new Runnable() {
            public void run() {
                try {
                    System.out.println("T2 tentando pegar LOCK_B");
                    LOCK_B.lock();
                    System.out.println("T2 pegou LOCK_B");
                    Thread.sleep(50);
                    System.out.println("T2 tentando pegar LOCK_A");
                    LOCK_A.lock();
                    System.out.println("T2 pegou LOCK_A");
                    System.out.println("T2 concluiu");
                    LOCK_A.unlock();
                    LOCK_B.unlock();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        t1.start();
        t2.start();
    }
}
