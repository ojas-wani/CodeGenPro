class Foo {
    private boolean firstFinished, secondFinished;

    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        printFirst.run();
        firstFinished = true;
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (!firstFinished) {
            Thread.sleep(1);
        }
        printSecond.run();
        secondFinished = true;
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (!secondFinished) {
            Thread.sleep(1);
        }
        printThird.run();
    }
}