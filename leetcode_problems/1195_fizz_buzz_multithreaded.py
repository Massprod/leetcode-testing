# You have the four functions:
#  printFizz that prints the word "fizz" to the console,
#  printBuzz that prints the word "buzz" to the console,
#  printFizzBuzz that prints the word "fizzbuzz" to the console, and
#  printNumber that prints a given integer to the console.
# You are given an instance of the class FizzBuzz that has four functions:
#  fizz, buzz, fizzbuzz and number.
# The same instance of FizzBuzz will be passed to four different threads:
#  Thread A: calls fizz() that should output the word "fizz".
#  Thread B: calls buzz() that should output the word "buzz".
#  Thread C: calls fizzbuzz() that should output the word "fizzbuzz".
#  Thread D: calls number() that should only output the integers.
# Modify the given class to output the series [1, 2, "fizz", 4, "buzz", ...]
#  where the ith token (1-indexed) of the series is:
#  "fizzbuzz" if i is divisible by 3 and 5,
#  "fizz" if i is divisible by 3 and not 5,
#  "buzz" if i is divisible by 5 and not 3, or
#  i if i is not divisible by 3 or 5.
# Implement the FizzBuzz class:
#  FizzBuzz(int n) Initializes the object with the number n that represents the length
#   of the sequence that should be printed.
#  void fizz(printFizz) Calls printFizz to output "fizz".
#  void buzz(printBuzz) Calls printBuzz to output "buzz".
#  void fizzbuzz(printFizzBuzz) Calls printFizzBuzz to output "fizzbuzz".
#  void number(printNumber) Calls printnumber to output the numbers.
# --------------------------------
# 1 <= n <= 50
import threading

from typing import Callable


class FizzBuzz:
    # working_sol (67.37%, 42.25%) -> (41ms, 18.34mb)
    def __init__(self, n: int):
        self.n: int = n
        self.used: int = 1
        self.limit: int = self.n + 1
        self.condition: threading.Condition = threading.Condition()

    def check_fizz(self, value: int) -> bool:
        return 0 == value % 3 and 0 != value % 5
    
    def check_buzz(self, value: int) -> bool:
        return 0 != value % 3 and 0 == value % 5
    
    def check_fizzbuzz(self, value: int) -> bool:
        return 0 == value % 3 and 0 == value % 5

    def check_number(self, value: int) -> bool:
        return 0 != value % 3 and 0 != value % 5

    def wait_condition(
            self, condition: threading.Condition, printCall: Callable, checkValue
    ) -> None:
        while True:
            with condition:
                while self.used < self.limit and not checkValue(self.used):
                    condition.wait()
                if self.used >= self.limit:
                    return
                
                printCall()
                self.used += 1
                condition.notify_all()

    def fizz(self, printFizz: Callable) -> None:
        self.wait_condition(self.condition, printFizz, self.check_fizz)
        
    def buzz(self, printBuzz: Callable) -> None:
        self.wait_condition(self.condition, printBuzz, self.check_buzz)

    def fizzbuzz(self, printFizzBuzz: Callable) -> None:
        self.wait_condition(self.condition, printFizzBuzz, self.check_fizzbuzz)

    def number(self, printNumber: Callable)-> None:
        
        def print_number() -> None:
            printNumber(self.used)

        self.wait_condition(
            self.condition, print_number, self.check_number
        )


def test_print_fizz():
    print('fizz')

def test_print_buzz():
    print('buzz')

def test_print_fizzbuzz():
    print('fizzbuzz')

def test_print_number(number: int):
    print(number)


test: FizzBuzz = FizzBuzz(50)
threads: list[threading.Thread] = []
test_thread1: threading.Thread = threading.Thread(
    target=test.fizz, args=(test_print_fizz,)
)
threads.append(test_thread1)
test_thread2: threading.Thread = threading.Thread(
    target=test.buzz, args=(test_print_buzz,)
)
threads.append(test_thread2)
test_thread3: threading.Thread = threading.Thread(
    target=test.fizzbuzz, args=(test_print_fizzbuzz,)
)
threads.append(test_thread3)
test_thread4: threading.Thread = threading.Thread(
    target=test.number, args=(test_print_number,)
)
threads.append(test_thread4)


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
