import random
from datetime import time

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QPersistentModelIndex, Qt

import error_controller
import new_form
from data_controller import Data
from time import sleep


class Controller(QtWidgets.QMainWindow, new_form.Ui_MainWindow, Data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonLoadSettings.clicked.connect(self.load_settings_callback)
        self.saveParams.clicked.connect(self.save_settings_callback)
        self.pushButtonLoadList.clicked.connect(self.load_file_callback)
        self.pushButtonAdd.clicked.connect(self.add_participant)
        self.pushButtonDelete.clicked.connect(self.delete_participant)
        self.pushButtonSave.clicked.connect(self.save_participants)
        self.pushButtonAccept.clicked.connect(self.display_resQ1_callback)
        self.pushButtonTime1.clicked.connect(self.manual_time_1)
        self.pushButtonAccept_2.clicked.connect(self.display_resQ2_callback)
        self.pushButtonTime2.clicked.connect(self.manual_time_2)
        self.pushButtonAcceptRes.clicked.connect(self.res_callback)
        self.pushButtonSet_bibs.clicked.connect(self.set_bibs)
        self.pushButtonShowFinals.clicked.connect(self.show_finals)
        self.pushButtonConfirmFinalTime.clicked.connect(self.confirm_final_time)
        self.comboBoxFinals.currentIndexChanged.connect(self.finals)
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
        self.participantsTable.setItem(0, 0, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 1, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 2, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 3, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 4, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 5, QtWidgets.QTableWidgetItem(''))
        self.participantsTable.setItem(0, 5, QtWidgets.QTableWidgetItem(''))

    def save_participants(self):
        Data._participants_data.clear()
        for i in range(0, self.counter() - 1):
            part_data = {}
            try:
                part_data.setdefault('Ст№', int(self.participantsTable.item(i, 0).text()))
            except ValueError:
                self.error.show()
                self.error.wrong_bib_type(i + 1)
                break
            if self.counter() >= 2:
                for j in range(i + 1, self.counter() - 1):
                    if self.participantsTable.item(i, 0).text() == self.participantsTable.item(j, 0).text():
                        self.error.show()
                        self.error.wrong_bib(i + 1, j + 1)
                        break
            part_data.setdefault('С.Ф.', self.participantsTable.item(i, 1).text())
            part_data.setdefault('Фамилия Имя', self.participantsTable.item(i, 2).text())
            part_data.setdefault('Г.р.', self.participantsTable.item(i, 3).text())
            part_data.setdefault('Спорт. разр.', self.participantsTable.item(i, 4).text())
            part_data.setdefault('Очки КР', self.participantsTable.item(i, 5).text())
            part_data.setdefault('Внутренний рейтинг', self.participantsTable.item(i, 6).text())
            part_data.setdefault('QT1_course', None)
            part_data.setdefault('QT_1', None)
            part_data.setdefault('QT2_course', None)
            part_data.setdefault('QT_2', None)
            Data._participants_data[str(self.participantsTable.item(i, 0).text())] = part_data
            if Data._participants_data[str(self.participantsTable.item(i, 0).text())]['Ст№'] == '' and \
                    Data._participants_data[str(self.participantsTable.item(i, 0).text())]['Фамилия Имя'] == '':
                del Data._participants_data[str(self.participantsTable.item(i, 0).text())]
                self.error.show()
                self.error.error_msg_double(i + 1)
                break
            if Data._participants_data[str(self.participantsTable.item(i, 0).text())]['Ст№'] == '':
                del Data._participants_data[str(self.participantsTable.item(i, 0).text())]
                self.error.show()
                self.error.error_msg_bib(i + 1)
                break
            if Data._participants_data[str(self.participantsTable.item(i, 0).text())]['Фамилия Имя'] == '':
                del Data._participants_data[str(self.participantsTable.item(i, 0).text())]
                self.error.show()
                self.error.error_msg_fio(i + 1)
                break
            else:
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
        self.set_bibs()

    def display_resQ1_callback(self):
        sleep(1)
        self.tabWidget.setCurrentIndex(3)
        self.display_res_q1(Data._participants_data)

    def display_resQ2_callback(self):
        sleep(1)
        self.tabWidget.setCurrentIndex(5)
        self.display_res_q2()

    def save_settings_callback(self):
        Data.save_settings(self)
        sleep(1)
        self.tabWidget.setCurrentIndex(1)
        print('Данные сохранены!')

    def load_settings_callback(self):
        Data.choose_file_participants(self)
        Data.load_settings(self)

    def load_file_callback(self):
        Data.choose_file_participants(self)
        Data.load_file(self)
        self.display_participants(Data._participants_data)

    def res_callback(self):
        default_fin = int(self.competition_data['rounds_amount'].split(sep='/')[1])
        while default_fin >= 2:
            self.comboBoxFinals.addItem('1/' + str(default_fin))
            default_fin = int(default_fin / 2)
        self.comboBoxFinals.addItem('BF|SF')
        if self.competition_data['Q_amount'] == '2':
            sleep(1)
            self.tabWidget.setCurrentIndex(4)
            self.divideQ2()
        else:
            sleep(1)
            self.tabWidget.setCurrentIndex(6)
            self.show_finals()

    def display_participants(self, data):
        self.participantsTable.setRowCount(0)
        row = 0
        for entry in range(1, len(data) + 1):
            self.participantsTable.insertRow(row)
            self.participantsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['С.Ф.'])))
            self.participantsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Фамилия Имя'])))
            self.participantsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Г.р.'])))
            self.participantsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(
                str(data['{}'.format(entry)]['Спорт. разр.'])))
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, int(data['{}'.format(entry)]['Очки КР']))
            self.participantsTable.setItem(row, 5, item)
            item = QtWidgets.QTableWidgetItem()
            item.setData(Qt.EditRole, int(data['{}'.format(entry)]['Внутренний рейтинг']))
            self.participantsTable.setItem(row, 6, item)
            row += 1
        self.participantsTable.sortItems(0, Qt.DescendingOrder)

    def set_bibs(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        random.shuffle(a)
        for i in range(self.participantsTable.rowCount()):
            if self.participantsTable.item(i, 6).text() == '':
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.EditRole, 0)
                self.participantsTable.setItem(i, 6, item)
            if self.participantsTable.item(i, 5).text() == '':
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.EditRole, 0)
                self.participantsTable.setItem(i, 5, item)

        self.participantsTable.sortItems(5, Qt.DescendingOrder)
        for i in range(self.participantsTable.rowCount()):
            for j in range(1, self.participantsTable.rowCount()):
                if int(self.participantsTable.item(i, 5).text()) == int(self.participantsTable.item(j, 5).text()) and \
                        int(self.participantsTable.item(i, 6).text()) > int(self.participantsTable.item(j, 6).text()):
                    temp = [self.participantsTable.item(i, 1).text(),
                            self.participantsTable.item(i, 2).text(),
                            self.participantsTable.item(i, 3).text(),
                            self.participantsTable.item(i, 4).text(),
                            self.participantsTable.item(i, 5).text(),
                            self.participantsTable.item(i, 6).text()]
                    self.participantsTable.setItem(i, 1,
                                                   QtWidgets.QTableWidgetItem(self.participantsTable.item(j, 1).text()))
                    self.participantsTable.setItem(i, 2,
                                                   QtWidgets.QTableWidgetItem(self.participantsTable.item(j, 2).text()))
                    self.participantsTable.setItem(i, 3,
                                                   QtWidgets.QTableWidgetItem(self.participantsTable.item(j, 3).text()))
                    self.participantsTable.setItem(i, 4,
                                                   QtWidgets.QTableWidgetItem(self.participantsTable.item(j, 4).text()))
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole, int(self.participantsTable.item(j, 5).text()))
                    self.participantsTable.setItem(i, 5, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setData(Qt.EditRole, int(self.participantsTable.item(j, 6).text()))
                    self.participantsTable.setItem(i, 6, item)

                    self.participantsTable.setItem(j, 1, QtWidgets.QTableWidgetItem(temp[0]))
                    self.participantsTable.setItem(j, 2, QtWidgets.QTableWidgetItem(temp[1]))
                    self.participantsTable.setItem(j, 3, QtWidgets.QTableWidgetItem(temp[2]))
                    self.participantsTable.setItem(j, 4, QtWidgets.QTableWidgetItem(temp[3]))
                    self.participantsTable.setItem(j, 5, QtWidgets.QTableWidgetItem(temp[4]))
                    self.participantsTable.setItem(j, 6, QtWidgets.QTableWidgetItem(temp[5]))

        for i in range(0, 16):
            self.participantsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(a[i])))
        for i in range(16, self.participantsTable.rowCount()):
            self.participantsTable.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))

    def divideQ1(self, data):
        self.redListQ1.setRowCount(0)
        self.blueListQ1.setRowCount(0)
        n = m = 0
        for t in data:
            if int(data[str(t)]['Ст№']) % 2 == 1:
                self.redListQ1.insertRow(n)
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.DisplayRole, data[str(t)]['Ст№'])
                self.redListQ1.setItem(n, 0, item)
                self.redListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(data[str(t)]['С.Ф.'])))
                self.redListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(data[str(t)]['Фамилия Имя'])))
                self.redListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(data[str(t)]['Спорт. разр.'])))
                data[str(t)]['QT1_course'] = 'Красная'
                self.redListQ1.item(n, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.redListQ1.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.redListQ1.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.redListQ1.item(n, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                n += 1
            else:
                self.blueListQ1.insertRow(m)
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.DisplayRole, data[str(t)]['Ст№'])
                self.blueListQ1.setItem(m, 0, item)
                self.blueListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(data[str(t)]['С.Ф.'])))
                self.blueListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(data[str(t)]['Фамилия Имя'])))
                self.blueListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(data[str(t)]['Спорт. разр.'])))
                data[str(t)]['QT1_course'] = 'Синяя'
                self.blueListQ1.item(m, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.blueListQ1.item(m, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.blueListQ1.item(m, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.blueListQ1.item(m, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                m += 1

            self.redListQ1.sortItems(0)
            self.blueListQ1.sortItems(0)

    def display_res_q1(self, data):
        self.get_time_qual1()
        self.RedUnsortListQ1.setRowCount(0)
        self.BlueUnsortListQ1.setRowCount(0)
        n = m = 0
        for x in data:
            if data[x]['QT1_course'] == 'Красная':
                self.RedUnsortListQ1.insertRow(n)
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.DisplayRole, data[str(x)]['Ст№'])
                self.RedUnsortListQ1.setItem(n, 0, item)
                self.RedUnsortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(data[str(x)]['С.Ф.'])))
                self.RedUnsortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(data[str(x)]['Фамилия Имя'])))
                self.RedUnsortListQ1.setItem(n, 3,
                                             QtWidgets.QTableWidgetItem(Data._participants_data[str(n + 1)]['QT_1']))
                self.RedUnsortListQ1.item(n, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.RedUnsortListQ1.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.RedUnsortListQ1.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                n += 1
            else:
                self.BlueUnsortListQ1.insertRow(m)
                item = QtWidgets.QTableWidgetItem()
                item.setData(Qt.DisplayRole, data[str(x)]['Ст№'])
                self.BlueUnsortListQ1.setItem(m, 0, item)
                self.BlueUnsortListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(data[str(x)]['С.Ф.'])))
                self.BlueUnsortListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(data[str(x)]['Фамилия Имя'])))
                self.BlueUnsortListQ1.setItem(m, 3,
                                              QtWidgets.QTableWidgetItem(Data._participants_data[str(n + 1)]['QT_1']))
                self.BlueUnsortListQ1.item(m, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.BlueUnsortListQ1.item(m, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.BlueUnsortListQ1.item(m, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                m += 1
        self.RedUnsortListQ1.sortItems(0)
        self.BlueUnsortListQ1.sortItems(0)

    def manual_time_1(self):
        for i in range(self.RedUnsortListQ1.rowCount()):
            Data._participants_data[str(self.RedUnsortListQ1.item(i, 0).text())]['QT_1'] = self.RedUnsortListQ1.item(i,
                                                                                                                     3).text()
        for i in range(self.BlueUnsortListQ1.rowCount()):
            Data._participants_data[str(self.BlueUnsortListQ1.item(i, 0).text())]['QT_1'] = self.BlueUnsortListQ1.item(
                i, 3).text()
        self.sort_res_q1(Data._participants_data)

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
            self.ResSortListQ1.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ1.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ1.item(n, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ1.item(n, 4).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            n += 1
        self.ResSortListQ1.sortItems(3)
        self.ResSortListQ1.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1)))
        for _ in range(1, self.ResSortListQ1.rowCount()):
            if self.ResSortListQ1.item(_, 3).text() == self.ResSortListQ1.item(_ - 1, 3).text():
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            else:
                place = _ + 1
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            self.ResSortListQ1.item(_, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        # for _ in range(break_flag, len(data)):
        #     self.ResSortListQ1.removeRow(break_flag)

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
                self.redListQ2.item(n, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.redListQ2.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.redListQ2.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                n += 1
            else:
                self.blueListQ2.insertRow(m)
                self.blueListQ2.setItem(m, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 1).text())))
                self.blueListQ2.setItem(m, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 2).text())))
                self.blueListQ2.setItem(m, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(t - 1, 3).text())))
                Data._participants_data[str(self.ResSortListQ1.item(t - 1, 1).text())]['QT2_course'] = 'Синяя'
                self.blueListQ2.item(m, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.blueListQ2.item(m, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.blueListQ1.item(m, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                m += 1

    def display_res_q2(self):
        self.get_time_qual2()
        self.RedUnsortListQ2.setRowCount(0)
        self.BlueUnsortListQ2.setRowCount(0)
        for n in range(self.redListQ2.rowCount()):
            self.RedUnsortListQ2.insertRow(n)
            self.RedUnsortListQ2.setItem(n, 0,
                                         QtWidgets.QTableWidgetItem(str(self.redListQ2.item(n, 0).text())))
            self.RedUnsortListQ2.setItem(n, 1,
                                         QtWidgets.QTableWidgetItem(str(
                                             Data._participants_data[str(self.redListQ2.item(n, 0).text())][
                                                 'С.Ф.'])))
            self.RedUnsortListQ2.setItem(n, 2,
                                         QtWidgets.QTableWidgetItem(str(self.redListQ2.item(n, 1).text())))
            self.RedUnsortListQ2.setItem(n, 3, QtWidgets.QTableWidgetItem(Data._participants_data[str(n + 1)]['QT_2']))
            self.RedUnsortListQ2.item(n, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.RedUnsortListQ2.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.RedUnsortListQ2.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        for m in range(self.blueListQ2.rowCount()):
            self.BlueUnsortListQ2.insertRow(m)
            self.BlueUnsortListQ2.setItem(m, 0,
                                          QtWidgets.QTableWidgetItem(str(self.blueListQ2.item(m, 0).text())))
            self.BlueUnsortListQ2.setItem(m, 1,
                                          QtWidgets.QTableWidgetItem(str(
                                              Data._participants_data[str(self.blueListQ2.item(m, 0).text())][
                                                  'С.Ф.'])))
            self.BlueUnsortListQ2.setItem(m, 2,
                                          QtWidgets.QTableWidgetItem(str(self.blueListQ2.item(m, 1).text())))
            self.BlueUnsortListQ2.setItem(m, 3, QtWidgets.QTableWidgetItem(Data._participants_data[str(m + 1)]['QT_2']))
            self.BlueUnsortListQ2.item(m, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.BlueUnsortListQ2.item(m, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.BlueUnsortListQ2.item(m, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def manual_time_2(self):
        for i in range(self.RedUnsortListQ2.rowCount()):
            Data._participants_data[str(self.RedUnsortListQ2.item(i, 0).text())]['QT_2'] = self.RedUnsortListQ2.item(i,
                                                                                                                     3).text()
        for i in range(self.BlueUnsortListQ2.rowCount()):
            Data._participants_data[str(self.BlueUnsortListQ2.item(i, 0).text())]['QT_2'] = self.BlueUnsortListQ2.item(
                i, 3).text()
        self.sort_res_q2()

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
            self.ResSortListQ2.item(n, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ2.item(n, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ2.item(n, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ2.item(n, 4).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.ResSortListQ2.item(n, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.ResSortListQ2.sortItems(4)
        self.ResSortListQ2.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1)))
        for _ in range(1, self.ResSortListQ2.rowCount()):
            if self.ResSortListQ2.item(_, 4).text() == self.ResSortListQ2.item(_ - 1, 4).text():
                self.ResSortListQ2.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            else:
                place = _ + 1
                self.ResSortListQ2.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            self.ResSortListQ2.item(_, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        # for _ in range(break_flag, self.ResSortListQ1.rowCount()):
        #     self.ResSortListQ2.removeRow(break_flag)

    def show_finals(self):
        self.tabWidget.setCurrentIndex(6)
        self.finalTable.setRowCount(0)

        default_fin = int(self.competition_data['rounds_amount'].split(sep='/')[1])
        x = 0
        heat_num = 1
        if self.qualificationsComboBox.currentText() == '2':
            for i in range(0, default_fin * 4, 4):
                self.finalTable.insertRow(i)
                self.finalTable.setItem(i, 0, QtWidgets.QTableWidgetItem('Heat ' + str(heat_num)))

                self.finalTable.insertRow(i + 1)
                self.finalTable.setItem(i + 1, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 0).text())))
                self.finalTable.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 1).text())))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 2).text())))
                self.finalTable.setItem(i + 1, 3, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(i + 1, 4, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                        'FT_{}_1'.format('1/' + str(default_fin))])))
                self.finalTable.setItem(i + 1, 5, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(i + 1, 6, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                        'FT_{}_2'.format('1/' + str(default_fin))])))
                self.finalTable.item(i + 1, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                x += 1

                self.finalTable.insertRow(i + 2)
                self.finalTable.setItem(i + 2, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 0).text())))
                self.finalTable.setItem(i + 2, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 1).text())))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 2, 1).text()].setdefault(
                    'FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 2, 1).text()].setdefault(
                    'FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(i + 2, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ2.item(x, 2).text())))
                self.finalTable.setItem(i + 2, 3, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(i + 2, 4, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                        'FT_{}_1'.format('1/' + str(default_fin))])))
                self.finalTable.setItem(i + 2, 5, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(i + 2, 6, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                        'FT_{}_2'.format('1/' + str(default_fin))])))
                self.finalTable.item(i + 2, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                x += 1

                self.finalTable.insertRow(i + 3)

                heat_num += 1

        else:
            for i in range(0, default_fin * 4, 4):
                self.finalTable.insertRow(i)
                self.finalTable.setItem(i, 0, QtWidgets.QTableWidgetItem('Heat ' + str(heat_num)))

                self.finalTable.insertRow(i + 1)
                self.finalTable.setItem(i + 1, 0,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 0).text())))
                self.finalTable.setItem(i + 1, 1,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 1).text())))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(i + 1, 2,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 2).text())))
                self.finalTable.setItem(i + 1, 3, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(i + 1, 4, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                        'FT_{}_1'.format('1/' + str(default_fin))])))
                self.finalTable.setItem(i + 1, 5, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(i + 1, 6, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                        'FT_{}_2'.format('1/' + str(default_fin))])))
                self.finalTable.item(i + 1, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 1, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                x += 1

                self.finalTable.insertRow(i + 2)
                self.finalTable.setItem(i + 2, 0,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 0).text())))
                self.finalTable.setItem(i + 2, 1,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 1).text())))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 2, 1).text()].setdefault(
                    'FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[self.finalTable.item(i + 2, 1).text()].setdefault(
                    'FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[self.finalTable.item(i + 1, 1).text()].setdefault(
                    'FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(i + 2, 2,
                                        QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(x, 2).text())))
                self.finalTable.setItem(i + 2, 3, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(i + 2, 4, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                        'FT_{}_1'.format('1/' + str(default_fin))])))
                self.finalTable.setItem(i + 2, 5, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(i + 2, 6, QtWidgets.QTableWidgetItem(str(
                    Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                        'FT_{}_2'.format('1/' + str(default_fin))])))
                self.finalTable.item(i + 2, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(i + 2, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                x += 1

                self.finalTable.insertRow(i + 3)

                heat_num += 1

    def confirm_final_time(self):
        round_num = self.comboBoxFinals.currentText()
        for i in range(0, self.finalTable.rowCount(), 4):
            Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                'FT_{}_1'.format(round_num)] = self.finalTable.item(i + 1, 4).text()
            Data._participants_data[self.finalTable.item(i + 1, 1).text()][
                'FT_{}_2'.format(round_num)] = self.finalTable.item(i + 1, 6).text()
            Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                'FT_{}_1'.format(round_num)] = self.finalTable.item(i + 2, 4).text()
            Data._participants_data[self.finalTable.item(i + 2, 1).text()][
                'FT_{}_2'.format(round_num)] = self.finalTable.item(i + 2, 6).text()
            if Data._participants_data[self.finalTable.item(i + 1, 1).text()]['FT_{}_2'.format(round_num)] < \
                    Data._participants_data[self.finalTable.item(i + 2, 1).text()]['FT_{}_2'.format(round_num)]:
                Data._participants_data[self.finalTable.item(i + 1, 1).text()]['FT_{}_win'.format(round_num)] = '+'
                Data._participants_data[self.finalTable.item(i + 2, 1).text()]['FT_{}_win'.format(round_num)] = '-'
            else:
                Data._participants_data[self.finalTable.item(i + 1, 1).text()]['FT_{}_win'.format(round_num)] = '-'
                Data._participants_data[self.finalTable.item(i + 2, 1).text()]['FT_{}_win'.format(round_num)] = '+'

        for i in Data._participants_data:
            try:
                if Data._participants_data[str(i)]['FT_BF|SF_win'] == '+' and Data._participants_data[str(i)][
                    'FT_1/2_win'] == '+':
                    self.labelFstPlace.setText(
                        '1 место = участник {}'.format(Data._participants_data[str(i)]['Фамилия Имя']))
                elif Data._participants_data[str(i)]['FT_BF|SF_win'] == '-' and Data._participants_data[str(i)][
                    'FT_1/2_win'] == '+':
                    self.labelScndPlace.setText(
                        '2 место = участник {}'.format(Data._participants_data[str(i)]['Фамилия Имя']))
                elif Data._participants_data[str(i)]['FT_BF|SF_win'] == '+' and Data._participants_data[str(i)][
                    'FT_1/2_win'] == '-':
                    self.labelThrdPlace.setText(
                        '3 место = участник {}'.format(Data._participants_data[str(i)]['Фамилия Имя']))
            except KeyError:
                continue

    def finals(self):
        if self.comboBoxFinals.currentText() == self.roundsComboBox.currentText():
            self.show_finals()
            print('Welcome back')
        elif self.comboBoxFinals.currentText() == 'BF|SF':
            self.bf_sf()
        else:
            heat_num = int(self.finalTable.item(self.finalTable.rowCount() - 4, 0).text()[5::]) + 1
            default_fin = int(self.comboBoxFinals.currentText().split(sep='/')[1])
            prev_fin = self.comboBoxFinals.itemText(self.comboBoxFinals.currentIndex() - 1)
            self.finalTable.setRowCount(0)
            data_indexes = []
            ind = 0
            for i in Data._participants_data:
                try:
                    if Data._participants_data[str(i)]['FT_{}_win'.format(prev_fin)] == '+':
                        data_indexes.append(str(i))
                except KeyError:
                    continue

            for x in range(0, default_fin * 4, 4):
                self.finalTable.insertRow(x)
                self.finalTable.setItem(x, 0, QtWidgets.QTableWidgetItem('Heat ' + str(heat_num)))

                self.finalTable.insertRow(x + 1)
                self.finalTable.setItem(x + 1, 0, QtWidgets.QTableWidgetItem(str('')))
                self.finalTable.setItem(x + 1, 1, QtWidgets.QTableWidgetItem(
                    str(Data._participants_data[data_indexes[ind]]['Ст№'])))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(x + 1, 2, QtWidgets.QTableWidgetItem(
                    str(Data._participants_data[data_indexes[ind]]['Фамилия Имя'])))
                self.finalTable.setItem(x + 1, 3, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(x + 1, 4, QtWidgets.QTableWidgetItem(
                    Data._participants_data[data_indexes[ind]]['FT_{}_1'.format('1/' + str(default_fin))]))
                self.finalTable.setItem(x + 1, 5, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(x + 1, 6, QtWidgets.QTableWidgetItem(
                    Data._participants_data[data_indexes[ind]]['FT_{}_2'.format('1/' + str(default_fin))]))
                self.finalTable.item(x + 1, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 1, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 1, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 1, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 1, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                ind += 1

                self.finalTable.insertRow(x + 2)
                self.finalTable.setItem(x + 2, 0, QtWidgets.QTableWidgetItem(str('')))
                self.finalTable.setItem(x + 2, 1, QtWidgets.QTableWidgetItem(
                    str(Data._participants_data[data_indexes[ind]]['Ст№'])))

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_1'.format('1/' + str(default_fin)), timer)

                min_time = int(random.uniform(1, 59))
                sec_time = int(random.uniform(1, 59))
                micro_time = int(random.uniform(9999, 999999))
                timer = str(time(hour=0, minute=min_time, second=sec_time,
                                 microsecond=micro_time))[3:]

                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_2'.format('1/' + str(default_fin)), timer)
                Data._participants_data[data_indexes[ind]].setdefault('FT_{}_win'.format('1/' + str(default_fin)))
                self.finalTable.setItem(x + 2, 2, QtWidgets.QTableWidgetItem(
                    Data._participants_data[data_indexes[ind]]['Фамилия Имя']))
                self.finalTable.setItem(x + 2, 3, QtWidgets.QTableWidgetItem('с'))
                self.finalTable.setItem(x + 2, 4, QtWidgets.QTableWidgetItem(
                    Data._participants_data[data_indexes[ind]]['FT_{}_1'.format('1/' + str(default_fin))]))
                self.finalTable.setItem(x + 2, 5, QtWidgets.QTableWidgetItem('к'))
                self.finalTable.setItem(x + 2, 6, QtWidgets.QTableWidgetItem(
                    Data._participants_data[data_indexes[ind]]['FT_{}_2'.format('1/' + str(default_fin))]))
                self.finalTable.item(x + 2, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 2, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 2, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 2, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.finalTable.item(x + 2, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                ind += 1

                self.finalTable.insertRow(x + 3)

                heat_num += 1

    def bf_sf(self):
        # heat_num = int(self.finalTable.item(self.finalTable.rowCount() - 4, 0).text()[5::]) + 1
        default_fin = self.comboBoxFinals.currentText()
        self.finalTable.setRowCount(0)
        data_indexes_win = []
        data_indexes_lose = []
        ind = 0
        for i in Data._participants_data:
            try:
                if Data._participants_data[str(i)]['FT_{}_win'.format('1/2')] == '+':
                    data_indexes_win.append(str(i))
                elif Data._participants_data[str(i)]['FT_{}_win'.format('1/2')] == '-':
                    data_indexes_lose.append(str(i))
            except KeyError:
                continue

        for x in range(0, 4, 4):
            self.finalTable.insertRow(x)
            self.finalTable.setItem(x, 0, QtWidgets.QTableWidgetItem('Big Final'))

            self.finalTable.insertRow(x + 1)
            self.finalTable.setItem(x + 1, 0, QtWidgets.QTableWidgetItem(str('')))
            self.finalTable.setItem(x + 1, 1,
                                    QtWidgets.QTableWidgetItem(
                                        str(Data._participants_data[data_indexes_win[ind]]['Ст№'])))

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_1'.format(str(default_fin)), timer)

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_2'.format(str(default_fin)), timer)
            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_win'.format(str(default_fin)))
            self.finalTable.setItem(x + 1, 2, QtWidgets.QTableWidgetItem(
                str(Data._participants_data[data_indexes_win[ind]]['Фамилия Имя'])))
            self.finalTable.setItem(x + 1, 3, QtWidgets.QTableWidgetItem('к'))
            self.finalTable.setItem(x + 1, 4, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_win[ind]]['FT_{}_1'.format(str(default_fin))]))
            self.finalTable.setItem(x + 1, 5, QtWidgets.QTableWidgetItem('с'))
            self.finalTable.setItem(x + 1, 6, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_win[ind]]['FT_{}_2'.format(str(default_fin))]))
            self.finalTable.item(x + 1, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            ind += 1

            self.finalTable.insertRow(x + 2)
            self.finalTable.setItem(x + 2, 0, QtWidgets.QTableWidgetItem(str('')))
            self.finalTable.setItem(x + 2, 1,
                                    QtWidgets.QTableWidgetItem(
                                        str(Data._participants_data[data_indexes_win[ind]]['Ст№'])))

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_1'.format(str(default_fin)), timer)

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_2'.format(str(default_fin)), timer)
            Data._participants_data[data_indexes_win[ind]].setdefault('FT_{}_win'.format(str(default_fin)))
            self.finalTable.setItem(x + 2, 2, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_win[ind]]['Фамилия Имя']))
            self.finalTable.setItem(x + 2, 3, QtWidgets.QTableWidgetItem('с'))
            self.finalTable.setItem(x + 2, 4, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_win[ind]]['FT_{}_1'.format(str(default_fin))]))
            self.finalTable.setItem(x + 2, 5, QtWidgets.QTableWidgetItem('к'))
            self.finalTable.setItem(x + 2, 6, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_win[ind]]['FT_{}_2'.format(str(default_fin))]))
            self.finalTable.item(x + 2, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            ind += 1

            self.finalTable.insertRow(x + 3)

            # heat_num += 1

        ind = 0
        print(data_indexes_lose, data_indexes_win)
        for x in range(4, 8, 4):
            self.finalTable.insertRow(x)
            self.finalTable.setItem(x, 0, QtWidgets.QTableWidgetItem('Small Final'))

            self.finalTable.insertRow(x + 1)
            self.finalTable.setItem(x + 1, 0, QtWidgets.QTableWidgetItem(str('')))
            self.finalTable.setItem(x + 1, 1,
                                    QtWidgets.QTableWidgetItem(
                                        str(Data._participants_data[data_indexes_lose[ind]]['Ст№'])))

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_1'.format(str(default_fin)), timer)

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_2'.format(str(default_fin)), timer)
            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_win'.format(str(default_fin)))
            self.finalTable.setItem(x + 1, 2, QtWidgets.QTableWidgetItem(
                str(Data._participants_data[data_indexes_lose[ind]]['Фамилия Имя'])))
            self.finalTable.setItem(x + 1, 3, QtWidgets.QTableWidgetItem('к'))
            self.finalTable.setItem(x + 1, 4, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_lose[ind]]['FT_{}_1'.format(str(default_fin))]))
            self.finalTable.setItem(x + 1, 5, QtWidgets.QTableWidgetItem('с'))
            self.finalTable.setItem(x + 1, 6, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_lose[ind]]['FT_{}_2'.format(str(default_fin))]))
            self.finalTable.item(x + 1, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 1, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            ind += 1

            self.finalTable.insertRow(x + 2)
            self.finalTable.setItem(x + 2, 0, QtWidgets.QTableWidgetItem(str('')))
            self.finalTable.setItem(x + 2, 1,
                                    QtWidgets.QTableWidgetItem(
                                        str(Data._participants_data[data_indexes_lose[ind]]['Ст№'])))

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_1'.format(str(default_fin)), timer)

            min_time = int(random.uniform(1, 59))
            sec_time = int(random.uniform(1, 59))
            micro_time = int(random.uniform(9999, 999999))
            timer = str(time(hour=0, minute=min_time, second=sec_time,
                             microsecond=micro_time))[3:]

            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_2'.format(str(default_fin)), timer)
            Data._participants_data[data_indexes_lose[ind]].setdefault('FT_{}_win'.format(str(default_fin)))
            self.finalTable.setItem(x + 2, 2, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_lose[ind]]['Фамилия Имя']))
            self.finalTable.setItem(x + 2, 3, QtWidgets.QTableWidgetItem('с'))
            self.finalTable.setItem(x + 2, 4, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_lose[ind]]['FT_{}_1'.format(str(default_fin))]))
            self.finalTable.setItem(x + 2, 5, QtWidgets.QTableWidgetItem('к'))
            self.finalTable.setItem(x + 2, 6, QtWidgets.QTableWidgetItem(
                Data._participants_data[data_indexes_lose[ind]]['FT_{}_2'.format(str(default_fin))]))
            self.finalTable.item(x + 2, 0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 1).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 2).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 3).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.finalTable.item(x + 2, 5).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            ind += 1

            self.finalTable.insertRow(x + 3)

            # heat_num += 1
