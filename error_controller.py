from PySide2 import QtWidgets

import errordialog


class ErrorController(QtWidgets.QMainWindow, errordialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonOK.clicked.connect(self.close)

    def error_msg_fio(self, i):
        self.labelError.setText('Ошибка в строке {}: неверные ФИО!'.format(i))

    def error_msg_bib(self, i):
        self.labelError.setText('Ошибка в строке {}: неверный bib!'.format(i))

    def error_msg_double(self, i):
        self.labelError.setText('Ошибка в строке {}: неверные bib и ФИО!'.format(i))

    def wrong_bib(self, i, j):
        self.labelError.setText('bib в строке {i} совпадает с bib в троке {j}!'.format(i=i, j=j))

    def wrong_bib_type(self, i):
        self.labelError.setText('bib в строке {} должен быть числом'.format(i))
