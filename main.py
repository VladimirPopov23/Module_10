# module_10_4.py
# 04.12.2024 Задача "Потоки гостей в кафе"

from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number  # номер стола
        self.guest = None  # гость, который сидит за этим столом (по умолчанию None)


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name  # номер стола

    def run(self):
        sleep(randint(3, 10))  # ожидание от 3 до 10 сек.


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()  # очередь (объект класса Queue)
        self.tables = tables  # столы в этом кафе (любая коллекция).

    def guest_arrival(self, *guests):  # прибытие гостей, должен принимать неограниченное кол-во гостей
        for guest in guests:
            for table in self.tables:
                if table.guest is None:  # если стол не занят
                    table.guest = guest  # сажаем гостя за стол (назначаем столу guest)
                    table.guest.start()  # запускаем поток гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                self.queue.put(guest)  # иначе добавляем гостя в очередь потока
                print(f'{guest.name} в очереди')

    def discuss_guests(self):  # обслужить гостей
        # Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
        while not self.queue.empty() or not (table.guest for table in self.tables):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):  # если стол занят и поток завершен (is_alive)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None  # текущий стол освобождается

                if not self.queue.empty() and (table.guest is None):  # если очередь не пуста (метод empty) и стол один из столов освободился (None)
                    name_guest = self.queue.get()  # гость взятый из очереди (queue.get())
                    table.guest = name_guest  # текущему столу присваивается гость взятый из очереди (queue.get())
                    print(f'{name_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    name_guest.start()  # Далее запустить поток этого гостя (start)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
