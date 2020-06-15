import xlwt
import xlrd
from xlutils.copy import copy
import new_form


class XLS:

    def __init__(self):
        open('test.xls', 'w').close()
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Шаблон')
        ws.write(0, 0, 'Hello')
        wb.save('test.xls')

    def save_excel(self, sheet_name, data):  # TODO param: sheet_name, table_name; make a template with competition data
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        ws = wb.add_sheet(sheet_name)
        ws.write_merge(0, 0, 0, 6, '{}'.format(data['title']), xlwt.easyxf("align: horiz center"))
        ws.write_merge(1, 1, 0, 6, '{}'.format(data['place']), xlwt.easyxf("align: horiz center"))
        ws.write_merge(3, 3, 0, 6, '{}'.format('test'),
                       xlwt.easyxf("align: horiz center"))  # TODO add param 'list name'
        ws.write_merge(5, 5, 0, 6, '{}'.format(data['type']), xlwt.easyxf("align: horiz center"))
        ws.write_merge(7, 7, 0, 1, '{}'.format('Организаторы:'), xlwt.easyxf("align: horiz left"))
        # TODO set column width depending on len(data)
        ws.write_merge(7, 7, 2, 3, '{}'.format(data['orgs']), xlwt.easyxf("align: horiz left"))
        ws.write_merge(7, 7, 4, 5, 'Информация о трассе:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 0, 2, 'Главная Судейская Комиссия', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 4, 4, 'Название трассы:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 5, 5, str(data['track_name']), xlwt.easyxf("align: horiz left"))
        ws.write_merge(11, 11, 0, 1, 'Технический делегат:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(11, 11, 2, 2, str(data['delegat'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(11, 11, 3, 3, str(data['delegat'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(12, 12, 0, 1, 'Директор соревнований:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(12, 12, 2, 2, str(data['director'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(12, 12, 3, 3, str(data['director'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(13, 13, 0, 0, 'Рефери:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(13, 13, 2, 2, str(data['referee'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(13, 13, 3, 3, str(data['referee'][0]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(14, 14, 0, 1, 'Главный секретарь:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(14, 14, 2, 2, str(data['secretary'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(14, 14, 3, 3, str(data['secretary'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(16, 16, 0, 1, 'Начальник трассы:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(16, 16, 2, 2, str(data['track_chief'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(16, 16, 3, 3, str(data['track_chief'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(17, 17, 0, 1, 'Рефери на старте:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(17, 17, 2, 2, str(data['start_referee'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(17, 17, 3, 3, str(data['start_referee'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(19, 19, 0, 1, 'Постановщик трассы:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(19, 19, 2, 2, str(data['track_dir'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(19, 19, 3, 3, str(data['track_dir'][1]), xlwt.easyxf("align: horiz left"))

        ws.write_merge(21, 21, 0, 1, 'Открывающие:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(21, 21, 2, 2, str(data['opener1'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(21, 21, 3, 3, str(data['opener1'][1]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(22, 22, 2, 2, str(data['opener2'][0]), xlwt.easyxf("align: horiz left"))
        ws.write_merge(22, 22, 3, 3, str(data['opener2'][1]), xlwt.easyxf("align: horiz left"))

        ws.write(11, 4, 'Старт:', xlwt.easyxf("align: horiz left"))
        ws.write(11, 5, str(data['start']), xlwt.easyxf("align: horiz left"))

        ws.write(12, 4, 'Финиш:', xlwt.easyxf("align: horiz left"))
        ws.write(12, 5, str(data['finish']), xlwt.easyxf("align: horiz left"))

        ws.write(13, 4, 'Перепад высот:', xlwt.easyxf("align: horiz left"))
        ws.write(13, 5, str(data['alt_dif']), xlwt.easyxf("align: horiz left"))

        ws.write(14, 4, '№ гомологации:', xlwt.easyxf("align: horiz left"))
        ws.write(14, 5, str(data['homologation']), xlwt.easyxf("align: horiz left"))

        ws.write(15, 4, 'Количество ворот:', xlwt.easyxf("align: horiz left"))
        ws.write(15, 5, str(data['gates_amount']), xlwt.easyxf("align: horiz left"))

        ws.write(16, 4, 'Длина трассы:', xlwt.easyxf("align: horiz left"))
        ws.write(16, 5, str(data['track_len']), xlwt.easyxf("align: horiz left"))

        ws.write(17, 4, 'Время начала:', xlwt.easyxf("align: horiz left"))
        ws.write(17, 5, str(data['start_time']), xlwt.easyxf("align: horiz left"))

        ws.write(18, 4, 'Финалы:', xlwt.easyxf("align: horiz left"))
        ws.write(18, 5, str(data['finals']), xlwt.easyxf("align: horiz left"))

        ws.write(20, 4, 'Погода:', xlwt.easyxf("align: horiz left"))
        ws.write(21, 4, 'Темп. старта:', xlwt.easyxf("align: horiz left"))
        ws.write(21, 5, str(data['start_temp']), xlwt.easyxf("align: horiz left"))

        ws.write(22, 4, 'Темп. финиша:', xlwt.easyxf("align: horiz left"))
        ws.write(22, 5, str(data['finish_temp']), xlwt.easyxf("align: horiz left"))

        ws.write(24, 4, 'Снег:', xlwt.easyxf("align: horiz left"))
        ws.write(24, 5, str(data['snow']), xlwt.easyxf("align: horiz left"))
        wb.save('test.xls')

    def save_participants_list(self, sheet_name, data, table):
        self.save_excel(sheet_name, data)
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        sheet = wb.get_sheet(1)
        sheet.write(27, 0, 'Ст№')
        sheet.write(27, 1, 'С.Ф.')
        sheet.write(27, 2, 'Фамилия Имя')
        sheet.write(27, 3, 'Г.р.')
        sheet.write(27, 4, 'Спорт. разряд')
        sheet.write(27, 5, 'Очки КР')
        sheet.write(27, 6, 'Внутренний рейтинг')
        for i in range(table.rowCount()):
            sheet.write(28 + i, 0, table.item(i, 0).text())
            sheet.write(28 + i, 1, table.item(i, 1).text())
            sheet.write(28 + i, 2, table.item(i, 2).text())
            sheet.write(28 + i, 3, table.item(i, 3).text())
            sheet.write(28 + i, 4, table.item(i, 4).text())
            sheet.write(28 + i, 5, table.item(i, 5).text())
            sheet.write(28 + i, 6, table.item(i, 6).text())
        wb.save('test.xls')

    def save_start_list_1(self, sheet_name, data, table1, table2):
        self.save_excel(sheet_name, data)
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        sheet = wb.get_sheet(2)
        sheet.write_merge(26, 26, 0, 6, 'КРАСНАЯ ТРАССА', xlwt.easyxf("align: horiz center"))
        sheet.write_merge(26, 26, 7, 13, 'СИНЯЯ ТРАССА', xlwt.easyxf("align: horiz center"))
        sheet.write(27, 1, 'Ст№')
        sheet.write(27, 2, 'С.Ф.')
        sheet.write(27, 3, 'Фамилия Имя')
        sheet.write(27, 4, 'Г.р.')
        sheet.write(27, 8, 'Ст№')
        sheet.write(27, 9, 'С.Ф.')
        sheet.write(27, 10, 'Фамилия Имя')
        sheet.write(27, 11, 'Г.р.')
        for i in range(table1.rowCount()):
            sheet.write(28 + i, 1, table1.item(i, 0).text())
            sheet.write(28 + i, 2, table1.item(i, 1).text())
            sheet.write(28 + i, 3, table1.item(i, 2).text())
            sheet.write(28 + i, 4, table1.item(i, 3).text())
        for i in range(table2.rowCount()):
            sheet.write(28 + i, 8, table2.item(i, 0).text())
            sheet.write(28 + i, 9, table2.item(i, 1).text())
            sheet.write(28 + i, 10, table2.item(i, 2).text())
            sheet.write(28 + i, 11, table2.item(i, 3).text())
        wb.save('test.xls')

    def save_res_1(self, sheet_name, data, table1):
        self.save_excel(sheet_name, data)
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        sheet = wb.get_sheet(3)
        sheet.write(27, 0, 'Место')
        sheet.write(27, 1, 'Ст№')
        sheet.write(27, 2, 'Фамилия Имя')
        sheet.write(27, 3, 'Время')
        sheet.write(27, 4, 'Трасса')
        for i in range(table1.rowCount()):
            sheet.write(28 + i, 0, table1.item(i, 0).text())
            sheet.write(28 + i, 1, table1.item(i, 1).text())
            sheet.write(28 + i, 2, table1.item(i, 2).text())
            sheet.write(28 + i, 3, table1.item(i, 3).text())
            sheet.write(28 + i, 4, table1.item(i, 4).text())
        wb.save('test.xls')

    def save_start_list_2(self, sheet_name, data, table1, table2):  # switch blueList and redList (?)
        self.save_excel(sheet_name, data)
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        sheet = wb.get_sheet(4)
        sheet.write_merge(26, 26, 0, 6, 'КРАСНАЯ ТРАССА', xlwt.easyxf("align: horiz center"))
        sheet.write_merge(26, 26, 7, 13, 'СИНЯЯ ТРАССА', xlwt.easyxf("align: horiz center"))
        sheet.write(27, 1, 'Ст№')
        sheet.write(27, 2, 'Фамилия Имя')
        sheet.write(27, 3, 'Время Q1')
        sheet.write(27, 8, 'Ст№')
        sheet.write(27, 9, 'Фамилия Имя')
        sheet.write(27, 10, 'Время Q1')
        for i in range(table1.rowCount()):
            sheet.write(28 + i, 1, table1.item(i, 0).text())
            sheet.write(28 + i, 2, table1.item(i, 1).text())
            sheet.write(28 + i, 3, table1.item(i, 2).text())
        for i in range(table2.rowCount()):
            sheet.write(28 + i, 8, table2.item(i, 0).text())
            sheet.write(28 + i, 9, table2.item(i, 1).text())
            sheet.write(28 + i, 10, table2.item(i, 2).text())
        wb.save('test.xls')

    def save_res_2(self, sheet_name, data, table1):
        self.save_excel(sheet_name, data)
        rb = xlrd.open_workbook('test.xls', formatting_info=True)
        wb = copy(rb)
        sheet = wb.get_sheet(5)
        sheet.write(27, 0, 'Место')
        sheet.write(27, 1, 'Ст№')
        sheet.write(27, 2, 'Фамилия Имя')
        sheet.write(27, 3, 'Время')
        sheet.write(27, 4, 'Трасса')
        for i in range(table1.rowCount()):
            sheet.write(28 + i, 0, table1.item(i, 0).text())
            sheet.write(28 + i, 1, table1.item(i, 1).text())
            sheet.write(28 + i, 2, table1.item(i, 2).text())
            sheet.write(28 + i, 3, table1.item(i, 4).text())
            sheet.write(28 + i, 4, table1.item(i, 5).text())
        wb.save('test.xls')

    def save_finals(self):
        pass
