import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Foo {
    private boolean firstFinished, secondFinished;
    private Lock lock = new ReentrantLock();
    private Condition con1, con2;

    public Foo() {
        lock.lock();
        try {
            con1 = lock.newCondition();
            con2 = lock.newCondition();
        } finally {
            lock.unlock();
        }
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        lock.lock();  // To acquire the lock before writing
        try {
            firstFinished = true;
            con1.signal();  // Signal that first is finished
        } finally {
            lock.unlock();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        lock.lock();  // Acquire lock before waiting
        try {
            while (!firstFinished) {
                con1.await();  // Wait for first to finish
            }
            printSecond.run();
            secondFinished = true;
            con2.signal();  // Signal that second is finished
        } finally {
            lock.unlock();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        lock.lock();  // Acquire lock before waiting
        try {
            while (!secondFinished) {
                con2.await();  // Wait for second to finish
            }
            printThird.run();
        } finally {
            lock.unlock();
        }
    }
}