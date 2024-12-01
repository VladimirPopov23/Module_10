# module_10_3.py
# 01.12.2024 Задача "Банковские операции"

import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0  # баланс банка (int)
        self.lock = threading.Lock()  # объект класса Lock для блокировки потоков.

    def deposit(self):
        for i in range(100):
            refill = randint(50, 500)
            self.balance += refill
            print(f'Пополнение: {refill}. Баланс: {self.balance}\n', end='')
        if self.balance >= 500 and self.lock.locked() == True:
            self.lock.release()
        time.sleep(0.001)
        return self.balance

    def take(self):
        for i in range(100):
            cut = randint(50, 500)
            print(f'Запрос на {cut}\n', end='')
            if cut <= self.balance:
                self.balance -= cut
                print(f'Снятие: {cut}. Баланс: {self.balance}\n', end='')
            else:
                print(f'Запрос отклонён, недостаточно средств\n', end='')
                self.lock.acquire()
                return self.balance


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
