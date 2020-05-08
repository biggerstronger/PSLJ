import random


def get_time(comp_time):
    for _ in range(len(comp_time)):
        ttime = random.uniform(5.00, 60.00)
        ttime = '{:.2f}'.format(ttime)
        comp_time[_]['FTBig_1'] = ttime
        print(comp_time[_])
        print(ttime)
# TODO
#  требуется доработка записи в словарь по заданным параметрам
