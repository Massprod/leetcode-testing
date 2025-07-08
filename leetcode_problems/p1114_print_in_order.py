# Suppose we have a class:
#  public class Foo {
#    public void first() { print("first"); }
#    public void second() { print("second"); }
#    public void third() { print("third"); }
#  }
# The same instance of Foo will be passed to three different threads.
# Thread A will call first(), thread B will call second(),
#  and thread C will call third().
# Design a mechanism and modify the program to ensure that second()
#  is executed after first(), and third() is executed after second().
# Note:
#  We do not know how the threads will be scheduled in the operating system,
#   even though the numbers in the input seem to imply the ordering.
#  The input format you see is mainly to ensure our tests' comprehensiveness.
# ------------------------------
# nums is a permutation of [1, 2, 3].
import threading

from random import shuffle

from typing import Callable


def _printFirst() -> None:
    print('first')


def _printSecond() -> None:
    print('second')


def _printThird() -> None:
    print('third')


class Foo:
    def __init__(self):
        self.first_printed = threading.Event()
        self.second_printed = threading.Event()

    def first(self, call_back: Callable) -> None:
        call_back()
        self.first_printed.set()

    def second(self, call_back: Callable) -> None:
        call_back()
        self.second_printed.set()

    def third(self, call_back: Callable) -> None:
        self.second_printed.wait()
        call_back()


# Time complexity: O(1)
# ------------------------------
# Auxiliary space: O(1)


test: Foo = Foo()

for _ in range(10):
    test_thread1: threading.Thread = threading.Thread(target=test.first, args=(_printFirst,))
    test_thread2: threading.Thread = threading.Thread(target=test.second, args=(_printSecond,))
    test_thread3: threading.Thread = threading.Thread(target=test.third, args=(_printThird,))
    test_sequence: list[threading.Thread] = [test_thread1, test_thread2, test_thread3]
    shuffle(test_sequence)
    print('Original Sequence\n', ' -> '.join([seq.name for seq in test_sequence]))

    test_thread1.start()
    test_thread2.start()
    test_thread3.start()

    test_thread1.join()
    test_thread2.join()
    test_thread3.join()
    print('\n--- ---\n')
