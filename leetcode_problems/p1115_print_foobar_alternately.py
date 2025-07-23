# Suppose you are given the following code:
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
# The same instance of FooBar will be passed to two different threads:
#  - thread A will call foo(), while
#  - thread B will call bar().
# Modify the given program to output "foobar" n times.
# -----------------------
# 1 <= n <= 1000
import threading

from typing import Callable


class FooBar:
    # working_sol (61.12%, 76.23%) -> (69ms, 18.10mb)  time: O(n) | space: O(1)
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.foo_event: threading.Event = threading.Event()
        self.bar_event: threading.Event = threading.Event()
        self.foo_event.set()

    def foo(self, printFoo: Callable) -> None:
        for _ in range(self.n):
            self.foo_event.wait()
            printFoo()
            self.foo_event.clear()
            self.bar_event.set()

    def bar(self, printBar: Callable) -> None:
        for _ in range(self.n):
            self.bar_event.wait()
            printBar()
            self.bar_event.clear()
            self.foo_event.set()


def printFoo() -> None:
    print('foo')

def printBar() -> None:
    print('bar')


test_class: FooBar = FooBar(4)
test_foo: threading.Thread = threading.Thread(target=test_class.foo, args=[printFoo])
test_bar: threading.Thread = threading.Thread(target=test_class.bar, args=[printBar])

test_foo.start()
test_bar.start()

test_foo.join()
test_bar.join()

print(f'Alive: {threading.enumerate()}')
