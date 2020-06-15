import xlwt
import xlrd
from xlutils.copy import copy


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
        ws.write_merge(3, 3, 0, 6, '{}'.format('test'), xlwt.easyxf("align: horiz center"))
        ws.write_merge(5, 5, 0, 6, '{}'.format(data['type']), xlwt.easyxf("align: horiz center"))
        ws.write_merge(7, 7, 0, 1, '{}'.format('Организаторы:'), xlwt.easyxf("align: horiz left"))
        # TODO set column width depending on len(data)
        ws.write_merge(7, 7, 2, 3, '{}'.format(data['orgs']), xlwt.easyxf("align: horiz left"))
        ws.write_merge(7, 7, 4, 5, 'Информация о трассе:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 0, 2, 'Главная Судейская Комиссия', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 4, 4, 'Название трассы:', xlwt.easyxf("align: horiz left"))
        ws.write_merge(9, 9, 5, 5, 'Название трассы:', xlwt.easyxf("align: horiz left"))
        # TODO add 'название трассы' into competiton_data

        wb.save('test.xls')
