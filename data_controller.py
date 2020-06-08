import json
import random
import xlrd
from datetime import time
from PySide2 import QtWidgets


def write_to_json(data_dict):
    with open("main_data.json", 'w') as f:
        json.dump(data_dict, f)


class Data:
    file_path = None
    _participants_data = {}
    competition_data = {}

    def get_time_qual1(self):
        for _ in self._participants_data:
            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            self._participants_data[str(_)]['QT_1'] = str(time(minute=min_time, second=sec_time, microsecond=micro_time))[3:]

    def get_time_qual2(self):
        for _ in self._participants_data:
            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            self._participants_data[str(_)]['QT_2'] = str(time(minute=min_time, second=sec_time, microsecond=micro_time))[3:]

    def save_settings(self):
        self.competition_data = {
            'title': self.titlelineEdit.text(),
            'place': self.datelineEdit.text(),
            'type': self.typelineEdit.text(),
            'orgs': self.orglineEdit.text(),
            'Q_amount': self.qualificationsComboBox.currentText(),
            'run_amount': self.runsComboBox.currentText(),
            'rounds_amount': self.roundsComboBox.currentText(),

            'delegat': [self.fio1.text(), self.city1.text()],
            'director': [self.fio2.text(), self.city2.text()],
            'referee': [self.fio3.text(), self.city3.text()],
            'secretary': [self.fio4.text(), self.city4.text()],
            'track_chief': [self.fio5.text(), self.city5.text()],
            'start_referee': [self.fio6.text(), self.city6.text()],
            'track_dir': [self.fio7.text(), self.city7.text()],
            'opener1': [self.fio8.text(), self.city8.text()],
            'opener2': [self.fio9.text(), self.city9.text()],

            'track_name': self.trackName.text(),
            'start': self.start.text(),
            'finish': self.finish.text(),
            'alt_dif': self.altitudeDiff.text(),
            'homologation': self.homologation.text(),
            'gates_amount': self.gates.text(),
            'track_len': self.length.text(),
            'start_time': self.startTime.text(),
            'finals': self.finalsTime.text(),

            'start_temp': self.startTemp.text(),
            'finish_temp': self.finishTemp.text(),
            'snow': self.snow.text()

        }
        if self.competition_data["Q_amount"] == '1':
            self.CC_Q_2_Tab.setDisabled(1)
            self.RES_Q_2_Tab.setDisabled(1)
        write_to_json(self.competition_data)

    def choose_file_participants(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                          "Excel Files (*.xls?)")
        if file_name[0]:
            self.file_path = file_name[0]
            self.fileNameLabel.setText(file_name[0])

    def load_settings(self):
        wb = xlrd.open_workbook(str(self.file_path))
        for sheet in wb.sheets():
            if sheet.name == "Шаблон":
                xlstime = xlrd.xldate_as_tuple(sheet.cell(34, 1).value, wb.datemode)
                stime = time(*xlstime[3:])
                xlftime = xlrd.xldate_as_tuple(sheet.cell(35, 1).value, wb.datemode)
                ftime = time(*xlftime[3:])
                self.titlelineEdit.setText(sheet.cell(1, 1).value)
                self.datelineEdit.setText(sheet.cell(2, 1).value)
                self.typelineEdit.setText(sheet.cell(4, 1).value)
                self.orglineEdit.setText(sheet.cell(6, 1).value)

                self.fio1.setText(sheet.cell(9, 1).value)
                self.city1.setText(sheet.cell(9, 2).value)
                self.fio2.setText(sheet.cell(10, 1).value)
                self.city2.setText(sheet.cell(10, 2).value)
                self.fio3.setText(sheet.cell(11, 1).value)
                self.city3.setText(sheet.cell(11, 2).value)
                self.fio4.setText(sheet.cell(12, 1).value)
                self.city4.setText(sheet.cell(12, 2).value)
                self.fio5.setText(sheet.cell(14, 1).value)
                self.city5.setText(sheet.cell(14, 2).value)
                self.fio6.setText(sheet.cell(15, 1).value)
                self.city6.setText(sheet.cell(15, 2).value)
                self.fio7.setText(sheet.cell(17, 1).value)
                self.city7.setText(sheet.cell(17, 2).value)
                self.fio8.setText(sheet.cell(19, 1).value)
                self.city8.setText(sheet.cell(19, 2).value)
                self.fio9.setText(sheet.cell(20, 1).value)
                self.city9.setText(sheet.cell(20, 2).value)

                self.trackName.setText(sheet.cell(26, 1).value)
                self.start.setText(sheet.cell(28, 1).value)
                self.finish.setText(sheet.cell(29, 1).value),
                self.altitudeDiff.setText(sheet.cell(30, 1).value)
                self.homologation.setText(sheet.cell(31, 1).value)
                self.gates.setText(str(int(sheet.cell(32, 1).value)))
                self.length.setText(sheet.cell(33, 1).value)
                self.startTime.setText(str(stime))
                self.finalsTime.setText(str(ftime))

                self.startTemp.setText(str(sheet.cell(38, 1).value))
                self.finishTemp.setText(str(sheet.cell(39, 1).value))
                self.snow.setText(sheet.cell(41, 1).value)

    def load_file(self):
        wb = xlrd.open_workbook(str(self.file_path))
        for sheet in wb.sheets():
            if sheet.name == "Список Участников":
                rows = sheet.nrows
                columns = sheet.ncols
                column_names = [sheet.cell(27, column_index).value for column_index in range(columns)]
                for row_index in range(28, rows):
                    part_data = {}
                    for column_index, column_name in enumerate(column_names):
                        if column_index != 0:
                            part_data[column_name] = sheet.cell(row_index, column_index).value
                        else:
                            part_data[column_name] = int(sheet.cell(row_index, column_index).value)
                    part_data.setdefault('QT1_course', None)
                    part_data.setdefault('QT_1', None)
                    part_data.setdefault('QT2_course', None)
                    part_data.setdefault('QT_2', None)
                    self._participants_data['{}'.format(part_data['Ст№'])] = part_data
        # print(self._participants_data)
