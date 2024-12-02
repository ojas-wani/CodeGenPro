import threading
import functools

class Foo:
    def __init__(self):
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.done = set()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.lock:
            printFirst()
            self.done.add(1)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock:
            while 1 not in self.done:
                self.condition.wait()
            printSecond()
            self.done.add(2)

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock:
            while 2 not in self.done:
                self.condition.wait()
            printThird()
            self.done.add(3)