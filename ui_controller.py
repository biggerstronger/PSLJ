import sys

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QPersistentModelIndex

import error_controller
import new_form
from data_controller import Data
from time import sleep


class Controller(QtWidgets.QMainWindow, new_form.Ui_MainWindow, Data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saveParams.clicked.connect(self.save_settings_callback)
        self.pushButtonLoadList.clicked.connect(self.load_file_callback)
        self.pushButtonAdd.clicked.connect(self.add_participant)
        self.pushButtonDelete.clicked.connect(self.delete_participant)
        self.pushButtonSave.clicked.connect(self.save_participants)
        self.pushButtonAccept.clicked.connect(self.display_resQ1_callback)
        self.pushButtonAccept_2.clicked.connect(self.display_resQ2_callback)
        self.error = error_controller.ErrorController()

    @staticmethod
    def setColorRed(table, rowIndex, cellIndex):
        table.item(rowIndex, cellIndex).setForeground(QtGui.QColor(255, 0, 0))

    @staticmethod
    def setColorBlue(table, rowIndex, cellIndex):
        table.item(rowIndex, cellIndex).setForeground(QtGui.QColor(0, 0, 255))

    def counter(self):
        x = self.participantsTable.rowCount()
        return x + 1

    def add_participant(self):
        self.participantsTable.insertRow(0)
        self.counter()
        self.participantsTable.setItem(0, 0, QtWidgets.QTableWidgetItem(' '))
        self.participantsTable.setItem(0, 1, QtWidgets.QTableWidgetItem(' '))
        self.participantsTable.setItem(0, 2, QtWidgets.QTableWidgetItem(' '))
        self.participantsTable.setItem(0, 3, QtWidgets.QTableWidgetItem(' '))
        self.participantsTable.setItem(0, 4, QtWidgets.QTableWidgetItem(' '))
        self.participantsTable.setItem(0, 5, QtWidgets.QTableWidgetItem(' '))

    def save_participants(self):
        for i in range(1, self.counter()):
            part_data = {}
            part_data.setdefault('Ст№', self.participantsTable.item(i - 1, 0).text())
            part_data.setdefault('С.Ф.', self.participantsTable.item(i - 1, 1).text())
            part_data.setdefault('Фамилия Имя', self.participantsTable.item(i - 1, 2).text())
            part_data.setdefault('Г.р.', self.participantsTable.item(i - 1, 3).text())
            part_data.setdefault('Спорт. разр.', self.participantsTable.item(i - 1, 4).text())
            part_data.setdefault('Очки КР', self.participantsTable.item(i - 1, 5).text())
            part_data.setdefault('QT1_course', None)
            part_data.setdefault('QT_1', None)
            part_data.setdefault('QT2_course', None)
            part_data.setdefault('QT_2', None)
            part_data.setdefault('FT1/32_course', None)
            part_data.setdefault('FT1/32_1', None)
            part_data.setdefault('FT1/32_2', None)
            part_data.setdefault('FT1/16_course', None)
            part_data.setdefault('FT1/16_1', None)
            part_data.setdefault('FT1/16_2', None)
            part_data.setdefault('FT1/8_course', None)
            part_data.setdefault('FT1/8_1', None)
            part_data.setdefault('FT1/8_2', None)
            part_data.setdefault('FT1/4_course', None)
            part_data.setdefault('FT1/4_1', None)
            part_data.setdefault('FT1/4_2', None)
            part_data.setdefault('FTSmall_course', None)
            part_data.setdefault('FTSmall_1', None)
            part_data.setdefault('FTSmall_2', None)
            part_data.setdefault('FTBig_course', None)
            part_data.setdefault('FTBig_1', None)
            part_data.setdefault('FTBig_2', None)
            Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())] = part_data
            if Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]['Ст№'] == ' ' and \
                    Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]['Фамилия Имя'] == ' ':
                del Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]
                self.error.show()
                self.error.error_msg_double(i)
                continue
            if Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]['Ст№'] == ' ':
                del Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]
                self.error.error_msg_bib(i)
                self.error.show()
                continue
            if Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]['Фамилия Имя'] == ' ':
                del Data._participants_data[str(self.participantsTable.item(i - 1, 0).text())]
                self.error.show()
                self.error.error_msg_fio(i)
                continue
            self.divideQ1(Data._participants_data)

    def delete_participant(self):
        if self.participantsTable.selectionModel().hasSelection():
            indexes = [QPersistentModelIndex(index) for index in self.participantsTable.selectionModel().selectedRows()]
            for index in sorted(indexes):
                print('Deleting row %d...' % index.row())
                try:
                    Data._participants_data.pop(str(self.participantsTable.item(index.row(), 0).text()))
                    self.participantsTable.removeRow(index.row())
                except:
                    self.participantsTable.removeRow(index.row())
        else:
            print('No row selected!')

    def display_resQ1_callback(self):
        sleep(1)
        self.tabWidget.setCurrentIndex(3)
        self.display_res_q1(Data._participants_data)
        self.sort_res_q1(Data._participants_data)
        if self.competition_data['Q_amount'] == '2':
            self.divideQ2()

    def display_resQ2_callback(self):
        sleep(1)  # TODO пофиксить переключение вкладок
        self.tabWidget.setCurrentIndex(4)
        self.display_res_q2()
        self.sort_res_q2()

    def save_settings_callback(self):
        Data.save_settings(self)
        sleep(1)
        self.tabWidget.setCurrentIndex(1)
        print('Данные сохранены!')
        # self.show_finals()

    def load_file_callback(self):
        Data.choose_file_participants(self)
        Data.load_file(self)
        self.display_participants(Data._participants_data)

    def display_participants(self, data):
        self.participantsTable.setRowCount(0)
        row = 0
        for entry in range(1, len(data) + 1):
            self.participantsTable.insertRow(row)
            self.participantsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Ст№'])))
            self.participantsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['С.Ф.'])))
            self.participantsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Фамилия Имя'])))
            self.participantsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Г.р.'])))
            self.participantsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Спорт. разр.'])))
            self.participantsTable.setItem(row, 5, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Очки КР'])))
            # self.participantsTable.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
            row += 1

    def divideQ1(self, data):
        self.redListQ1.setRowCount(0)
        self.blueListQ1.setRowCount(0)
        n = m = 0
        for t in data:
            if int(data[str(t)]['Ст№']) % 2 == 1:
                self.redListQ1.insertRow(n)
                self.redListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(data[str(t)]['Ст№'])))
                self.redListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(data[str(t)]['С.Ф.'])))
                self.redListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(data[str(t)]['Фамилия Имя'])))
                self.redListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(data[str(t)]['Спорт. разр.'])))
                data[str(t)]['QT1_course'] = 'Красная'
                n += 1
            else:
                self.blueListQ1.insertRow(m)
                self.blueListQ1.setItem(m, 0, QtWidgets.QTableWidgetItem(str(data[str(t)]['Ст№'])))
                self.blueListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(data[str(t)]['С.Ф.'])))
                self.blueListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(data[str(t)]['Фамилия Имя'])))
                self.blueListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(data[str(t)]['Спорт. разр.'])))
                data[str(t)]['QT1_course'] = 'Синяя'
                m += 1
        self.redListQ1.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.blueListQ1.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

    def display_res_q1(self, data):
        Data.get_time_qual1(self)
        self.RedUnsortListQ1.setRowCount(0)
        self.BlueUnsortListQ1.setRowCount(0)
        n = m = 0
        for x in data:
            if data[x]['QT1_course'] == 'Красная':
                self.RedUnsortListQ1.insertRow(n)
                self.RedUnsortListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(data[str(x)]['Ст№'])))
                self.RedUnsortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(data[str(x)]['Фамилия Имя'])))
                self.RedUnsortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT_1'])))
                self.RedUnsortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT1_course'])))
                self.setColorRed(self.RedUnsortListQ1, n, 3)
                n += 1
            else:
                self.BlueUnsortListQ1.insertRow(m)
                self.BlueUnsortListQ1.setItem(m, 0, QtWidgets.QTableWidgetItem(str(data[str(x)]['Ст№'])))
                self.BlueUnsortListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(data[str(x)]['Фамилия Имя'])))
                self.BlueUnsortListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT_1'])))
                self.BlueUnsortListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT1_course'])))
                self.setColorBlue(self.BlueUnsortListQ1, m, 3)
                m += 1

    def sort_res_q1(self, data):
        self.ResSortListQ1.setRowCount(0)
        n = 0
        place = 1
        break_flag = len(Data._participants_data) // 2 + 2 if len(Data._participants_data) % 2 == 0 else len(
            Data._participants_data) // 2 + 1
        for x in data:
            self.ResSortListQ1.insertRow(n)
            self.ResSortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(data[str(x)]['Ст№'])))
            self.ResSortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(data[str(x)]['Фамилия Имя'])))
            self.ResSortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT_1'])))
            self.ResSortListQ1.setItem(n, 4, QtWidgets.QTableWidgetItem(str(data[str(x)]['QT1_course'])))
            if data[str(x)]['QT1_course'] == 'Красная':
                self.setColorRed(self.ResSortListQ1, n, 4)
            else:
                self.setColorBlue(self.ResSortListQ1, n, 4)
            n += 1
        self.ResSortListQ1.sortItems(3)
        self.ResSortListQ1.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1)))
        for _ in range(1, break_flag + 1):
            if self.ResSortListQ1.item(_, 4).text() == self.ResSortListQ1.item(_ - 1, 4).text():
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            else:
                place = _ + 1
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
        for _ in range(break_flag, len(data)):
            self.ResSortListQ1.removeRow(break_flag)

    def divideQ2(self):
        self.redListQ2.setRowCount(0)
        self.blueListQ2.setRowCount(0)
        m = n = 0
        for t in range(1, self.ResSortListQ1.rowCount() + 1):
            if int(self.ResSortListQ1.item(t - 1, 1).text()) % 2 == 0:
                self.redListQ2.insertRow(n)
                self.redListQ2.setItem(n, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 1).text())))
                self.redListQ2.setItem(n, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 2).text())))
                self.redListQ2.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 3).text())))
                Data._participants_data[str(self.ResSortListQ1.item(t - 1, 1).text())]['QT2_course'] = 'Красная'
                n += 1
            else:
                self.blueListQ2.insertRow(m)
                self.blueListQ2.setItem(m, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 1).text())))
                self.blueListQ2.setItem(m, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 2).text())))
                self.blueListQ2.setItem(m, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 3).text())))
                Data._participants_data[str(self.ResSortListQ1.item(t - 1, 1).text())]['QT2_course'] = 'Синяя'
                m += 1
        self.redListQ2.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.blueListQ2.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        # self.blueListQ2.column(0).

    def display_res_q2(self):
        Data.get_time_qual2(self)
        self.RedUnsortListQ2.setRowCount(0)
        self.BlueUnsortListQ2.setRowCount(0)
        for n in range(self.redListQ2.rowCount()):
            self.RedUnsortListQ2.insertRow(n)
            self.RedUnsortListQ2.setItem(n, 0,
                                         QtWidgets.QTableWidgetItem(str(self.redListQ2.item(n, 0).text())))
            self.RedUnsortListQ2.setItem(n, 1,
                                         QtWidgets.QTableWidgetItem(str(self.redListQ2.item(n, 1).text())))
            self.RedUnsortListQ2.setItem(n, 2,
                                         QtWidgets.QTableWidgetItem(str(
                                             Data._participants_data[str(self.redListQ2.item(n, 0).text())]['QT_2'])))
            self.RedUnsortListQ2.setItem(n, 3,
                                         QtWidgets.QTableWidgetItem(str(
                                             Data._participants_data[str(self.redListQ2.item(n, 0).text())][
                                                 'QT2_course'])))
            self.setColorRed(self.RedUnsortListQ2, n, 3)
        for m in range(self.blueListQ2.rowCount()):
            self.BlueUnsortListQ2.insertRow(m)
            self.BlueUnsortListQ2.setItem(m, 0,
                                          QtWidgets.QTableWidgetItem(str(self.blueListQ2.item(m, 0).text())))
            self.BlueUnsortListQ2.setItem(m, 1,
                                          QtWidgets.QTableWidgetItem(str(self.blueListQ2.item(m, 1).text())))
            self.BlueUnsortListQ2.setItem(m, 2, QtWidgets.QTableWidgetItem(
                str(Data._participants_data[str(self.blueListQ2.item(m, 0).text())]['QT_2'])))
            self.BlueUnsortListQ2.setItem(m, 3,
                                          QtWidgets.QTableWidgetItem(
                                              str(Data._participants_data[str(self.blueListQ2.item(m, 0).text())][
                                                      'QT2_course'])))
            self.setColorBlue(self.BlueUnsortListQ2, m, 3)

    def sort_res_q2(self):
        self.ResSortListQ2.setRowCount(0)
        place = 1
        break_flag = int(self.competition_data['rounds_amount'].split(sep='/')[1]) * 2
        for n in range(self.ResSortListQ1.rowCount()):
            self.ResSortListQ2.insertRow(n)
            self.ResSortListQ2.setItem(n, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 1).text())))
            self.ResSortListQ2.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 2).text())))
            self.ResSortListQ2.setItem(n, 3, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 3).text())))
            self.ResSortListQ2.setItem(n, 4, QtWidgets.QTableWidgetItem(
                str(Data._participants_data[str(self.ResSortListQ1.item(n, 1).text())]['QT_2'])))
            self.ResSortListQ2.setItem(n, 5, QtWidgets.QTableWidgetItem(
                str(Data._participants_data[str(self.ResSortListQ1.item(n, 1).text())]['QT2_course'])))
            if Data._participants_data[str(self.ResSortListQ1.item(n, 1).text())]['QT2_course'] == 'Красная':
                self.setColorRed(self.ResSortListQ2, n, 5)
            else:
                self.setColorBlue(self.ResSortListQ2, n, 5)
        self.ResSortListQ2.sortItems(4)
        self.ResSortListQ2.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1)))
        for _ in range(1, break_flag):
            if self.ResSortListQ2.item(_, 4).text() == self.ResSortListQ2.item(_ - 1, 4).text():
                self.ResSortListQ2.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            else:
                place = _ + 1
                self.ResSortListQ2.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
        for _ in range(break_flag, self.ResSortListQ1.rowCount()):
            self.ResSortListQ2.removeRow(break_flag)

    def show_finals(self):
        # self.tableWidgetFinals.setRowCount(0)
        # for i in range(0, 16):
        #     self.tableWidgetFinals.setItem(i, 1, QtWidgets.QTableWidgetItem(self.))
        #     self.tableWidgetFinals.setItem(i, 1, QtWidgets.QTableWidgetItem('Красная'))
        #     self.tableWidgetFinals.setItem(i, 3, QtWidgets.QTableWidgetItem('Синяя'))
        #
        # # else:
        # #     pass
        # if self.radioButtonBF_SF.isChecked():
        pass
