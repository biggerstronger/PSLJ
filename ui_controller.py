import os

import xlrd
from PySide2 import QtCore, QtWidgets, QtGui
import json
import new_form


class Controller(QtWidgets.QMainWindow, new_form.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.file_path = None
        self._competitors_data = []
        self._participants_data = []
        self.setupUi(self)
        self.saveParams.clicked.connect(self.save_settings_callback)
        self.pushButtonLoadList.clicked.connect(self.load_file_callback)

    def save_settings_callback(self):
        self.save_settings()
        print("Данные сохранены!")

    def load_file_callback(self):
        self.choose_file_participants()
        self.load_file(self.file_path)
        self.display_participants(self._participants_data)
        self.divide(self._participants_data)

    def save_settings(self):
        competition_data = {
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
        if competition_data["Q_amount"] == '1':
            self.CC_Q_2_Tab.setDisabled(1)
            self.RES_Q_2_Tab.setDisabled(1)
        self.write_to_json(competition_data)

    def write_to_json(self, data_dict):
        with open("main_data.json", 'w') as f:
            json.dump(data_dict, f)

    def choose_file_participants(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                          "Excel Files (*.xls?)")
        if file_name[0]:
            self.file_path = file_name[0]
            self.fileNameLabel.setText(file_name[0])

    def display_participants(self, data):
        if os.path.isfile(self.file_path):
            print("SUCCESS")
        else:
            print("ERROR")

        self.participantsTable.setRowCount(0)
        row = 0
        for entry in data:
            self.participantsTable.insertRow(row)
            # self.participantsTable.setItem(row_number, 0, QtWidgets.QTableWidgetItem(int(data[row_number]["Ст№"])))
            self.participantsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry["С.Ф."])))
            self.participantsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["Фамилия Имя"])))
            self.participantsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry["Г.р."])))
            self.participantsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry["Спорт. разр."])))
            self.participantsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry["Очки КР"])))
            row += 1

    def divide(self, data):
        if os.path.isfile(self.file_path):
            print("SUCCESS")
        else:
            print("ERROR")

        self.redListQ1.setRowCount(0)
        self.blueListQ1.setRowCount(0)
        t = n = m = 0
        for x in data:
            if data[t]['Ст№'] % 2 == 1:
                self.redListQ1.insertRow(n)
                self.redListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(int(x["Ст№"])))
                self.redListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x["С.Ф."])))
                self.redListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
                self.redListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
                self.redListQ1.setItem(n, 4, QtWidgets.QTableWidgetItem(str(x["Спорт. разр."])))
                n += 1
            else:
                self.blueListQ1.insertRow(m)
                self.blueListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(x["С.Ф."])))
                self.blueListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
                self.blueListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
                self.blueListQ1.setItem(m, 4, QtWidgets.QTableWidgetItem(str(x["Спорт. разр."])))
                m += 1
            t += 1

    def load_file(self, file_name):
        wb = xlrd.open_workbook(str(file_name))
        for sheet in wb.sheets():
            if sheet.name == "Список Участников":
                rows = sheet.nrows
                columns = sheet.ncols
                column_names = [sheet.cell(27, column_index).value for column_index in range(columns)]
                for row_index in range(28, rows):
                    part_data = {}
                    for column_index, column_name in enumerate(column_names):
                        part_data[column_name] = sheet.cell(row_index, column_index).value
                    self._participants_data.append(part_data)
