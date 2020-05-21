from PySide2 import QtCore, QtWidgets, QtGui
import new_form
from data_controller import Data
from time import sleep


class Controller(QtWidgets.QMainWindow, new_form.Ui_MainWindow, Data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saveParams.clicked.connect(self.save_settings_callback)
        self.pushButtonLoadList.clicked.connect(self.load_file_callback)
        self.pushButtonAccept.clicked.connect(self.display_res_callback)

    def display_res_callback(self):
        sleep(1)
        self.tabWidget.setCurrentIndex(3)
        self.display_res_q1(Data._participants_data)
        self.sort_res_q1(Data._participants_data)
        if self.competition_data['Q_amount'] == '2':
            self.divideQ2()
            self.display_res_q2()
            self.sort_res_q2()

    def save_settings_callback(self):
        Data.save_settings(self)
        sleep(1)
        self.tabWidget.setCurrentIndex(1)
        print('Данные сохранены!')

    def load_file_callback(self):
        Data.choose_file_participants(self)
        Data.load_file(self)
        self.display_participants(Data._participants_data)
        self.divideQ1(Data._participants_data)

    def display_participants(self, data):
        self.participantsTable.setRowCount(0)
        row = 0
        for entry in data:
            self.participantsTable.insertRow(row)
            self.participantsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry['Ст№'])))
            self.participantsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry['С.Ф.'])))
            self.participantsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry['Фамилия Имя'])))
            self.participantsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry['Г.р.'])))
            self.participantsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry['Спорт. разр.'])))
            self.participantsTable.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry['Очки КР'])))
            row += 1

    def divideQ1(self, data):
        self.redListQ1.setRowCount(0)
        self.blueListQ1.setRowCount(0)
        t = n = m = 0
        for x in data:

            if data[t]['Ст№'] % 2 == 1:
                self.redListQ1.insertRow(n)
                self.redListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(x['Ст№'])))
                self.redListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x['С.Ф.'])))
                self.redListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x['Фамилия Имя'])))
                self.redListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x['Спорт. разр.'])))
                Data._participants_data[t]['QT1_course'] = 'Красная'
                n += 1
            else:
                self.blueListQ1.insertRow(m)
                self.blueListQ1.setItem(m, 0, QtWidgets.QTableWidgetItem(str(x['Ст№'])))
                self.blueListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(x['С.Ф.'])))
                self.blueListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(x['Фамилия Имя'])))
                self.blueListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(x['Спорт. разр.'])))
                Data._participants_data[t]['QT1_course'] = 'Синяя'
                m += 1
            t += 1

    def display_res_q1(self, data):
        Data.get_time_qual1(self)
        self.ResUnsortListQ1.setRowCount(0)
        n = 0
        for x in data:
            self.ResUnsortListQ1.insertRow(n)
            self.ResUnsortListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(x['Ст№'])))
            self.ResUnsortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x['Фамилия Имя'])))
            self.ResUnsortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x['QT_1'])))
            self.ResUnsortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x['QT1_course'])))
            n += 1

    def sort_res_q1(self, data):
        self.ResSortListQ1.setRowCount(0)
        n = 0
        place = 1
        if len(data) % 2 == 0:
            break_flag = len(data) // 2 + 2
        else:
            break_flag = len(data) // 2 + 1
        for x in data:
            self.ResSortListQ1.insertRow(n)
            self.ResSortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x['Ст№'])))
            self.ResSortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x['С.Ф.'])))
            self.ResSortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x['Фамилия Имя'])))
            self.ResSortListQ1.setItem(n, 4, QtWidgets.QTableWidgetItem(str(x['QT_1'])))
            self.ResSortListQ1.setItem(n, 5, QtWidgets.QTableWidgetItem(str(x['QT1_course'])))
            n += 1
            self.ResSortListQ1.sortItems(4)
        self.ResSortListQ1.setItem(0, 0, QtWidgets.QTableWidgetItem(str(1)))
        for _ in range(1, break_flag + 1):
            if self.ResSortListQ1.item(_, 4).text() == self.ResSortListQ1.item(_ - 1, 4).text():
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            else:
                place = _ + 1
                self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
        for _ in range(break_flag, len(data)):
            self.ResSortListQ1.removeRow(break_flag)

    # TODO переписать под реалии пройденного КУ1
    def divideQ2(self):
        self.redListQ2.setRowCount(0)
        self.blueListQ2.setRowCount(0)
        t = x = m = 0
        for n in range(self.ResSortListQ1.rowCount()):
            # if Data._participants_data[t]['Ст№'] % 2 == 1:
            self.redListQ2.insertRow(n)
            self.redListQ2.setItem(n, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 1).text())))
            self.redListQ2.setItem(n, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 3).text())))
            self.redListQ2.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 4).text())))
            # Data._participants_data[t]['QT2_course'] = 'Красная'
            # # n += 1
            # # else:
            # self.blueListQ2.insertRow(m)
            # self.blueListQ2.setItem(m, 0, QtWidgets.QTableWidgetItem(str(x['Ст№'])))
            # self.blueListQ2.setItem(m, 1, QtWidgets.QTableWidgetItem(str(x['С.Ф.'])))
            # self.blueListQ2.setItem(m, 2, QtWidgets.QTableWidgetItem(str(x['Фамилия Имя'])))
            # self.blueListQ2.setItem(m, 3, QtWidgets.QTableWidgetItem(str(x['Спорт. разр.'])))
            # Data._participants_data[t]['QT2_course'] = 'Синяя'
            n += 1
        # t += 1

    def display_res_q2(self):
        Data.get_time_qual2(self)
        self.ResUnsortListQ2.setRowCount(0)
        for n in range(self.ResSortListQ1.rowCount()):
            self.ResUnsortListQ2.insertRow(n)
            self.ResUnsortListQ2.setItem(n, 0, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 1).text())))
            self.ResUnsortListQ2.setItem(n, 1, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 3).text())))
            self.ResUnsortListQ2.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.ResSortListQ1.item(n, 4).text())))
            self.ResUnsortListQ2.setItem(n, 3, QtWidgets.QTableWidgetItem(str(Data._participants_data[n]['QT_2'])))

    def sort_res_q2(self):
        self.ResSortListQ2.setRowCount(0)
        place = 1
        break_flag = self.ResSortListQ1.rowCount() // 2
        for n in range(break_flag):
            self.ResSortListQ2.insertRow(n)
            self.ResSortListQ2.setItem(n, 1, QtWidgets.QTableWidgetItem(str(self.ResUnsortListQ2.item(n, 0).text())))
            self.ResSortListQ2.setItem(n, 2, QtWidgets.QTableWidgetItem(str(self.ResUnsortListQ2.item(n, 1).text())))
            self.ResSortListQ2.setItem(n, 3, QtWidgets.QTableWidgetItem(str(self.ResUnsortListQ2.item(n, 2).text())))
            self.ResSortListQ2.setItem(n, 4, QtWidgets.QTableWidgetItem(str(self.ResUnsortListQ2.item(n, 3).text())))
            self.ResSortListQ2.setItem(n, 5, QtWidgets.QTableWidgetItem(str(Data._participants_data[n]['QT2_course'])))
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
