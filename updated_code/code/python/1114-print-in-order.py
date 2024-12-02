import threading

class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.done = set()
        self.done.add(0)

    def first(self, printFirst):
        with self.lock:
            printFirst()
            self.done.clear()
            self.done.add(1)
            self.condition.notify_all()

    def second(self, printSecond):
        with self.lock:
            while 1 not in self.done:
                self.condition.wait()
            printSecond()
            self.done.clear()
            self.done.add(2)
            self.condition.notify_all()

    def third(self, printThird):
        with self.lock:
            while 2 not in self.done:
                self.condition.wait()
            printThird()
            self.done.clear()
            self.done.add(3)