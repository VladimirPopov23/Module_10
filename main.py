# module_10_1.py
# 28.11.2024 Задача "Потоковая запись в файлы"

from time import sleep, time
from threading import Thread

time_start1 = time()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end1 = time()
print(f'Работа потоков {time_end1 - time_start1}')

time_start2 = time()

thread5 = Thread(target=write_words, args=(10, 'example5.txt'))
thread6 = Thread(target=write_words, args=(30, 'example6.txt'))
thread7 = Thread(target=write_words, args=(200, 'example7.txt'))
thread8 = Thread(target=write_words, args=(100, 'example8.txt'))

thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread5.join()
thread6.join()
thread7.join()
thread8.join()

time_end2 = time()
print(f'Работа потоков {time_end2 - time_start2}')
