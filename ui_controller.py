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

    def save_settings_callback(self):
        Data.save_settings(self)
        sleep(1)
        self.tabWidget.setCurrentIndex(1)
        print("Данные сохранены!")

    def load_file_callback(self):
        Data.choose_file_participants(self)
        Data.load_file(self)
        self.display_participants(Data._participants_data)
        self.divide(Data._participants_data)

    def display_participants(self, data):
        self.participantsTable.setRowCount(0)
        row = 0
        for entry in data:
            self.participantsTable.insertRow(row)
            self.participantsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(str(entry["Ст№"])))
            self.participantsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(entry["С.Ф."])))
            self.participantsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(entry["Фамилия Имя"])))
            self.participantsTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(entry["Г.р."])))
            self.participantsTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(entry["Спорт. разр."])))
            self.participantsTable.setItem(row, 5, QtWidgets.QTableWidgetItem(str(entry["Очки КР"])))
            row += 1

    def divide(self, data):
        self.redListQ1.setRowCount(0)
        self.blueListQ1.setRowCount(0)
        t = n = m = 0
        for x in data:
            if data[t]['Ст№'] % 2 == 1:
                self.redListQ1.insertRow(n)
                self.redListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(x["Ст№"])))
                self.redListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x["С.Ф."])))
                self.redListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
                self.redListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
                self.redListQ1.setItem(n, 4, QtWidgets.QTableWidgetItem(str(x["Спорт. разр."])))
                n += 1
            else:
                self.blueListQ1.insertRow(m)
                self.blueListQ1.setItem(m, 0, QtWidgets.QTableWidgetItem(str(x["Ст№"])))
                self.blueListQ1.setItem(m, 1, QtWidgets.QTableWidgetItem(str(x["С.Ф."])))
                self.blueListQ1.setItem(m, 2, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
                self.blueListQ1.setItem(m, 3, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
                self.blueListQ1.setItem(m, 4, QtWidgets.QTableWidgetItem(str(x["Спорт. разр."])))
                m += 1
            t += 1

    def display_res_q1(self, data):
        Data.get_time(self)
        self.ResUnsortListQ1.setRowCount(0)
        n = 0
        for x in data:
            self.ResUnsortListQ1.insertRow(n)
            self.ResUnsortListQ1.setItem(n, 0, QtWidgets.QTableWidgetItem(str(x["Ст№"])))
            self.ResUnsortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
            self.ResUnsortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
            self.ResUnsortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(
                str(x["FT{0}_{1}".format(self.roundsComboBox.currentText(), self.runsComboBox.currentText())])))
            n += 1

    def sort_res_q1(self, data):
        self.ResSortListQ1.setRowCount(0)
        n = 0
        z = self.roundsComboBox.currentText().split(sep='/')
        z = int(z[1])
        place = 1
        for x in data:
            self.ResSortListQ1.insertRow(n)
            self.ResSortListQ1.setItem(n, 1, QtWidgets.QTableWidgetItem(str(x["Ст№"])))
            self.ResSortListQ1.setItem(n, 2, QtWidgets.QTableWidgetItem(str(x["С.Ф."])))
            self.ResSortListQ1.setItem(n, 3, QtWidgets.QTableWidgetItem(str(x["Фамилия Имя"])))
            self.ResSortListQ1.setItem(n, 4, QtWidgets.QTableWidgetItem(str(x["Г.р."])))
            self.ResSortListQ1.setItem(n, 5, QtWidgets.QTableWidgetItem(
                str(x["FT{0}_{1}".format(self.roundsComboBox.currentText(), self.runsComboBox.currentText())])))
            n += 1
            if n == z * 2:
                self.ResSortListQ1.sortItems(5)
                break
        for _ in range(z * 2):
            self.ResSortListQ1.setItem(_, 0, QtWidgets.QTableWidgetItem(str(place)))
            place += 1
