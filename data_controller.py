import json

import xlrd

from PySide2 import QtWidgets


def write_to_json(data_dict):
    with open("main_data.json", 'w') as f:
        json.dump(data_dict, f)


class Data:
    file_path = None
    _participants_data = []
    _competition_data = {}

    def save_settings(self):
        self._competition_data = {
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
            'finals': self.finals.text(),

            'start_temp': self.startTemp.text(),
            'finish_temp': self.finishTemp.text(),
            'snow': self.snow.text()

        }
        if self._competition_data["Q_amount"] == '1':
            self.CC_Q_2_Tab.setDisabled(1)
            self.RES_Q_2_Tab.setDisabled(1)
        write_to_json(self._competition_data)
        print(self._competition_data)

    def choose_file_participants(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                          "Excel Files (*.xls?)")
        if file_name[0]:
            self.file_path = file_name[0]
            self.fileNameLabel.setText(file_name[0])

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
                    part_data.setdefault('QT_course', None)
                    part_data.setdefault('QT_1', None)
                    part_data.setdefault('QT_2', None)
                    part_data.setdefault('FT32_course', None)
                    part_data.setdefault('FT32_1', None)
                    part_data.setdefault('FT32_2', None)
                    part_data.setdefault('FT16_course', None)
                    part_data.setdefault('FT16_1', None)
                    part_data.setdefault('FT16_2', None)
                    part_data.setdefault('FT8_course', None)
                    part_data.setdefault('FT8_1', None)
                    part_data.setdefault('FT8_2', None)
                    part_data.setdefault('FT4_course', None)
                    part_data.setdefault('FT4_1', None)
                    part_data.setdefault('FT4_2', None)
                    part_data.setdefault('FTSmall_course', None)
                    part_data.setdefault('FTSmall_1', None)
                    part_data.setdefault('FTSmall_2', None)
                    part_data.setdefault('FTBig_course', None)
                    part_data.setdefault('FTBig_1', None)
                    part_data.setdefault('FTBig_2', None)
                    self._participants_data.append(part_data)
        # print(self._participants_data)
