# module_10_5.py
# 07.12.2024 Задача "Многопроцессное считывание"

from datetime import datetime
from multiprocessing import Pool


def read_info(*name):
    all_data = []
    for file_line in name:
        with open(file_line, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if line:
                    all_data.append(line)
                else:
                    break


filenames = [f'./file {number}.txt' for number in range(1, 5)]
print(filenames)

# Линейный вызов
start_time1 = datetime.now()
# for file in filenames:
#     data = read_info(file)
# ended_time1 = datetime.now()
# elapsed1 = ended_time1 - start_time1
# print(f'{elapsed1} (линейный)')

# Многопроцессный
if __name__ == '__main__':
    with Pool(4) as p:
        start_time2 = datetime.now()
        p.map(read_info, filenames)
        ended_time2 = datetime.now()
        elapsed2 = ended_time2 - start_time2
        print(f'{elapsed2} (многопроцессный)')
