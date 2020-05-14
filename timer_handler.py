# import random
# from data_controller import Data
#
#
# def get_time(comp_time, setts):
#     for _ in range(len(comp_time)):
#         ttime = '{:.2f}'.format(random.uniform(10.00, 60.00))
#         if Data.competition_data['rounds_amount'] == '1/16':
#             if setts['run_amount'] == 1:
#                 comp_time[_]['FT16_1'] = ttime
#             else:
#                 comp_time[_]['FT16_2'] = ttime
#         elif str(setts.get('rounds_amount')) == '1/8':
#             if setts['run_amount'] == '1':
#                 comp_time[_]['FT8_1'] = ttime
#             else:
#                 comp_time[_]['FT8_2'] = ttime
#         elif str(setts.get('rounds_amount')) == '1/4':
#             if setts['run_amount'] == '1':
#                 comp_time[_]['FT4_1'] = ttime
#             else:
#                 comp_time[_]['FT4_2'] = ttime
#         print(comp_time[_])
#         print(ttime)
# # TODO
# #  требуется доработка записи в словарь по заданным параметрам
# #  сорт по времени, выборка по финалам 32 = 1/16 16 = 1/8 8 = 1/4 и тд
