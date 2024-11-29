# module_10_2.py
# 29.11.2024 Задача "За честь и отвагу!"

import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        frag = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while frag:
            frag -= self.power
            days += 1
            time.sleep(1)
            if frag > 0:
                print(f'{self.name} сражается {days} дней(дня)..., осталось {frag} воинов.\n', end='')
            else:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!\n', end='')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
